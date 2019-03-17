#!/usr/bin/env python3
# Version: 1.0
# Created by: Lachlan Sneddon

from mpkg import csv_io
from mpkg import data_man
import os


def main():
    # takes in all files in input
    # de-accumulates hourly accumulations
    # finds the peak thirty minute rainfall
    # returns de-accumulated data to output folder
    # prints time(unix) and rainfall values for peak thirty minute data points

    path = os.getcwd().replace('\\', '/') + "/csv_files/input"
    file_list = os.listdir(path)

    for file in file_list:
        if file.endswith(".csv"):
            rain_data = csv_io.csv_input(path + "/" + file)
            deaccum_data = data_man.deaccum_data(rain_data)
            peak_thirty_data = data_man.peak_thirty(deaccum_data)
            csv_io.csv_output(deaccum_data, file)
            print("\n" + file + " de-accumulation successful")
            print("Output: " + os.getcwd().replace('\\', '/') + "/csv_files/output/" + file[:-4] + "Output.csv \n")

            peak_thirty_sum = 0.0
            for row in peak_thirty_data:
                peak_thirty_sum += float(row[1])

            print("The peak thirty minute data set is: ")
            print(peak_thirty_data)
            print("With a maximum rainfall of: " + str(peak_thirty_sum) + " inches")
        else:
            print(file + " is not a csv")


if __name__ == '__main__':
    main()
