#!/usr/bin/env python
# Version: 1.0
# Created by: Lachlan Sneddon

import csv
import os
import time


def csv_input(path):
    # Takes in csv path
    # Returns list of tuples

    with open(path, 'r') as fcsv:  # with closes io after use
        reader = csv.reader(fcsv, delimiter=",")
        csv_data = []
        next(reader, None)  # skips over header

        epoch_time = int(time.time())  # int cast will always round down
        for count, row in enumerate(reader, 2):
            # checks to ensure recorded time is positive and historical
            # checks to ensure rain measurement is positive (a maximum could be improper)
            if 0 <= int(row[0]) <= epoch_time:
                if float(row[1]) >= 0:
                    csv_data += [(int(row[0]), row[1])]
                else:
                    raise Exception("invalid rain measurement on line " + str(count) + " of csv")
            else:
                raise Exception("invalid time measurement on line " + str(count) + " of csv")

    # in event data is not ordered sequentially
    csv_data.sort()
    return csv_data


def csv_output(data_list, filename):
    # writes csv file to output directory

    if filename.lower().endswith(".csv"):
        filename = filename[:-4]

    output_path = os.getcwd().replace('\\', '/') + "/csv_files/output/" + filename + "Output.csv"

    with open(output_path, 'w', newline='') as fcsv:
        writer = csv.writer(fcsv, delimiter=',')
        writer.writerow(["unixdatetime", "value"])
        for row in data_list:
            writer.writerow([row[0], row[1]])
