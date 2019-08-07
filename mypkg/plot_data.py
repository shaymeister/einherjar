#!/usr/bin/env python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from math import e


def plotData(
        transformed_data,
        ftype_plots,
        verbose):
    """Plot query data using matplotlib"""
    # making functions more explicit
    transformed_data, ftype_plots, verbose = \
        transformed_data, ftype_plots, verbose
    if verbose >= 1:
        print("Plotting Data")
    mpl.use('Agg')  # Force matplotlib to not use any Xwindows backend
    data = transformed_data
    data = data.sort_values(by=['total_duration'], ascending=False)
    plot_data = data['total_duration'].dropna().astype(float)
    fig, ax = plt.subplots()
    plt.rc('xtick', labelsize=5)
    plt.rc('ytick', labelsize=5)
    plt.rc('figure', titlesize=8)
    
    if verbose >= 2:
        print("Mean, Std, and Normpdf are being calculated")

    # calculating required variables
    datamean = np.mean(plot_data)
    datastd = np.std(plot_data)
    pdf = stats.norm.pdf(plot_data, datamean, datastd) 
    longest = plot_data[0:1].values

    if verbose >= 2:
        print("Mean, Std, and Normpdf have been calculated")

    # giving our plot a title
    plt.suptitle("Distribution of Latency Across Different Queries\n"+\
                "The 99.99% of the distribution is " + str(longest) + "ms",\
                size = 8) 

# Plot 1 -> line graph w/ default x-scale
    if verbose >= 2:
        print("Plot 1 is being created")
    plt.subplot(221).set_title('time(ms)/pdf')
    plt.plot(pdf, plot_data)
    if verbose >= 2:
        print("Plot 1 has been created")

# Plot 2 -> hist w/ default x-scale
    if verbose >= 2:
        print("Plot 2 is being created")
    plt.subplot(222).set_title('pdf/time(ms)') # places the plot in quadrant I
    plt.hist(plot_data, 20, density=True)
    plt.plot(plot_data, pdf)
    if verbose >= 2:
        print("Plot 2 has been created")

# Plot 3 -> line graph w/ log base 2 x-scale
    if verbose >= 2:
        print("Plot 3 is being created")
    plt.subplot(223).set_title("time(ms)/pdf x=log2")  # places the plot in quadrant III
    plt.semilogx(pdf, plot_data, basex=2)
    if verbose >= 2:
        print("Plot 3 has been created")

# Plot 4 -> line graph w/ Log base e x-scale
    if verbose >= 2:
        print("Plot 4 is being created")
    plt.subplot(224).set_title("time(ms)/pdf x=log10")  # places the plot in quadrant IV
    plt.semilogx(pdf, plot_data, basex = 10)
    if verbose >= 2:
        print("Plot 4 has been created")

    plt.subplots_adjust(hspace=0.3, wspace=0.3)
    plt_name = 'queries.' + ftype_plots
    plt.savefig(plt_name)
    if verbose >= 1:
        print("Data has been plotted")
