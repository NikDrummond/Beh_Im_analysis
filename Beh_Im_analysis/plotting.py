# fucntions for plotting

# Import libraries
import ast
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd
import glob, os
import re
import math
from tqdm import tqdm
from scipy.stats import stats
from scipy.stats import mannwhitneyu
import itertools
import seaborn as sns


# Plotting - single sample for whole time
# To make the plot in the notebook and not in an extra window
# %matplotlib notebook
def layout_plot(plot, tick_spacing=2, fov=(1000, 1400, -0.05, 0.3), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)


# PLOTTING THE ALIGNED EVENT, INDEPENDENT OF TRANSITION EVENT
# Plotting for multi-events (all_df) (raw_dff_data) of a single sample
# If a dataframe with NANs is plotted, use
# marker = '+', or 'o', since the line in the lineplot only connects
# consecutive data points
def aligned_layout_plot(plot, tick_spacing=0.5, fov=(-20, 50, -0.05, 1.9), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)

# For multiple transition types!!
# If a dataframe with NANs is plotted (raw-data = non interpolated), use
# marker = '+', or 'o', since the line in the lineplot only connects
# consecutive data points
def aligned_layout_plot(plot, tick_spacing=2, fov=(-15, 15, -0.04, 1), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    #plot.legend().set_visible(legend)


# Plotting for multi-events (same_behavioral_transition)
# If a dataframe with NANs is plotted (raw-data = non interpolated), use
# marker = '+', or 'o', since the line in the lineplot only connects
# consecutive data points
def aligned_layout_plot(plot, tick_spacing=5, fov=(-18.5, 42.4, 0.0, 1.0), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)


# Plotting for multi-events (same_behavioral_transition)
# If a dataframe with NANs is plotted (raw-data = non interpolated), use
# marker = '+', or 'o', since the line in the lineplot only connects
# consecutive data points
def aligned_layout_plot(plot, tick_spacing=2, fov=(-10, 20, 0.0, 1), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)


# Plotting for multi-events (same_behavioral_transition)
# If a dataframe with NANs is plotted (raw-data = non interpolated), use
# marker = '+', or 'o', since the line in the lineplot only connects
# consecutive data points
def aligned_layout_plot(plot, tick_spacing=2, fov=(-15, 15, 0.0, 0.2), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)


def aligned_layout_plot(plot, tick_spacing=1, fov=(-10, 10, 0.0, 0.9), legend=False):
    # Set fine x-axis scale
    plot.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Set x and y limits and legend (default = False)
    plot.axis(fov)
    plot.legend().set_visible(legend)
