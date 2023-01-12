# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import os
from datetime import datetime
import numpy

from xai_components.base import xai_component, Component, InArg, InCompArg


@xai_component(color='rgb(47,79,79)')
class StoreResults(Component):
    data_to_store: InCompArg[list]
    bucket_name: InArg[str]
    folder_path: InArg[str]
    H5_format: InArg[bool]

    def __init__(self):
        self.done = False
        self.bucket_name = InArg(None)
        self.folder_path = InArg('')
        self.H5_format = InArg(False)

    def execute(self, ctx) -> None:
        if self.bucket_name.value is not None:
            self._store_to_bucket()
        else:
            self._store_to_drive()

    def _store_to_bucket(self):
        print(f"Will store results to bucket {self.bucket_name.value}...")

    def _store_to_drive(self):
        # prepare output folder
        output_directory = os.path.join(self.folder_path.value, 'results')
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
            print(f"Storing to H5 is not supported yet. Will be added soon...")
        else:
            ts_file_name = os.path.join(output_directory, f"timeseries_{time_series.title}.npy")
            print(f"Storing timeseries for {time_series.title} monitor to {ts_file_name}...")
            numpy.save(ts_file_name, time_series.data)
