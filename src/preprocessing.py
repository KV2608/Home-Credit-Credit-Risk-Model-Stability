import pandas as pd

def preprocess_data(df):
    df = df.copy()
    df.fillna(-1, inplace=True)
    return df
