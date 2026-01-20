import pandas as pd
import numpy as np

def yoy(series, periods=12):
    return series.pct_change(periods) * 100

def mom(series):
    return series.pct_change(1) * 100

def qoq(series):
    return series.pct_change(3) * 100

def zscore(series, window=60):
    return (series - series.rolling(window).mean()) / series.rolling(window).std()

def index_to_100(series, base_date=None):
    if base_date is None:
        base_date = series.first_valid_index()
    return series / series.loc[base_date] * 100

def real_adjust(nominal, cpi):
    return nominal / cpi * 100
