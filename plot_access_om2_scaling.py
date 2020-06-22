# plot_access_om2_scaling

import plot_pandas_data as ppd
import matplotlib.pyplot as plt


def loglog_om2_speed_by_ncpus(df):
    p = ppd.loglog("om2_ncpus", "om2_speed", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="ACCESS-OM2 speed (d/d)",
        marker='+')
    return p


def semilogx_om2_speed_per_cpu_by_ncpus(df):
    p = ppd.semilogx("om2_ncpus", "OM2 speed per cpu", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="ACCESS-OM2 speed (d/d) per CPU",
        marker='+')
    return p


def loglog_ocean_speed_by_ncpus(df):
    p = ppd.loglog("ocean_ncpus", "ocean_speed", 
        data=df, 
        xlabel="MOM number of CPUs",
        ylabel="MOM speed (d/d)",
        marker='+')
    return p


def semilogx_ocean_speed_per_cpu_by_ncpus(df):
    p = ppd.semilogx("ocean_ncpus", "Ocean speed per cpu", 
        data=df, 
        xlabel="MOM number of CPUs",
        ylabel="MOM speed (d/d) per CPU",
        marker='+')
    return p


def loglog_ice_speed_by_ncpus(df):
    p = ppd.loglog("ice_ncpus", "ice_speed", 
        data=df, 
        xlabel="CICE number of CPUs",
        ylabel="CICE speed (d/d)",
        marker='+')
    return p


def semilogx_ice_speed_per_cpu_by_ncpus(df):
    p = ppd.semilogx("ice_ncpus", "Ice speed per cpu", 
        data=df, 
        xlabel="CICE number of CPUs",
        ylabel="CICE speed (d/d) per CPU",
        marker='+')
    return p


def loglog_ice_speed_by_ncpus_nbr_blocks(df):
    ppd.loglog_by_group("ice_nbr_blocks", "ice_speed", 
        by="om2_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ncpus")


def loglog_ice_speed_by_ocean_ncpus_nbr_blocks(df):
    ppd.loglog_by_group("ice_nbr_blocks", "ice_speed", 
        by="ocean_ncpus",
        data=df,
        xlabel="Number of CICE blocks",
        ylabel="CICE speed (d/d)",
        legend_title="Ocean ncpus")
    

def loglog_ice_timeloop_by_ncpus_nbr_blocks(df):
    ppd.loglog_by_group("ice_nbr_blocks", "ice_timeloop", 
        by="om2_ncpus",
        xlabel="Number of CICE blocks",
        ylabel="CICE TimeLoop",
        legend_title="Ncpus")
    

def loglog_ice_from_ocn_by_om2_ncpus(df):
    p = ppd.loglog("om2_ncpus", "ice_from_ocn", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE from_ocn",
        marker='+')
    return p


def semilogx_relative_ice_from_ocn_by_om2_ncpus(df):
    p = ppd.semilogx("om2_ncpus", "relative ice_from_ocn", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="CICE from_ocn / TimeLoop",
        marker='+')
    return p


def loglog_ocean_oasis_recv_by_om2_ncpus(df):
    p = ppd.loglog("om2_ncpus", "ocean_oasis_recv", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM oasis_recv",
        marker='+')
    return p


def semilogx_relative_ocean_oasis_recv_by_om2_ncpus(df):
    p = ppd.semilogx("om2_ncpus", "relative ocean_oasis_recv", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="MOM oasis_recv / Ocean time",
        marker='+')
    return p


def semilogx_relative_wait_by_om2_ncpus(df):
    p = ppd.semilogx("om2_ncpus", "relative wait", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="(from_ocn + oasis_recv) / (TimeLoop + Ocean)",
        marker='+')
    return p


def semilogx_walltime_wait_by_om2_ncpus(df):
    p = ppd.semilogx("om2_ncpus", "wait relative to walltime", 
        data=df, 
        xlabel="ACCESS-OM2 number of CPUs",
        ylabel="(from_ocn + oasis_recv) / Walltime",
        marker='+')
    return p

