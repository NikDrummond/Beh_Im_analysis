# Packages used
# Import libraries

import pandas as pd
import glob, os
from tqdm import tqdm
import pandas as pd
import re

# created functions

def load_beh(path):
    """ Load behaviour files in a specified folder

    Files MUST have specific format, and have behavior in the name.

    Parameters
    ----------

    path:   str
            The file path to the folder containing the behavioural data.

    Returns
    -------

    dict:   dict
            Dictionary, with entry per file. Keys are the ID at the start of the file name, each value
            is a DataFrame of encoded behaviours.

    """

    # loop over each file in the folder, selecting the .csv files with 'behavior' in the name
    beh_data = {}
    for fname in glob.glob(path + '*.csv'):
        if 'behavior' in fname:
            # Get the dataframe and edit a touch
            data = pd.read_csv(fname, index_col = None, header=0, delimiter=';')
            data.fillna(0,inplace = True)
            # set up the dictionary key
            key = os.path.basename(fname)
            key = key.replace("behavior","")
            key = key.replace(".csv","")

            # add to dictionary
            beh_data[key] = data
    return(beh_data)

def load_flour(path):
