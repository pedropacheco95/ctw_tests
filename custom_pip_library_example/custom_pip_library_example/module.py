import pandas as pd


def add_numbers(a, b):
    s = pd.Series([a, b])
    return s.sum()
