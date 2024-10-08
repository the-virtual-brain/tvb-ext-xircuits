# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import json
import os
import shutil
from datetime import datetime
import ebrains_drive
import numpy
from ebrains_drive.exceptions import DoesNotExist
from tvb.config.init.datatypes_registry import populate_datatypes_registry
from tvb.core.neocom import h5
from tvb.storage.storage_interface import StorageInterface
from tvb_ext_bucket.ebrains_drive_wrapper import BucketWrapper
from tvb_ext_bucket.exceptions import CollabAccessError
from tvbwidgets.core.auth import get_current_token

from tvbextxircuits.utils import *
from xai_components.base import xai_component, InArg, InCompArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.logger.builder import get_logger
from typing import Literal

LOGGER = get_logger(__name__)


@xai_component(color='rgb(153,0,102)')
class StoreResultsToDrive(ComponentWithWidget):
    data_to_store: InCompArg[list]
    collab_name: InCompArg[str]
    folder_path: InArg[str]
    format: InArg[Literal['h5', 'npz']]

    def __init__(self):
        self.done = False
        self.is_hpc_launch = False
        self.collab_name = InArg('')
        self.folder_path = InArg('')
        self.format = InArg('npz')

    def execute(self, ctx) -> None:
        args = ctx.get('args')
        if args is not None:
            self.is_hpc_launch = args.is_hpc_launch
        if self.is_hpc_launch:
            # Save the config in json format for stage-out step
            json_config = {COLLAB_NAME_KEY: self.collab_name.value,
                           FOLDER_PATH_KEY: self.folder_path.value}
            with open(STORAGE_CONFIG_FILE, 'w') as f:
                json.dump(json_config, f)
        self._store_to_drive()

    def _store_to_drive(self):
        # prepare output folder
        temp_local_directory = create_temporary_dir()

        files_to_upload = list()
        for data_piece in self.data_to_store.value:
            data_file = StoreFactory.store_data_piece(data_piece, temp_local_directory, self.format.value)
            files_to_upload.append(data_file)

        if not self.is_hpc_launch:
            is_stored = self._upload_to_drive(files_to_upload, temp_local_directory)
            if is_stored:
                remove_temporary_dir(temp_local_directory)

    @staticmethod
    def connect_to_drive():
        bearer_token = get_current_token()
        client = ebrains_drive.connect(token=bearer_token)
        return client

    @staticmethod
    def create_results_folder_in_collab(collab_name, folder_path, output_directory):
        drive_client = StoreResultsToDrive.connect_to_drive()
        repos = drive_client.repos.get_repos_by_name(collab_name)

        if repos is None or len(repos) == 0:
            LOGGER.error(f'Could not find the selected Collab {collab_name} within the Drive.')
            return False

        if len(repos) > 1:
            LOGGER.warn(f'Found multiple Collabs with the name {collab_name}. Storing files to the first one...')

        if not folder_path.startswith('/'):
            folder_path = '/' + folder_path

        try:
            folder = repos[0].get_dir(folder_path)
        except DoesNotExist:
            folder = repos[0].get_dir('/')
            LOGGER.warn(f'Folder {folder_path} does not exist under the chosen Collab. Will store files under root...')

        sub_folder = folder.mkdir(output_directory)
        LOGGER.info(f'Folder {sub_folder.path} has been created into Drive, under Collab {collab_name}')
        return sub_folder

    def _upload_to_drive(self, files_to_upload, output_directory):
        LOGGER.info('Uploading files to Drive...')
        sub_folder = self.create_results_folder_in_collab(self.collab_name.value, self.folder_path.value,
                                                          output_directory)
        if sub_folder is False:
            return False

        for file_to_upload in files_to_upload:
            file = sub_folder.upload_local_file(file_to_upload)
            LOGGER.info(f'File {file.path} has been stored to Drive')
        return True


@xai_component(color='rgb(153,0,102)')
class StoreResultsToBucket(ComponentWithWidget):
    data_to_store: InCompArg[list]
    bucket_name: InCompArg[str]
    folder_path: InArg[str]
    format: InArg[Literal['h5', 'npz']]

    def __init__(self):
        self.done = False
        self.is_hpc_launch = False
        self.bucket_name = InArg('')
        self.folder_path = InArg('')
        self.format = InArg('npz')

    def execute(self, ctx) -> None:
        args = ctx.get('args')
        if args is not None:
            self.is_hpc_launch = args.is_hpc_launch
        if self.is_hpc_launch:
            # Save the config in json format for stage-out step
            json_config = {BUCKET_NAME_KEY: self.bucket_name.value,
                           FOLDER_PATH_KEY: self.folder_path.value}
            with open(STORAGE_CONFIG_FILE, 'w') as f:
                json.dump(json_config, f)
        self._store_to_bucket()

    def _upload_to_bucket(self, files_to_upload, output_directory):
        LOGGER.info('Uploading files to Drive...')
        bucket_wrapper = BucketWrapper()

        for file_to_upload in files_to_upload:
            filename = os.path.basename(file_to_upload)
            folder = os.path.join(self.folder_path.value, output_directory)

            try:
                is_uploaded = bucket_wrapper.upload_file_to(file_to_upload, self.bucket_name.value, folder, filename)
                if is_uploaded:
                    LOGGER.info(f'File {file_to_upload} has been stored to Bucket')
                    return True
                else:
                    LOGGER.info(f'Could not upload file {file_to_upload} to the selected Bucket. '
                                f'You can find the results locally.')
                    return False

            except CollabAccessError:
                LOGGER.info(f'Could not upload file {file_to_upload} to the selected Bucket. '
                            f'You can find the results locally.')
                return False

    def _store_to_bucket(self):
        # prepare output folder
        temp_local_directory = create_temporary_dir()

        files_to_upload = list()
        for data_piece in self.data_to_store.value:
            data_file = StoreFactory.store_data_piece(data_piece, temp_local_directory, self.format.value)
            files_to_upload.append(data_file)

        if not self.is_hpc_launch:
            is_stored = self._upload_to_bucket(files_to_upload, temp_local_directory)
            if is_stored:
                remove_temporary_dir(temp_local_directory)


def create_temporary_dir():
    dirname = STORE_RESULTS_DIR + f"_{datetime.now().strftime(DIR_TIME_STAMP_FRMT)}"
    os.mkdir(dirname)
    return dirname


def remove_temporary_dir(dirname):
    LOGGER.info(f'Removing temporary local folder {dirname}')
    shutil.rmtree(dirname)


class StoreFactory(object):

    @staticmethod
    def store_data_piece(data_piece, output_directory, save_format):
        from tvb.datatypes.time_series import TimeSeries

        if issubclass(type(data_piece), TimeSeries):
            return StoreFactory.store_time_series(data_piece, output_directory, save_format)
        else:
            LOGGER.error(f"Cannot store data of type {type(data_piece)} yet. "
                         f"Please contact the development team for this.")

    @staticmethod
    def store_time_series(time_series, output_directory, save_format):
        if save_format == 'h5':
            ts_file_name = StorageInterface.FILE_NAME_STRUCTURE.format(type(time_series).__name__, time_series.gid.hex)
            ts_file_path = os.path.join(output_directory, ts_file_name)
            LOGGER.info(f"Storing timeseries for {time_series.title} monitor temporary to {ts_file_path}...")
            populate_datatypes_registry()
            h5.store(time_series, ts_file_path)
        elif save_format == 'npz':
            ts_file_path = os.path.join(output_directory, f"timeseries_{time_series.title}.npz")
            LOGGER.info(f"Storing timeseries for {time_series.title} monitor temporary to {ts_file_path}...")
            numpy.savez(ts_file_path, data=time_series.data, time=time_series.time)
        else:
            raise NotImplementedError("this format is not supported yet")
        return ts_file_path
