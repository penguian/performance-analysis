# parse_um_atmos_results

import glob
import os
import pandas as pd


def parse_omp_num_threads(log_file_name):
    threads_text = "I am running with"
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if threads_text in text_line:
                threads_split = text_line.split()
                return int(threads_split[-2])


def parse_nbr_time_steps(log_file_name):
    atm_step_text = "Atm_Step_4A (AS)"
    field_name_len = 20
    field_value_len = 5
    parsing_nbr_time_steps = False
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.startswith("END OF RUN"):
                parsing_nbr_time_steps = True
            if parsing_nbr_time_steps and atm_step_text in text_line:
                name_beg = text_line.find(' ') + 1
                value_beg = name_beg + field_name_len
                value_end = value_beg + field_value_len
                nbr_time_steps = int(text_line[value_beg:value_end].strip())
                return nbr_time_steps


def parse_seconds_per_time_step(log_file_name):
    timestep_text = "Model running with timestep"
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.startswith(timestep_text):
                seconds_len = 12
                seconds_beg = len(timestep_text)
                seconds_end = seconds_beg + seconds_len
                return float(text_line[seconds_beg:seconds_end])


def parse_atm_npes_layout(log_file_name):
    npes_layout_text = "processors in atmosphere configuration"
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if npes_layout_text in text_line:
                layout_text_beg = text_line.find(' ') + 1
                npes = int(text_line[:layout_text_beg].strip())
                layout_beg = layout_text_beg + len(npes_layout_text)
                layout = text_line[layout_beg:].split('x')
                atm_rows = int(layout[0].strip())
                atm_cols = int(layout[1].strip())
                return npes, atm_rows, atm_cols


def parse_times(log_file_name):
    field_name_len = 20
    field_value_len = 14
    parsing_times = False
    times = dict()
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.startswith("MPP : Inclusive timer"):
                for skip in range(4):
                    text_line = next(log_file)
                parsing_times = True
            if parsing_times:
                space_index = text_line.find(' ')
                if space_index <= 0:
                    return times
                name_beg = space_index + 1
                name_end = name_beg + field_name_len
                value_beg = name_end
                value_end = value_beg + field_value_len
                field_name = text_line[name_beg:name_end].strip()
                field_value = float(text_line[value_beg:value_end].strip())
                times[field_name] = field_value
    return times


def parse_atm_npes_layout(log_file_name):
    npes_layout_text = "processors in atmosphere configuration"
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if npes_layout_text in text_line:
                layout_text_beg = text_line.find(' ') + 1
                npes = int(text_line[:layout_text_beg].strip())
                layout_beg = layout_text_beg + len(npes_layout_text)
                layout = text_line[layout_beg:].split('x')
                atm_rows = int(layout[0].strip())
                atm_cols = int(layout[1].strip())
                return npes, atm_rows, atm_cols


def parse_ocn_npes_layout(log_file_name):
    layout_text = "mom_domain domain decomposition:"
    with open(log_file_name, "r") as log_file:
        for text_line in log_file:
            if text_line.startswith(layout_text):
                layout_split = text_line.split()
                ocn_rows = int(layout_split[-3].strip())
                ocn_cols = int(layout_split[-1].strip())
                ocn_npes = ocn_rows * ocn_cols
                return ocn_npes, ocn_rows, ocn_cols


def parse_bytes_at_end(text_line):
    words = text_line.strip().split()
    return words[-1]


def parse_float_at_end(text_line):
    words = text_line.strip().split()
    return float(words[-1])


def parse_int_at_end(text_line):
    words = text_line.strip().split()
    return int(words[-1])


def parse_time_hms_at_end(text_line):
    words = text_line.strip().split()
    hms = words[-1].split(':')
    h = int(hms[0])
    m = int(hms[1])
    s = float(hms[2])
    return h * 3600.0 + m * 60.0 + s


def parse_cm2_job_output(output_file_name):
    stats = dict()
    times = dict()
    resource_usage_text = "Resource Usage on"
    parsing_usage = False
    with open(output_file_name, "r") as output_file:
        for text_line in output_file:
            if resource_usage_text in text_line:
                for skip in range(4):
                    text_line = next(output_file)
                parsing_usage = True
            if parsing_usage:
                stats["service_units"] = parse_float_at_end(text_line)
                text_line = next(output_file)
                stats["ncpus"] = parse_int_at_end(text_line)
                text_line = next(output_file)
                times["cpu_seconds"] = parse_time_hms_at_end(text_line)
                text_line = next(output_file)
                stats["memory"] = parse_bytes_at_end(text_line)
                text_line = next(output_file)
                times["walltime"] = parse_time_hms_at_end(text_line)
                text_line = next(output_file)
                stats["jobfs"] = parse_bytes_at_end(text_line)
                return stats, times


def parse_atm_log_file(log_file_name):
    logged = dict()
    omp_num_threads = parse_omp_num_threads(log_file_name)
    logged["omp_num_threads"] = omp_num_threads
    nbr_time_steps = parse_nbr_time_steps(log_file_name)
    logged["nbr_time_steps"] = nbr_time_steps
    seconds_per_time_step = parse_seconds_per_time_step(log_file_name)
    logged["seconds_per_time_step"] = seconds_per_time_step
    exp_seconds = nbr_time_steps * seconds_per_time_step
    logged["exp_seconds"] = exp_seconds
    npes, atm_rows, atm_cols = parse_atm_npes_layout(log_file_name)
    logged["npes"] = npes
    logged["atm_rows"] = atm_rows
    logged["atm_cols"] = atm_cols
    times = parse_times(log_file_name)
    return logged, times


def parse_ocn_log_file(log_file_name):
    logged = dict()
    ocn_npes, ocn_rows, ocn_cols = parse_ocn_npes_layout(log_file_name)
    logged["ocn_npes"] = ocn_npes
    logged["ocn_rows"] = ocn_rows
    logged["ocn_cols"] = ocn_cols
    return logged


def derive_proc_times(times, nproc_dict, nproc_name):
    result = dict()
    for field_name in times:
        time = times[field_name]
        result_field_name = field_name + " * " + nproc_name
        result[result_field_name] = time * nproc_dict[nproc_name]
    return result


def derive_times_per_time_step(times, nbr_time_steps):
    result = dict()
    for field_name in times:
        time = times[field_name]
        result_field_name = field_name + " per time step"
        result[result_field_name] = time / nbr_time_steps
    return result


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


def parse_cm2_work_dir(work_dir_name):
    output_file_glob = os.path.join(
        work_dir_name,
        "runmodel*.o[0-9]*")
    output_file_name = glob.glob(output_file_glob)[0]
    output_stats, output_times = parse_cm2_job_output(output_file_name)
    
    atm_log_file_glob = os.path.join(
        work_dir_name, 
        "ATM_RUNDIR",
        "pe_output",
        "atmos.fort6.pe*000")
    atm_log_file_name = glob.glob(atm_log_file_glob)[0]
    atm_log, atm_times = parse_atm_log_file(atm_log_file_name)
    nbr_time_steps = atm_log["nbr_time_steps"]
    
    ocn_log_file_name = os.path.join(
        work_dir_name, 
        "OCN_RUNDIR",
        "logfile.000000.out")
    ocn_log = parse_ocn_log_file(ocn_log_file_name)

    logged_times = {
        **output_times,
        **atm_times}
    cpu_times = derive_proc_times(logged_times, output_stats, "ncpus")
    pe_times =  derive_proc_times(logged_times, atm_log, "npes")
    
    all_times = {
        **logged_times,
        **cpu_times,
        **pe_times}
    all_times_per_time_step = derive_times_per_time_step(
        all_times, 
        nbr_time_steps)
    
    exp_seconds = atm_log["exp_seconds"]
    speeds = derive_speeds(all_times, exp_seconds)

    result = {
        **output_stats,
        **atm_log,
        **ocn_log,
        **logged_times,
        **all_times,
        **all_times_per_time_step,
        **speeds}
    return result


def parse_all(work_dir_list):
    result_list = list()

    for work_dir_name in work_dir_list:
        result_list.append(parse_cm2_work_dir(work_dir_name))
    return pd.DataFrame(result_list)

