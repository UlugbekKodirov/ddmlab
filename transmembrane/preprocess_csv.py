import skbio
import pandas as pd

def map_values(input_file, output_file, label_file):
    labels = []
    for label in open(label_file, 'r'):
        labels.append(label.strip('\n'))
    label_set = set(labels)
    with open(output_file, 'w') as output:
        for i, seq in enumerate(skbio.io.read(input_file, format='fasta')):
            if seq.metadata['id'] in label_set:
                output.write(str(i) + '\n')

def create_dataset(pos_file, seq_file, save_file, neg_ratio=1, rnd_seed=0, num_seq=69029793):
    import numpy as np
    np.random.seed(rnd_seed)
    true_i = []
    for pos in open(pos_file, 'r'):
        true_i.append(int(pos.strip('\n')))
    true_i = set(true_i)
    neg_i = set([])
    for i in range(int(len(true_i) * neg_ratio)):
        neg_samp = np.random.randint(num_seq)
        while neg_samp in true_i or neg_samp in neg_i:
            neg_samp = np.random.randint(num_seq)
        neg_i.add(neg_samp)
    samples = []
    for i, seq in enumerate(skbio.io.read(seq_file, format='fasta')):
        if i in true_i:
            samples.append((seq, 1))
        elif i in neg_i:
            samples.append((seq, 0))
    df = pd.DataFrame(samples, columns=['seq', 'label'])
    print(df)
    df.to_csv(save_file)
#map_values(input_file="/mnt/uniref90.fasta", output_file="/mnt/map_values_output.txt", label_file="/mnt/transmembrane_ids.txt")
create_dataset(pos_file="/mnt/map_values_output.txt", seq_file="/mnt/uniref90.fasta", save_file="/mnt/test_dataset.csv")

