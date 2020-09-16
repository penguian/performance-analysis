# parse_access_om2_results

import glob
import os
import pandas as pd


def output_dirs(dir):
    output_glob_str = os.path.join(dir, os.path.join("*", "*output001"))
    return glob.glob(output_glob_str)


ice_diag_filename = os.path.join("ice", "ice_diag.d")
ocean_log_filename = os.path.join("ocean", "logfile.000000.out")
access_om2_filename = "access-om2.out"


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


def parse_times_at_index(filename, index):
    field_name_len = 34
    parsing_times = False
    times = dict()
    with open(filename, "r") as txt:
        for line in txt:
            if line.startswith("Total runtime"):
                parsing_times = True
            if parsing_times:
                if line.startswith(" MPP_STACK"):
                    break
                field_name = line[:field_name_len].strip()
                field_value = float(line.split()[index])
                times[field_name] = field_value
    return times


def parse_all_times_at_index(top_dir, filename, index):
    return_list = []
    dir_list = output_dirs(top_dir)
    for dir in dir_list:
        pathname = os.path.join(dir, filename)
        times = parse_times_at_index(pathname, index)
        return_list.append(times)
    return return_list


def parse_ice_times_at_line(filename, line_offset):
    field_name_beg = 10
    field_name_end = 23
    parsing_times = False
    times = dict()
    with open(filename, "r") as txt:
        for line in txt:
            if line.startswith("Timing information:"):
                parsing_times = True
            if parsing_times:
                if line.startswith("Timer"):
                    field_name = "Ice " + line[field_name_beg:field_name_end].strip()
                    for skip in range(line_offset):
                        line = next(txt)
                    field_value = float(line.split()[-2])
                    times[field_name] = field_value
    return times


def parse_all_ice_times_at_line(top_dir, filename, line_offset):
    return_list = []
    dir_list = output_dirs(top_dir)
    for dir in dir_list:
        pathname = os.path.join(dir, filename)
        times = parse_ice_times_at_line(pathname, line_offset)
        return_list.append(times)
    return return_list


def parse_all_mean_ice_times(dir):
    return  parse_all_ice_times_at_line(
        dir,
        ice_diag_filename,
        3)


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


def parse_ocean_ncpus(dir):
    return parse_int_at_end(
        dir,
        ocean_log_filename,
        "NPES=")


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
        "ice_ocean_timestep")


def parse_om2_walltime(dir):
    return parse_float_at_index(
        dir,
        "job.yaml",
        "WALLTIME",
        -2)


def parse_om2_times(dir):
    return parse_all_times_at_index(
        dir,
        "access-om2.out",
        -6)


def derive_per_step(times, nbr_time_steps):
    per_step = dict()
    for field_name in times:
        time = times[field_name]
        per_step_field_name = field_name + " per step"
        per_step[per_step_field_name] = time / nbr_time_steps
    return per_step


def derive_speed(times, simulated_time):
    speed = dict()
    for field_name in times:
        time = times[field_name]
        speed_field_name = field_name + " speed"
        speed[speed_field_name] = (
            0.0
            if time == 0.0 else
            float(simulated_time) / time)
    return speed


def parse_om2_dataframe(dir):
    om2_ncpus = parse_om2_ncpus(dir)
    om2_nbr_time_steps = parse_om2_nbr_time_steps(dir)
    om2_timestep = parse_om2_timestep(dir)
    om2_walltime = parse_om2_walltime(dir)
    om2_simulated_time = list(
        map(lambda x,y: x*y, om2_nbr_time_steps, om2_timestep))
    om2_times = parse_om2_times(dir)
    om2_per_step = map(derive_per_step, om2_times, om2_nbr_time_steps)
    om2_speed = map(derive_speed, om2_times, om2_simulated_time)
    ice_from_ocn = parse_ice_from_ocn(dir)
    ice_nbr_blocks = parse_ice_nbr_blocks(dir)
    ice_ncpus = parse_ice_ncpus(dir)
    ice_mean_times = parse_all_mean_ice_times(dir)
    ice_per_step = map(derive_per_step, ice_mean_times, om2_nbr_time_steps)
    ice_speed = map(derive_speed, ice_mean_times, om2_simulated_time)
    ocean_ncpus = parse_ocean_ncpus(dir)


    df = pd.DataFrame(
       list(zip(
            ice_from_ocn,
            ice_nbr_blocks,
            ice_ncpus,
            ocean_ncpus,
            om2_ncpus,
            om2_nbr_time_steps,
            om2_timestep,
            om2_walltime,
            om2_simulated_time)),
        columns = [
            "ice_from_ocn",
            "ice_nbr_blocks",
            "ice_ncpus",
            "ocean_ncpus",
            "om2_ncpus",
            "om2_nbr_time_steps",
            "om2_timestep",
            "om2_walltime",
            "om2_simulated_time"])

    df = pd.concat([
            df,
            pd.DataFrame(om2_times),
            pd.DataFrame(om2_per_step),
            pd.DataFrame(om2_speed),
            pd.DataFrame(ice_mean_times),
            pd.DataFrame(ice_per_step),
            pd.DataFrame(ice_speed)],
            axis=1)

    df["Ice initialization"] = df["Ice Total"] - df["Ice TimeLoop"]

    df["ice_cpu_time per step"] = df["Ice TimeLoop per step"] * df["ice_ncpus"]
    df["ice_om2_cpu_time per step"] = df["Ice TimeLoop per step"] * df["om2_ncpus"]
    df["ocean_cpu_time per step"] = df["Ocean per step"] * df["ocean_ncpus"]
    df["ocean_om2_cpu_time per step"] = df["Ocean per step"] * df["om2_ncpus"]

    df["Ice speed per cpu"] = df["Ice TimeLoop speed"] / df["ice_ncpus"]
    df["Ocean speed per cpu"] = df["Ocean speed"] / df["ocean_ncpus"]
    df["OM2 speed"] = df["om2_simulated_time"] / df["om2_walltime"]
    df["OM2 speed per cpu"] = df["OM2 speed"] / df["om2_ncpus"]

    df["relative ice_from_ocn"] = df["ice_from_ocn"] / df ["Ice TimeLoop"]
    df["relative ocean_oasis_recv"] = df["oasis_recv"] / df["Ocean"]
    df["relative wait"] = (
            (df["ice_from_ocn"] + df["oasis_recv"]) /
            (df ["Ice TimeLoop"] + df["Ocean"]))
    df["wait relative to walltime"] = (df["ice_from_ocn"] + df["oasis_recv"]) / df["om2_walltime"]

    return df

