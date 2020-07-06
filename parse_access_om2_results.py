# parse_access_om2_results

import glob
import os
import pandas as pd


def output_dirs(dir):
    output_glob_str = os.path.join(dir, os.path.join("*", "*output001"))
    return glob.glob(output_glob_str)


def parse_int_at_end(top_dir, filename, pattern):
    return_list = []
    dir_list = output_dirs(top_dir)
    for dir in dir_list:
        pathname = os.path.join(dir, filename)
        with open(pathname, 'r') as txt:
            for line in txt:
                if pattern in line:
                    return_list.append(int(line.split()[-1]))
                    break
    return return_list


def parse_float_at_index(top_dir, filename, pattern, index):
    return_list = []
    dir_list = output_dirs(top_dir)
    for dir in dir_list:
        pathname = os.path.join(dir, filename)
        with open(pathname, 'r') as txt:
            for line in txt:
                if pattern in line:
                    return_list.append(float(line.split()[index]))
                    break
    return return_list


ice_diag_filename = os.path.join("ice", "ice_diag.d")
ocean_log_filename = os.path.join("ocean", "logfile.000000.out")


def parse_ice_from_ocn(dir):
    return parse_float_at_index(
        dir,
        ice_diag_filename,
        "from_ocn",
        -2)


def parse_ice_nbr_blocks(dir):
    return parse_int_at_end(
        dir,
        ice_diag_filename,
        "number of blocks")


def parse_ice_ncpus(dir):
    return parse_int_at_end(
        dir,
        ice_diag_filename,
        "Processors")


def parse_ice_timeloop(dir):
    return parse_float_at_index(
        dir,
        ice_diag_filename,
        "TimeLoop",
        -2)


def parse_ocean_ncpus(dir):
    return parse_int_at_end(
        dir,
        ocean_log_filename,
        "NPES=")


def parse_ocean_oasis_recv(dir):
    return parse_float_at_index(
        dir,
        ocean_log_filename,
        "oasis_recv",
        -1)


def parse_ocean_time(dir):
    return parse_float_at_index(
        dir,
        ocean_log_filename,
        "Ocean",
        -1)


def parse_om2_nbr_time_steps(dir):
    return parse_int_at_end(
        dir,
        "access-om2.out",
        "number of time")


def parse_om2_ncpus(dir):
    return parse_int_at_end(
        dir,
        "config.yaml",
        "ncpus:")


def parse_om2_timestep(dir):
    return parse_int_at_end(
        dir,
        "accessom2.nml",
        "ocean_timestep")


def parse_om2_walltime(dir):
    return parse_float_at_index(
        dir,
        "job.yaml",
        "WALLTIME",
        -2)


def parse_om2_dataframe(dir):
    ice_from_ocn = parse_ice_from_ocn(dir)
    ice_nbr_blocks = parse_ice_nbr_blocks(dir)
    ice_ncpus = parse_ice_ncpus(dir)
    ice_timeloop = parse_ice_timeloop(dir)
    ocean_ncpus = parse_ocean_ncpus(dir)
    ocean_oasis_recv = parse_ocean_oasis_recv(dir)
    ocean_time = parse_ocean_time(dir)
    om2_nbr_time_steps = parse_om2_nbr_time_steps(dir)
    om2_ncpus = parse_om2_ncpus(dir)
    om2_timestep = parse_om2_timestep(dir)
    om2_walltime = parse_om2_walltime(dir)

    df = pd.DataFrame(
       list(zip(
            ice_from_ocn,
            ice_nbr_blocks,
            ice_ncpus,
            ice_timeloop,
            ocean_ncpus,
            ocean_oasis_recv,
            ocean_time,
            om2_nbr_time_steps,
            om2_ncpus,
            om2_timestep,
            om2_walltime)),
        columns = [
            "ice_from_ocn",
            "ice_nbr_blocks",
            "ice_ncpus",
            "ice_timeloop",
            "ocean_ncpus",
            "ocean_oasis_recv",
            "ocean_time",
            "om2_nbr_time_steps",
            "om2_ncpus",
            "om2_timestep",
            "om2_walltime"])

    df["ice_time_per_step"] = df["ice_timeloop"] / df["om2_nbr_time_steps"]
    df["ice_cpu_time_per_step"] = df["ice_time_per_step"] * df["ice_ncpus"]
    df["ice_om2_cpu_time_per_step"] = df["ice_time_per_step"] * df["om2_ncpus"]
    df["ocean_time_per_step"] = df["ocean_time"] / df["om2_nbr_time_steps"]
    df["ocean_cpu_time_per_step"] = df["ocean_time_per_step"] * df["ocean_ncpus"]
    df["ocean_om2_cpu_time_per_step"] = df["ocean_time_per_step"] * df["om2_ncpus"]

    df["om2_simulated_time"] = df["om2_nbr_time_steps"] * df["om2_timestep"]
    df["ice_speed"] = df["om2_simulated_time"] / df["ice_timeloop"]
    df["ocean_speed"] = df["om2_simulated_time"] / df["ocean_time"]
    df["om2_speed"] = df["om2_simulated_time"] / df["om2_walltime"]
    df["Ice speed per cpu"] = df["ice_speed"] / df["ice_ncpus"]
    df["Ocean speed per cpu"] = df["ocean_speed"] / df["ocean_ncpus"]
    df["OM2 speed per cpu"] = df["om2_speed"] / df["om2_ncpus"]

    df["relative ice_from_ocn"] = df["ice_from_ocn"] / df ["ice_timeloop"]
    df["relative ocean_oasis_recv"] = df["ocean_oasis_recv"] / df["ocean_time"]
    df["relative wait"] = (
            (df["ice_from_ocn"] + df["ocean_oasis_recv"]) / 
            (df ["ice_timeloop"] + df["ocean_time"]))
    df["wait relative to walltime"] = (df["ice_from_ocn"] + df["ocean_oasis_recv"]) / df["om2_walltime"] 

    return df

