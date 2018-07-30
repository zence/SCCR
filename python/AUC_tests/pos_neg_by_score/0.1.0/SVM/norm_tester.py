import sys
import os
import pandas as pd

mod_name = sys.argv[1].replace('.py', '')
random_seed = int(sys.argv[2])

cur_module = __import__(mod_name)

all_genes = ''
select_genes = []

if os.path.isfile('../results/misclassified_samples.tsv'):
    misclassied_samples = pd.read_csv('../results/misclassified_samples.tsv', sep='\t')
else:
    misclassied_samples = pd.DataFrame({'Sample': [], 'times_misclassified': [], 'notes': []})

print('rbf_SVM ' + mod_name)

# load gene data
with open('../genes.txt', 'r') as in_f:
    for line in in_f:
        select_genes.append(line.strip())

print(select_genes)

misclassied_samples = cur_module.run(select_genes, random_seed, misclassied_samples)

print(misclassied_samples)

misclassied_samples.to_csv('../results/misclassified_samples.tsv', sep='\t', index=False)

#print(''.join(['AUCs for ', mod_name, ': ', ', '.join([str(x) for x in avg_auc])]))
