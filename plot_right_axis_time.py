# plot_right_axis_years_days

from convert_time import days_to_gregorian_years, gregorian_years_to_days
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

