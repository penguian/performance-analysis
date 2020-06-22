# parse_mom_sis_results

import numpy as np
import os
import pandas as pd
import sys
from scipy.stats import norm

hours_per_day = 24.0
minutes_per_hour = 60.0
seconds_per_minute = 60.0
seconds_per_hour = seconds_per_minute * minutes_per_hour
seconds_per_day = seconds_per_hour * hours_per_day


def parse_exp_seconds(log_file_name):
    month_days = [
        31, # Jan
        28, # Feb
        31, # Mar
        30, # Apr
        31, # May
        30, # Jun
        31, # Jul
        31, # Aug
        30, # Sep
        31, # Oct
        30, # Nov
        31] # Dec
    parsing_exp = True
    parsing_months = True
    parsing_days = True
    parsing_hours = True
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if parsing_exp and text_line.lstrip().startswith("&coupler_nml"):
                while parsing_exp:
                    text_line = next(log_file)
                    if text_line.lstrip().startswith("months"):
                        parsing_months = False
                        months_split = text_line.split('=')
                        months = int(months_split[1].split(',')[0])
                    if text_line.lstrip().startswith("days"):
                        parsing_days = False
                        days_split = text_line.split('=')
                        days = float(days_split[1].split(',')[0])
                    if text_line.lstrip().startswith("hours"):
                        parsing_hours = False
                        hours_split = text_line.split('=')
                        hours = float(hours_split[1].split(',')[0])
                    parsing_exp = (
                        parsing_months or 
                        parsing_days or 
                        parsing_hours)
    return float(
        (sum(month_days[:months]) + days) * seconds_per_day + 
        (hours / hours_per_day) * seconds_per_hour)


def parse_seconds_per_time_step(log_file_name):
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.lstrip().startswith("&ocean_model_nml"):
                while True:
                    text_line = next(log_file)
                    if text_line.lstrip().startswith("dt_ocean"):
                        seconds_split = text_line.split('=')
                        return float(seconds_split[1].split(',')[0])


def parse_layout(log_file_name):
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.lstrip().startswith("layout"):
                layout_split = text_line.split('=')
                layout = layout_split[1].split(',')
                rows = int(layout[0])
                cols = int(layout[1])
                return rows, cols


def parse_npes(log_file_name):
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.lstrip().startswith("MPP started"):
                return int(text_line.split('=')[1])


def parse_times(log_file_name):
    field_name_len = 36
    parsing_times = False
    times = dict()
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.startswith("Total runtime"):
                parsing_times = True
            if parsing_times:
                field_name = text_line[:field_name_len].strip()
                field_value = float(text_line[field_name_len:])
                times[field_name] = field_value
    return times


def derive_speeds(times, exp_seconds):
    speeds = dict()
    for field_name in times:
        time = times[field_name]
        speed_field_name = field_name + " speed"
        speeds[speed_field_name] = (
            0.0 
            if time == 0.0 else
            float(exp_seconds) / time)
    return speeds


def parse_ocean_log_file(log_file_name):
    result = dict()
    log_basename_split = os.path.basename(log_file_name).split('.')
    arch_prefix = log_basename_split[2]
    result["arch"] = (
        log_basename_split[3] 
        if arch_prefix == "noht" else
        arch_prefix)
    exp_seconds = parse_exp_seconds(log_file_name)
    result["exp_seconds"] = exp_seconds
    result["seconds_per_time_step"] = parse_seconds_per_time_step(log_file_name)
    rows, cols = parse_layout(log_file_name)
    result["rows"] = rows
    result["cols"] = cols
    result["ncpus"] = parse_npes(log_file_name)
    times = parse_times(log_file_name)
    result.update(times)
    speeds = derive_speeds(times, exp_seconds)
    result.update(speeds)
    result["Ocean speed per cpu"] = result["Ocean speed"] / result["ncpus"]
    return result


def parse_all(log_file_list):
    log_list = list()

    for log_file_name in log_file_list:
        log_list.append(parse_ocean_log_file(log_file_name))
    return pd.DataFrame(log_list)

