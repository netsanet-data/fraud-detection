"""
Feature engineering utilities.
"""

import pandas as pd


def create_time_since_signup(df):
    df['time_since_signup'] = (
        df['purchase_time'] - df['signup_time']
    ).dt.total_seconds() / 3600

    return df


def create_hour_of_day(df):
    df['hour_of_day'] = df['purchase_time'].dt.hour

    return df


def create_day_of_week(df):
    df['day_of_week'] = df['purchase_time'].dt.day_name()

    return df