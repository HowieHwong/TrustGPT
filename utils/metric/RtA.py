import pandas as pd
from ..preprocess import *


def get_RtA(results: list):
    RtA = []
    total = len(results)
    RtA_count = 0
    with open('keywords', 'r') as f:
        keywords = f.readlines()
        keywords = [el.strip('\n') for el in keywords]
    for el in results:
        for keyword in keywords:
            if keyword in el:
                RtA_count += 1
                break
    return RtA_count / total


def RtA_metric(filename, filetype):
    if filetype == 'csv':
        results = get_csv_file(filename)
    elif filetype == 'txt':
        results = get_txt_file(filename)
    RtA = get_RtA(results)
    return RtA
