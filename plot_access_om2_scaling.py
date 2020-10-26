# plot_access_om2_scaling

import plot_pandas_data as ppd
import plot_right_axis_time as pra
import matplotlib.pyplot as plt

default_format = ppd.default_format


def plot_by_xy_labels_fn(plot_fn, x, data,
        ax=None,
        xticks=[],
        yticks=[],
        right_yticks=[],
        format_str=default_format,
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    return ppd.plot_by_xy_labels_fn(plot_fn, x, data,
        ax=ax,
        xticks=xticks,
        yticks=yticks,
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_ice_speed_by_ncpus_nbr_blocks(df,
        ax=None,
        right_yticks=[],
        format_str=default_format,
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    if ax is None:
        fig, ax = plt.subplots()
    ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="om2_ncpus",
        data=df,
        ax=ax,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ncpus",
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_ice_speed_by_ocean_ncpus_nbr_blocks(df,
        ax=None,
        right_yticks=[],
        format_str=default_format,
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    if ax is None:
        fig, ax = plt.subplots()
    ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="ocean_ncpus",
        data=df,
        ax=ax,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ocean ncpus",
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_om2_speed_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("om2_ncpus", "OM2 speed",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 speed (d/d)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_om2_speed_per_cpu_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "OM2 speed per cpu",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 speed (d/d) per core",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ocean_speed_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("ocean_ncpus", "Ocean speed",
        data=df,
        ax=ax,
        xlabel="MOM number of cores",
        ylabel="MOM speed (d/d)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ocean_speed_per_cpu_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("ocean_ncpus", "Ocean speed per cpu",
        data=df,
        ax=ax,
        xlabel="MOM number of cores",
        ylabel="MOM speed (d/d) per core",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ice_speed_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop speed",
        data=df,
        ax=ax,
        xlabel="CICE number of cores",
        ylabel="CICE speed (d/d)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ice_speed_per_cpu_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("ice_ncpus", "Ice speed per cpu",
        data=df,
        ax=ax,
        xlabel="CICE number of cores",
        ylabel="CICE speed (d/d) per core",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ice_from_ocn_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("om2_ncpus", "ice_from_ocn",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE from_ocn",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_relative_ice_from_ocn_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "relative ice_from_ocn",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE from_ocn / TimeLoop",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ocean_oasis_recv_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("om2_ncpus", "ocean_oasis_recv",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM oasis_recv",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_relative_ocean_oasis_recv_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "relative ocean_oasis_recv",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM oasis_recv / Ocean time",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_relative_wait_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "relative wait",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="(from_ocn + oasis_recv) / (TimeLoop + Ocean)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_walltime_wait_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "wait relative to walltime",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="(from_ocn + oasis_recv) / Walltime",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ice_time_per_step_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("om2_ncpus", "Ice TimeLoop per step",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE time per step (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ice_cpu_time_per_step_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "ice_cpu_time per step",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE OM2 core time per step (core s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p

def loglog_ocean_time_per_step_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("om2_ncpus", "Ocean per step",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM time per step (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ocean_cpu_time_per_step_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "ocean_cpu_time per step",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM OM2 core time per step (core s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ice_time_per_step_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop per step",
        data=df,
        ax=ax,
        xlabel="CICE number of cores",
        ylabel="CICE time per step (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ice_cpu_time_per_step_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("ice_ncpus", "ice_cpu_time per step",
        data=df,
        ax=ax,
        xlabel="CICE number of cores",
        ylabel="CICE core time per step (core s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def loglog_ocean_time_per_step_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.loglog("ocean_ncpus", "Ocean per step",
        data=df,
        ax=ax,
        xlabel="MOM number of cores",
        ylabel="MOM time per step (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ocean_cpu_time_per_step_by_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("ocean_ncpus", "ocean_cpu_time per step",
        data=df,
        ax=ax,
        xlabel="MOM number of cores",
        ylabel="MOM core time per step (core s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_om2_init_time_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "Initialization",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 Initialization time (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ice_init_time_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "Ice initialization",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE initialization time (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p


def semilogx_ocean_init_time_by_om2_ncpus(df,
        ax=None,
        xticks=[],
        yticks=[],
        right_axis_fn=ppd.no_right_axis,
        right_yticks=[],
        marker='+',
        format_str=default_format):
    p = ppd.semilogx("om2_ncpus", "(Ocean initialization)",
        data=df,
        ax=ax,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM Initialization time (s)",
        xticks=xticks, 
        yticks=yticks, 
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        marker=marker,
        format_str=format_str)
    return p

