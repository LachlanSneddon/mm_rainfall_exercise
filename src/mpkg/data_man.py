#!/usr/bin/env python
# Version: 1.0
# Created by: Lachlan Sneddon


def deaccum_data(accum_data):
    # de-accumulates data collected at an hour running total
    p_data = []
    for count, row in enumerate(accum_data):
        if count == 0:
            p_data = [(accum_data[0][0], accum_data[0][1])]
        else:
            if int(row[0]/3600) == int(accum_data[count-1][0]/3600):
                new_point = float(row[1]) - float(accum_data[count - 1][1])
                p_data += [(row[0], new_point)]
            else:
                p_data += [(row[0], row[1])]
    return p_data


def get_i_subsets(input_data):
    # returns list of all possible thirty minute subsets
    subsets = []
    for count, row in enumerate(input_data):
        t_subset = []
        itt = 0
        t_subset.append(count)

        if count + 1 < len(input_data):
            # if count is not last element
            while (count + itt + 1 < len(input_data)) & (input_data[count + itt + 1][0] - row[0] <= 1800):
                # while itt not at last element AND difference of itt and row is less than 1800
                if input_data[count + itt + 1][0] - row[0] <= 1800:
                    t_subset.append(count + itt + 1)
                if count + itt + 2 < len(input_data):
                    itt += 1
                else:
                    break
        subsets.append(t_subset)
    return subsets


def get_dp_totals(data, sets):
    # gets rain totals from a set of elements
    subset_totals = []

    for subset in sets:
        subset_sum = 0.0
        for index in subset:
            subset_sum += float(data[index][1])
        subset_totals.append(subset_sum)
    return subset_totals


def peak_thirty(input_data):
    # finds the peak 30 minute period in the data
    # returns the record time and values that make up the peak thirty minutes
    subsets = get_i_subsets(input_data)
    subset_totals = get_dp_totals(input_data, subsets)
    i_subset_max = subset_totals.index(max(subset_totals))

    peak_time_data = []

    for index in subsets[i_subset_max]:
        peak_time_data += [(input_data[index][0], input_data[index][1])]
    return peak_time_data
