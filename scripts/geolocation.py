import pandas as pd
import numpy as np


def load_data():
    fraud_df = pd.read_csv("data/raw/fraud_data.csv")
    ip_df = pd.read_csv("data/raw/IpAddress_to_Country.csv")

    return fraud_df, ip_df


def convert_ip_to_int(df):
    df["ip_address"] = df["ip_address"].astype(np.int64)
    return df


if __name__ == "__main__":
    fraud_df, ip_df = load_data()

    fraud_df = convert_ip_to_int(fraud_df)

    print(fraud_df["ip_address"].dtype)
    print(ip_df.head())