# functions for maths things

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

# Function to calculate the average cell/pattern_groups depending on regex
def average_grouping(grouping):
    df = grouping[list(grouping)[0]][1]
    average_df = pd.DataFrame(index=df.index)

    for group_pattern, df in grouping.values():
        average_col = df.mean(axis=1)
        average_df[group_pattern] = average_col

    return average_df

# Function to calculate the std cell/pattern_groups depending on regex
def std_grouping(grouping):
    df = grouping[list(grouping)[0]][1]
    std_df = pd.DataFrame(index=df.index)

    for group_pattern, df in grouping.values():
        std_col = df.std(axis=1)
        std_df[group_pattern] = std_col

    return std_df

# Function to calculate the sem cell/pattern_groups depending on regex
def sem_grouping(grouping):
    df = grouping[list(grouping)[0]][1]
    sem_df = pd.DataFrame(index=df.index)

    for group_pattern, df in grouping.values():
        sem_col = df.sem(axis=1)
        sem_df[group_pattern] = sem_col

    return sem_df
