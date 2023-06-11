import pandas as pd

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
