# plot_access_om2_scaling

import plot_pandas_data as ppd


def loglog_ice_speed_by_ncpus_nbr_blocks(df, **kwargs):
    p = ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="om2_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ncpus",
        **kwargs)
    return p


def loglog_ice_speed_by_ocean_ncpus_nbr_blocks(df, **kwargs):
    p = ppd.loglog_by_group("ice_nbr_blocks", "Ice TimeLoop speed",
        by="ocean_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ocean ncpus",
        **kwargs)
    return p


def loglog_om2_speed_by_ncpus(df, **kwargs):
    p = ppd.loglog("om2_ncpus", "OM2 speed",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 speed (d/d)",
        **kwargs)
    return p


def semilogx_om2_speed_per_cpu_by_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "OM2 speed per cpu",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 speed (d/d) per core",
        **kwargs)
    return p


def loglog_ocean_speed_by_ncpus(df, **kwargs):
    p = ppd.loglog("ocean_ncpus", "Ocean speed",
        data=df,
        xlabel="MOM number of cores",
        ylabel="MOM speed (d/d)",
        **kwargs) 
    return p


def semilogx_ocean_speed_per_cpu_by_ncpus(df, **kwargs):
    p = ppd.semilogx("ocean_ncpus", "Ocean speed per cpu",
        data=df,
        xlabel="MOM number of cores",
        ylabel="MOM speed (d/d) per core",
        **kwargs) 
    return p


def loglog_ice_speed_by_ncpus(df, **kwargs):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop speed",
        data=df,
        xlabel="CICE number of cores",
        ylabel="CICE speed (d/d)",
        **kwargs) 
    return p


def semilogx_ice_speed_per_cpu_by_ncpus(df, **kwargs):
    p = ppd.semilogx("ice_ncpus", "Ice speed per cpu",
        data=df,
        xlabel="CICE number of cores",
        ylabel="CICE speed (d/d) per core",
        **kwargs) 
    return p


def loglog_ice_from_ocn_by_om2_ncpus(df, **kwargs):
    p = ppd.loglog("om2_ncpus", "ice_from_ocn",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE from_ocn",
        **kwargs) 
    return p


def semilogx_relative_ice_from_ocn_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "relative ice_from_ocn",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE from_ocn / TimeLoop",
        **kwargs) 
    return p


def loglog_ocean_oasis_recv_by_om2_ncpus(df, **kwargs):
    p = ppd.loglog("om2_ncpus", "ocean_oasis_recv",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM oasis_recv",
        **kwargs) 
    return p


def semilogx_relative_ocean_oasis_recv_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "relative ocean_oasis_recv",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM oasis_recv / Ocean time",
        **kwargs) 
    return p


def semilogx_relative_wait_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "relative wait",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="(from_ocn + oasis_recv) / (TimeLoop + Ocean)",
        **kwargs) 
    return p


def semilogx_walltime_wait_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "wait relative to walltime",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="(from_ocn + oasis_recv) / Walltime",
        **kwargs) 
    return p


def loglog_ice_time_per_step_by_om2_ncpus(df, **kwargs):
    p = ppd.loglog("om2_ncpus", "Ice TimeLoop per step",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE time per step (s)",
        **kwargs) 
    return p


def semilogx_ice_cpu_time_per_step_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "ice_cpu_time per step",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE OM2 core time per step (core s)",
        **kwargs) 
    return p

def loglog_ocean_time_per_step_by_om2_ncpus(df, **kwargs):
    p = ppd.loglog("om2_ncpus", "Ocean per step",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM time per step (s)",
        **kwargs) 
    return p


def semilogx_ocean_cpu_time_per_step_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "ocean_cpu_time per step",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM OM2 core time per step (core s)",
        **kwargs) 
    return p


def loglog_ice_time_per_step_by_ncpus(df, **kwargs):
    p = ppd.loglog("ice_ncpus", "Ice TimeLoop per step",
        data=df,
        xlabel="CICE number of cores",
        ylabel="CICE time per step (s)",
        **kwargs) 
    return p


def semilogx_ice_cpu_time_per_step_by_ncpus(df, **kwargs):
    p = ppd.semilogx("ice_ncpus", "ice_cpu_time per step",
        data=df,
        xlabel="CICE number of cores",
        ylabel="CICE core time per step (core s)",
        **kwargs) 
    return p


def loglog_ocean_time_per_step_by_ncpus(df, **kwargs):
    p = ppd.loglog("ocean_ncpus", "Ocean per step",
        data=df,
        xlabel="MOM number of cores",
        ylabel="MOM time per step (s)",
        **kwargs) 
    return p


def semilogx_ocean_cpu_time_per_step_by_ncpus(df, **kwargs):
    p = ppd.semilogx("ocean_ncpus", "ocean_cpu_time per step",
        data=df,
        xlabel="MOM number of cores",
        ylabel="MOM core time per step (core s)",
        **kwargs) 
    return p


def semilogx_om2_init_time_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "Initialization",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="ACCESS-OM2 Initialization time (s)",
        **kwargs) 
    return p


def semilogx_ice_init_time_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "Ice initialization",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="CICE initialization time (s)",
        **kwargs) 
    return p


def semilogx_ocean_init_time_by_om2_ncpus(df, **kwargs):
    p = ppd.semilogx("om2_ncpus", "(Ocean initialization)",
        data=df,
        xlabel="ACCESS-OM2 number of cores",
        ylabel="MOM Initialization time (s)",
        **kwargs) 
    return p

