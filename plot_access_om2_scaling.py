# plot_access_om2_scaling

import plot_pandas_data as ppd
import plot_right_axis_time as pra
import matplotlib.pyplot as plt


def plot_by_xy_labels_fn(plot_fn, x, data,
        xticks=[],
        yticks=[],
        right_yticks=[],
        format_str="{:g}",
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    return ppd.plot_by_xy_labels_fn(plot_fn, x, data,
        xticks=xticks,
        yticks=yticks,
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_ice_speed_by_ncpus_nbr_blocks(df,
        right_yticks=[],
        format_str="{:g}",
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="om2_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ncpus",
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_ice_speed_by_ocean_ncpus_nbr_blocks(df,
        right_yticks=[],
        format_str="{:g}",
        right_axis_fn=pra.plot_right_axis_yd,
        marker='+'):
    ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="ocean_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ocean ncpus",
        right_yticks=right_yticks,
        format_str=format_str,
        right_axis_fn=right_axis_fn,
        marker=marker)


def loglog_om2_speed_by_ncpus(df,
        marker='+'):
    p = ppd.loglog("om2_ncpus", "OM2 speed",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="ACCESS-OM2 speed (d/d)",
        marker=marker)
    return p


def semilogx_om2_speed_per_cpu_by_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "OM2 speed per cpu",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="ACCESS-OM2 speed (d/d) per CPU",
        marker=marker)
    return p


def loglog_ocean_speed_by_ncpus(df,
        marker='+'):
    p = ppd.loglog("ocean_ncpus", "Ocean speed",
        data=df,
        xlabel="MOM number of CPUs",
        ylabel="MOM speed (d/d)",
        marker=marker)
    return p


def semilogx_ocean_speed_per_cpu_by_ncpus(df,
        marker='+'):
    p = ppd.semilogx("ocean_ncpus", "Ocean speed per cpu",
        data=df,
        xlabel="MOM number of CPUs",
        ylabel="MOM speed (d/d) per CPU",
        marker=marker)
    return p


def loglog_ice_speed_by_ncpus(df,
        marker='+'):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop speed",
        data=df,
        xlabel="CICE number of CPUs",
        ylabel="CICE speed (d/d)",
        marker=marker)
    return p


def semilogx_ice_speed_per_cpu_by_ncpus(df,
        marker='+'):
    p = ppd.semilogx("ice_ncpus", "Ice speed per cpu",
        data=df,
        xlabel="CICE number of CPUs",
        ylabel="CICE speed (d/d) per CPU",
        marker=marker)
    return p


def loglog_ice_from_ocn_by_om2_ncpus(df,
        marker='+'):
    p = ppd.loglog("om2_ncpus", "ice_from_ocn",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE from_ocn",
        marker=marker)
    return p


def semilogx_relative_ice_from_ocn_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "relative ice_from_ocn",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE from_ocn / TimeLoop",
        marker=marker)
    return p


def loglog_ocean_oasis_recv_by_om2_ncpus(df,
        marker='+'):
    p = ppd.loglog("om2_ncpus", "ocean_oasis_recv",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM oasis_recv",
        marker=marker)
    return p


def semilogx_relative_ocean_oasis_recv_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "relative ocean_oasis_recv",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM oasis_recv / Ocean time",
        marker=marker)
    return p


def semilogx_relative_wait_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "relative wait",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="(from_ocn + oasis_recv) / (TimeLoop + Ocean)",
        marker=marker)
    return p


def semilogx_walltime_wait_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "wait relative to walltime",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="(from_ocn + oasis_recv) / Walltime",
        marker=marker)
    return p


def loglog_ice_time_per_step_by_om2_ncpus(df,
        marker='+'):
    p = ppd.loglog("om2_ncpus", "Ice TimeLoop per step",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE time per step (s)",
        marker=marker)
    return p


def semilogx_ice_cpu_time_per_step_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "ice_cpu_time per step",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE OM2 CPU time per step (CPU s)",
        marker=marker)
    return p

def loglog_ocean_time_per_step_by_om2_ncpus(df,
        marker='+'):
    p = ppd.loglog("om2_ncpus", "Ocean per step",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM time per step (s)",
        marker=marker)
    return p


def semilogx_ocean_cpu_time_per_step_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "ocean_cpu_time per step",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM OM2 CPU time per step (CPU s)",
        marker=marker)
    return p


def loglog_ice_time_per_step_by_ncpus(df,
        marker='+'):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop per step",
        data=df,
        xlabel="CICE number of CPUs",
        ylabel="CICE time per step (s)",
        marker=marker)
    return p


def semilogx_ice_cpu_time_per_step_by_ncpus(df,
        marker='+'):
    p = ppd.semilogx("ice_ncpus", "ice_cpu_time per step",
        data=df,
        xlabel="CICE number of CPUs",
        ylabel="CICE CPU time per step (CPU s)",
        marker=marker)
    return p


def loglog_ocean_time_per_step_by_ncpus(df,
        marker='+'):
    p = ppd.loglog("ocean_ncpus", "Ocean per step",
        data=df,
        xlabel="MOM number of CPUs",
        ylabel="MOM time per step (s)",
        marker=marker)
    return p


def semilogx_ocean_cpu_time_per_step_by_ncpus(df,
        marker='+'):
    p = ppd.semilogx("ocean_ncpus", "ocean_cpu_time per step",
        data=df,
        xlabel="MOM number of CPUs",
        ylabel="MOM CPU time per step (CPU s)",
        marker=marker)
    return p


def semilogx_om2_init_time_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "Initialization",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="ACCESS-OM2 Initialization time (s)",
        marker=marker)
    return p


def semilogx_ice_init_time_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "Ice initialization",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE initialization time (s)",
        marker=marker)
    return p


def semilogx_ocean_init_time_by_om2_ncpus(df,
        marker='+'):
    p = ppd.semilogx("om2_ncpus", "(Ocean initialization)",
        data=df,
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM Initialization time (s)",
        marker=marker)
    return p

