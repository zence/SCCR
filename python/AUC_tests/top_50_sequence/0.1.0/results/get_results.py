import os
import pandas as pd

no_no_dirs = ['pycache', 'fixers', 'MLP', 'results', '0.0.2']

no_no_files = ['automator.sh']

best_genes = pd.DataFrame(columns = ['model', 'genes', 'auc'])

for root, dirs, files in os.walk('../.'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue
    #output = ''
    for in_p in files:
        if 'slurm' in in_p:
            in_f = open('/'.join([root, in_p]), 'r')
            metadata = in_f.readline().split(' ')
            model = metadata[0]
            if model == '':
                continue
            for line in in_f:
                if line.startswith('Current best'):
                    auc = line.strip().split(': ')[1]
                elif line.startswith('The winners so far'):
                    genes = line.strip().split(': ')[2].split(', ')
                    best_genes = best_genes.append({'model': model,
                                                    'genes': ','.join(genes),
                                                    'auc': float(auc)},
                                                    ignore_index=True) 
            in_f.close()
    #print(output)
best_genes.to_csv('seqd_genes_fish.tsv', sep='\t', index=False)
