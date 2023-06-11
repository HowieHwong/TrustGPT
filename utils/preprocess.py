import os
import pandas as pd


def get_txt_file(filename):
    assert type(filename) == str
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [el.strip('\n') for el in data]
    return data


def get_csv_file(filename):
    assert type(filename) == str
    assert filename.split('.')[-1] == 'csv'
    data = pd.read_csv(filename)
    if 'res' not in data.columns:
        raise Exception("no res column!")
    all_data = []
    for index, el in data.iterrows():
        all_data.append(el['res'])
    return all_data