# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import json
import os
from datetime import datetime
import numpy
from tvb.core.neocom import h5
from tvb.storage.storage_interface import StorageInterface

from tvbextxircuits.utils import STORAGE_CONFIG_FILE, STORE_RESULTS_DIR, BUCKET_NAME_KEY, FOLDER_PATH_KEY
from xai_components.base import xai_component, Component, InArg, InCompArg


@xai_component(color='rgb(153,0,102)')
class StoreResults(Component):
    data_to_store: InCompArg[list]
    bucket_name: InArg[str]
    folder_path: InArg[str]
    H5_format: InArg[bool]

    def __init__(self):
        self.done = False
        self.is_hpc_launch = False
        self.bucket_name = InArg(None)
        self.folder_path = InArg('')
        self.H5_format = InArg(False)

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
        if self.bucket_name.value is not None:
            self._store_to_bucket()
        else:
            self._store_to_drive()

    def _store_to_bucket(self):
        # TODO: store results to bucket as well
        print(f"TODO: Storing results to bucket {self.bucket_name.value}...")

    def _store_to_drive(self):
        # prepare output folder
        output_directory = STORE_RESULTS_DIR
        if not self.is_hpc_launch:
            output_directory = os.path.join(self.folder_path.value, output_directory)
        if os.path.isdir(output_directory):
            output_directory += f"_{datetime.now().strftime('%m.%d.%Y_%H:%M:%S')}"
        os.mkdir(output_directory)

        for data_piece in self.data_to_store.value:
            StoreFactory.store_data_piece(data_piece, output_directory, self.H5_format.value)


class StoreFactory(object):

    @staticmethod
    def store_data_piece(data_piece, output_directory, h5_format):
        from tvb.datatypes.time_series import TimeSeries

        if issubclass(type(data_piece), TimeSeries):
            StoreFactory.store_time_series(data_piece, output_directory, h5_format)
        else:
            print(f"Cannot store data of type {type(data_piece)} yet. Please contact the development team for this.")

    @staticmethod
    def store_time_series(time_series, output_directory, h5_format):
        if h5_format:
            ts_file_name = StorageInterface.FILE_NAME_STRUCTURE.format(type(time_series).__name__, time_series.gid.hex)
            ts_file_path = os.path.join(output_directory, ts_file_name)
            print(f"Storing timeseries for {time_series.title} monitor to {ts_file_path}...", flush=True)
            h5.store(time_series, ts_file_path)
        else:
            ts_file_path = os.path.join(output_directory, f"timeseries_{time_series.title}.npy")
            print(f"Storing timeseries for {time_series.title} monitor to {ts_file_path}...", flush=True)
            numpy.save(ts_file_path, time_series.data)
