"""
Data preprocessing utilities.
"""

import pandas as pd


def load_data(filepath):
    """
    Load CSV file.
    """
    return pd.read_csv(filepath)


def check_missing_values(df):
    """
    Return missing value counts.
    """
    return df.isnull().sum()


def check_duplicates(df):
    """
    Return duplicate count.
    """
    return df.duplicated().sum()