# plot_pandas_data

import matplotlib.pyplot as plt

default_format = "{:g}"


def no_right_axis(ax, right_yticks, format_str):
    return None


def plot_right_axis(ax, to_fn, inv_fn,
        right_yticks=[],
        format_str=default_format, 
        right_ylabel=""):
    right_axis = ax.secondary_yaxis(
        'right', 
        functions=(to_fn, inv_fn),
        ylabel=right_ylabel)
    if right_yticks == []:
        yticks = ax.get_yticks()
        right_yticks = [
            to_fn(tick) for tick in yticks]
    right_ytick_labels = [
        format_str.format(tick) for tick in right_yticks]
    right_axis.set_yticks([], minor=True)
    right_axis.set_yticks(right_yticks, minor=False)
    right_axis.set_yticklabels(right_ytick_labels)
    return right_axis


def plot_by_fn_by_group(plot_fn, x, y, by, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        legend_title=None,
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    dgb = data.groupby(by)
    fig, ax = plt.subplots()
    for name, group in dgb:
        means = group.groupby(x)[y].mean()
        p = plot_fn(means, marker='')
        color = p[0].get_color()
        plot_fn(x, y, 
            data=group, 
            marker=marker,
            linestyle='',
            color=color,
            label=str(name))
    if plot_fn == plt.semilogx:
        plt.ylim([0, data[y].max() * 1.1])
    if xticks == []:
        xticks = data[x].sort_values().unique()
    xtick_labels = [
        str(int(tick)) for tick in xticks]
    plt.xticks(xticks, xtick_labels, rotation=90)
    ax.set_xticks([], minor=True)
    if yticks != []:
        ytick_labels = [
            default_format.format(tick) for tick in yticks]
        plt.yticks(yticks, ytick_labels)
    right_axis = right_axis_fn(ax,
        right_yticks=right_yticks,
        format_str=format_str)
    plt.xlabel(x if xlabel == None else xlabel)
    plt.ylabel(y if ylabel == None else ylabel)
    plt.legend(title=legend_title)


def loglog_by_group(x, y, by, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        legend_title=None,
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    return plot_by_fn_by_group(
        plt.loglog, x, y, by, data,
        xlabel=xlabel, 
        ylabel=ylabel,
        xticks=xticks,
        yticks=yticks,
        legend_title=legend_title,
        marker=marker,
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        format_str=format_str)


def semilogx_by_group(x, y, by, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        legend_title=None,
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    return plot_by_fn_by_group(
        plt.semilogx, x, y, by, data,
        xlabel=xlabel, 
        ylabel=ylabel,
        xticks=xticks,
        yticks=yticks,
        legend_title=legend_title,
        marker=marker,
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        format_str=format_str)


def plot_by_fn(plot_fn, x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    if (xticks != [] or 
        yticks != [] or 
        right_axis_fn != no_right_axis):
        fig, ax = plt.subplots()
    means = data.groupby(x)[y].mean()
    p = plot_fn(means, marker='')
    color = p[0].get_color()
    if plot_fn == plt.semilogx:
        plt.ylim([0, data[y].max() * 1.1])
    plot_fn(x, y, 
        data=data, 
        marker=marker, 
        linestyle='', 
        color=color)
    if xticks != []:
        xtick_labels = [
            str(int(tick)) for tick in xticks]
        plt.xticks(xticks, xtick_labels)
        ax.set_xticks([], minor=True)
    if yticks != []:
        ytick_labels = [
            default_format.format(tick) for tick in yticks]
        plt.yticks(yticks, ytick_labels)
        ax.set_yticks([], minor=True)
    if right_axis_fn != no_right_axis:
        right_axis = right_axis_fn(ax,
            right_yticks=right_yticks,
            format_str=format_str)
    plt.xlabel(x if xlabel == None else xlabel)
    plt.ylabel(y if ylabel == None else ylabel)
    return p


def plot_by_xy_labels_fn(plot_fn, x, data,
        xticks=[], 
        yticks=[],
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format,
        marker='+'):
    if xticks == []:
        xticks = data[x].sort_values().unique()
    xtick_labels = [
        str(int(tick)) for tick in xticks]
    fig, ax = plt.subplots()
    p = plot_fn(
        data, 
        marker=marker)
    plt.xticks(xticks, xtick_labels)
    ax.set_xticks([], minor=True)
    if yticks != []:
        ytick_labels = [
            default_format.format(tick) for tick in yticks]
        plt.yticks(yticks, ytick_labels)
        ax.set_yticks([], minor=True)
    right_axis = right_axis_fn(ax,
            right_yticks=right_yticks,
            format_str=format_str)
    return p
    

def loglog(x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    return plot_by_fn(
        plt.loglog, x, y, data,
        xlabel=xlabel, 
        ylabel=ylabel, 
        xticks=xticks, 
        yticks=yticks, 
        marker=marker,
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        format_str=format_str)


def semilogx(x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+',
        right_axis_fn=no_right_axis,
        right_yticks=[],
        format_str=default_format):
    return plot_by_fn(
        plt.semilogx, x, y, data,
        xlabel=xlabel, 
        ylabel=ylabel, 
        xticks=xticks, 
        yticks=yticks, 
        marker=marker,
        right_axis_fn=right_axis_fn,
        right_yticks=right_yticks,
        format_str=format_str)

