# plot_right_axis_time

from convert_time import (
    days_to_gregorian_years, 
    gregorian_years_to_days,
    hours_to_seconds,
    seconds_to_hours)
import plot_pandas_data as ppd


def no_right_axis(ax,
        right_yticks=[],
        format_str=""):
    return None


def plot_right_axis_yd(ax, 
        right_yticks=[],
        format_str="{:g}"):
    return ppd.plot_right_axis(ax, 
        to_fn=days_to_gregorian_years, 
        inv_fn=gregorian_years_to_days,
        right_yticks=right_yticks, 
        format_str=format_str, 
        right_ylabel="Simulated years per day")


def plot_right_axis_sh(ax, 
        right_yticks=[],
        format_str="{:g}"):
    return ppd.plot_right_axis(ax, 
        to_fn=seconds_to_hours,
        inv_fn=hours_to_seconds,
        right_yticks=right_yticks, 
        format_str=format_str, 
        right_ylabel="Hours")

