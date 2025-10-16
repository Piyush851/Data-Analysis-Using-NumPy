import numpy as np
import pandas as pd

def load_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    return df

