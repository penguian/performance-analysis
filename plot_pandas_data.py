# plot_pandas_data

import matplotlib.pyplot as plt


def plot_by_fn_by_group(plot_fn, x, y, by, data,
        xlabel=None, 
        ylabel=None,
        yticks=[],
        legend_title=None,
        marker='+'):
    dgb = data.groupby(by)
    xticks = data[x].sort_values().unique()
    xtick_labels = [str(int(val)) for val in xticks]
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
    plt.xticks(xticks, xtick_labels)
    if yticks != []:
        ytick_labels = [str(tick) for tick in yticks]
        plt.yticks(yticks, ytick_labels)
    ax.set_xticks([], minor=True)
    plt.xlabel(x if xlabel == None else xlabel)
    plt.ylabel(y if ylabel == None else ylabel)
    plt.legend(title=legend_title)


def loglog_by_group(x, y, by, data,
        xlabel=None, 
        ylabel=None,
        yticks=[],
        legend_title=None,
        marker='+'):
    return plot_by_fn_by_group(
        plt.loglog, x, y, by, data,
        xlabel=xlabel, 
        ylabel=ylabel,
        yticks=yticks,
        legend_title=legend_title,
        marker=marker)

def semilogx_by_group(x, y, by, data,
        xlabel=None, 
        ylabel=None,
        yticks=[],
        legend_title=None,
        marker='+'):
    return plot_by_fn_by_group(
        plt.semilogx, x, y, by, data,
        xlabel=xlabel, 
        ylabel=ylabel,
        yticks=yticks,
        legend_title=legend_title,
        marker=marker)


def plot_by_fn(plot_fn, x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+'):
    if len(xticks) > 0 or len(yticks) > 0:
            fig, ax = plt.subplots()
    if len(xticks) > 0:
        xtick_labels = [str(int(val)) for val in xticks]
    if len(yticks) > 0:
        ytick_labels = [str(int(val)) for val in yticks]
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
    if len(xticks) > 0:
        plt.xticks(xticks, xtick_labels)
        ax.set_xticks([], minor=True)
    if len(yticks) > 0:
        plt.yticks(yticks, ytick_labels)
        ax.set_yticks([], minor=True)
    plt.xlabel(x if xlabel == None else xlabel)
    plt.ylabel(y if ylabel == None else ylabel)
    return p


def loglog(x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+'):
    return plot_by_fn(
        plt.loglog, x, y, data,
        xlabel=xlabel, 
        ylabel=ylabel, 
        xticks=xticks, 
        yticks=yticks, 
        marker=marker)


def semilogx(x, y, data,
        xlabel=None, 
        ylabel=None,
        xticks=[],
        yticks=[],
        marker='+'):
    return plot_by_fn(
        plt.semilogx, x, y, data,
        xlabel=xlabel, 
        ylabel=ylabel, 
        xticks=xticks, 
        yticks=yticks, 
        marker=marker)


def plot_by_xy_labels_fn(plot_fn, x, data,
    xticks=[], 
    yticks=[]):
    if xticks == []:
        xticks = data[x].sort_values().unique()
    xtick_labels = [str(int(val)) for val in xticks]
    fig, ax = plt.subplots()
    p = plot_fn(data)
    plt.xticks(xticks, xtick_labels)
    ax.set_xticks([], minor=True)
    if yticks != []:
        ytick_labels = [str(val) for val in yticks]
        plt.yticks(yticks, ytick_labels)
        ax.set_yticks([], minor=True)
    return p
    
