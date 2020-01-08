# classes

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

# Define a class with sample_id, cell_type, event_name and filter_pattern

class CellTraceConfig:

    def __init__(self, sample_id, cell_type, event_name, filter_pattern=None):
        self.sample_id = sample_id
        self.cell_type = cell_type
        self.event_name = event_name
        self.filter_pattern = filter_pattern

    def get_filter_regex(self):
        filter_regex = '^{}_'.format(self.cell_type)
        if self.filter_pattern:
            filter_regex += '.*{}.*'.format(self.filter_pattern)
        return filter_regex

    def get_event_start_col(self):
        return '{}_start'.format(self.event_name)

    def add_event_time_points_to_plot(self, source_df, plot):
        for idx, row in source_df.iterrows():
            plot.annotate(self.event_name, xy=(row['time'], 1))
            plt.axvline(row['time'], color='k', linestyle='-')

# Define a class with sample_id, cell_type, event_time and filter_pattern (for behavioral_transitions)
# Put '' [empty string] if you dont want any cell type

class CellTransConfig:

    def __init__(self, sample_id, cell_type, event_time, filter_pattern=None, first_event=None, second_event=None):
        self.sample_id = sample_id
        self.cell_type = cell_type
        self.event_time = event_time
        self.filter_pattern = filter_pattern
        self.first_event = first_event
        self.second_event = second_event

    def get_filter_regex(self):
        if self.cell_type is None:
            cell_str = r"[a-zA-Z0-9]+"
        else:
            cell_str = self.cell_type

        filter_regex = '^{}_'.format(cell_str)
        if self.filter_pattern:
            filter_regex += '.*{}.*'.format(self.filter_pattern)
        return filter_regex



# Define a class for filtering after behavioral_transitions for either only cell_type or filter_pattern or both.
# For example to average not only over all A00cs but all A00c_midL.

class DataFilter():
    def __init__(self, cell=None, pattern=None):
        self.cell = cell if cell is not None else '.*' # Makes argument optional
        self.pattern = pattern if pattern is not None else '.*' # Makes argument optional

    def get_cell_filter_regex(self):
        filter_regex = '.*_{}_.*_.*'.format(self.cell)
        return filter_regex

    def get_pattern_filter_regex(self):
        filter_regex = '.*_.*_{}_.*'.format(self.pattern)
        return filter_regex

    def get_cellpattern_filter_regex(self):
        filter_regex = '.*_{}_{}_.*'.format(self.cell, self.pattern)
        return filter_regex

    def __str__(self):
        return "{}_{}".format(self.cell, self.pattern)


# Define class to group the columns after cell_type/ pattern or both using the class Datafilter

class TransitionGrouper:
    def __init__(self, transitions_df):
        self.transitions_df = transitions_df

        sample_ids, cells, patterns, *_ = zip(*[column.split("_") for column in self.transitions_df.columns])

        self.sample_ids = sorted(set(sample_ids))
        self.cells = sorted(set(cells))
        self.patterns = sorted(set(patterns))

    def get_regex(self, cell_name=None, pattern=None):
        data_filter = DataFilter(cell=cell_name, pattern=pattern)
        if cell_name is not None and pattern is None:
            return data_filter, data_filter.get_cell_filter_regex()
        if cell_name is not None and pattern is not None:
            return data_filter, data_filter.get_cellpattern_filter_regex()
        if cell_name is None and pattern is not None:
            return data_filter, data_filter.get_pattern_filter_regex()
        raise ValueError("Both cell_name and pattern are None! :(")

    def group_cells(self):
        output = dict()
        for cell_name in self.cells:
            data_filter, regex = self.get_regex(cell_name)
            cell_df = self.transitions_df.filter(regex=regex)
            output[cell_name] = (str(data_filter), cell_df)
        return output

    def group_patterns(self):
        output = dict()
        for pattern in self.patterns:
            data_filter, regex = self.get_regex(pattern=pattern)
            pattern_df = self.transitions_df.filter(regex=regex)
            output[pattern] = (str(data_filter), pattern_df)
        return output

    def group_cellpattern(self):
        output = dict()
        for cell_name, pattern in itertools.product(self.cells, self.patterns):
            data_filter, regex = self.get_regex(cell_name, pattern)
            cellpattern_df = self.transitions_df.filter(regex=regex)
            output[(cell_name, pattern)] = (str(data_filter), cellpattern_df)
        return output

# Specific after Post-transitions for multiple transition kinds, used for plotting. For multiple transition
# events, group after transition (first, or second event) <most useful> with option to group
# after celltype, filterpattern, sample_id, observations.
class TransitionType:
    def __init__(self, sample_id=".*", cell=".*", filter_pattern=".*", n_obs=".*", first_event=".*", second_event=".*"):
        self.sample_id = sample_id
        self.cell = cell
        self.filter_pattern = filter_pattern
        self.n_obs = n_obs
        self.first_event = first_event
        self.second_event = second_event

        self.pattern = "{}_{}_{}_{}_{}_{}"

    def get_filter_regex(self, use_all=False, use_cell=False, use_sample=False, use_filter_pattern=False, use_n_obs=False, use_first_event=False, use_second_event=False):
        filter_regex = self.pattern.format(self.sample_id if use_sample or use_all else ".*",
                                          self.cell if use_cell or use_all else ".*",
                                          self.filter_pattern if use_filter_pattern or use_all else ".*",
                                          self.n_obs if use_n_obs or use_all else ".*",
                                          self.first_event if use_first_event or use_all else ".*",
                                          self.second_event if use_second_event or use_all else ".*")
        return filter_regex

class PostBehaviorTransition:

    def __init__(self, sample_id, event, post_event, max_delay=0):
        self.sample_id = sample_id
        self.post_event = post_event
        self.event = event
        self.max_delay = max_delay


class SamePairBehaviorTransition:

    def __init__(self, sample_id, pre_event, event, max_delay=0, max_ignored_quiet_time=math.inf):
        self.sample_id = sample_id
        self.pre_event = pre_event
        self.event = event
        self.max_delay = max_delay
        self.max_ignored_quiet_time = max_ignored_quiet_time
