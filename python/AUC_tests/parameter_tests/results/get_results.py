import os
import pandas as pd

no_no_dirs = ['pycache', 'fixers', 'MLP', 'results', '0.0.2']

no_no_files = ['automator.sh']

raw_aucs = pd.DataFrame(columns = ['model', 'method', 'auc'])

for root, dirs, files in os.walk('../.'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue
    #output = ''
    for in_p in files:
        if 'slurm' in in_p:
            in_f = open('/'.join([root, in_p]), 'r')
            in_f.readline()
            metadata = in_f.readline().split(' ')
            model = metadata[0]
            if model == '':
                continue
            method = '_'.join(metadata[1].split('_')[1:-1])
            for line in in_f:
                if line.startswith('AUC'):
                    aucs = line.split(': ')[1].split(', ')
                    for auc in aucs:
                        raw_aucs = raw_aucs.append({'model': model,
                                                    'method': method,
                                                    'auc': float(auc)},
                                                    ignore_index=True)
                    #aucs.append(float(line.split(': ')[1]))
            in_f.close()
    #print(output)
raw_aucs.to_csv('raw_aucs_params.tsv', sep='\t', index=False)
