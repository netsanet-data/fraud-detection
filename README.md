# Fraud Detection for E-commerce and Bank Transactions

## Project Overview

This project focuses on detecting fraudulent transactions in e-commerce and banking datasets using data analysis, preprocessing, feature engineering, and class imbalance handling techniques.

The objective is to prepare high-quality datasets for machine learning models capable of identifying fraudulent activities.

## Datasets

* Fraud_Data.csv
* creditcard.csv
* IpAddress_to_Country.csv

## Project Structure

fraud-detection/

├── data/

│   ├── raw/

│   └── processed/

├── notebooks/

│   ├── eda-fraud-data.ipynb

│   ├── eda-creditcard.ipynb

│   └── feature-engineering.ipynb

├── scripts/

├── src/

├── tests/

├── models/

├── requirements.txt

├── README.md

└── .gitignore

## Tasks Completed

### Data Cleaning

* Missing value analysis
* Duplicate checking
* Data type corrections

### Exploratory Data Analysis

* Univariate analysis
* Bivariate analysis
* Class imbalance analysis

### Feature Engineering

* time_since_signup
* hour_of_day
* day_of_week
* transaction_velocity

### Data Transformation

* One-hot encoding
* Standard scaling

### Class Imbalance Handling

* SMOTE applied to training data only

## Installation

```bash
pip install -r requirements.txt
```

## Author

Netsanet Gebrekidan
