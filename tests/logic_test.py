#!/usr/bin/env python

from mpkg import csv_io
from mpkg import data_man
import os


def logic_test():
    # known metrics

    deaccum_test = csv_io.csv_input(os.getcwd().replace('\\', '/') + "/test_csv_files/input/deaccumRainfall_test.csv")
    path = os.getcwd().replace('\\', '/') + "/test_csv_files/input/accumRainfall_test.csv"
    accum_data = csv_io.csv_input(path)
    deaccum_data = data_man.deaccum_data(accum_data)

    for itt in range(0, len(deaccum_data)):
        if round(deaccum_test[itt][1], 2) != round(deaccum_data[itt][1], 2):
            print("de-accumulation test: Failed")
        else:
            print("de-accumulation test: Passed")


logic_test()

