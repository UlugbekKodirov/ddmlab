import numpy as np
import argparse
import pandas as pd

f = open("/mnt/top200_5mers.txt", "r")
k_mers = f.read().splitlines()
#k_mers = ['AAAAAA', 'SSSSSS', 'QQQQQQ', 'GGGGGG']
vector_mapping = {e: i for i, e in enumerate(k_mers)}
def get_substrings(seq, k):
    n = len(seq)
    res = map(lambda i: seq[i:i + k], range(n - k + 1))
    return list(res)
def to_vector(seq, one_hot=True):
    res = np.zeros(len(k_mers))
    for mer in get_substrings(seq, len(k_mers[0])):
        if mer in vector_mapping:
            if one_hot:
                res[vector_mapping[mer]] = 1
            else:
                res[vector_mapping[mer]] += 1
    return res

#arguments handling
# parser = argparse.ArgumentParser(description='dataset vectorizer.')
# parser.add_argument('test_dataset.csv')
# args = parser.parse_args()
# #import the given dataset and vectorize it
df = pd.read_csv("/mnt/test_dataset.csv")  #args.datasetPath)
df['vectorize']=df.apply(lambda row: to_vector(row['seq'],row[0]), axis=1)
df = pd.concat([ df['label'], pd.DataFrame(df['vectorize'].values.tolist()) ], axis=1)
df.to_csv('/mnt/vecProteinLabel.csv', index=False)