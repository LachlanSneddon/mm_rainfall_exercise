#!/usr/bin/env python3
# Version: 1.0
# Created by: Lachlan Sneddon

import math
import random
import time


def generate_rain_data():
    # generates hour accumulated rain data
    last_time = 1542585600
    running_total = round(random.uniform(0, 1.29), 2)
    generated_data = [(last_time, running_total)]

    for itt in range(0, 99):
        new_time = last_time + random.randint(600, 1800)
        new_reading = round(random.uniform(0, 1.29), 2)
        if new_time <= time.time():
            # ensures new rows are historical
            if math.trunc(new_time/3600) == math.trunc(last_time/3600):
                running_total += new_reading
            else:
                running_total = new_reading
            generated_data += [(new_time, running_total)]
            last_time = new_time
        else:
            print("new rows have exceeded current time")
            break

    return generated_data
