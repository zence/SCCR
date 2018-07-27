import sys
import pandas as pd

mod_name = sys.argv[1].replace('.py', '')
random_seed = int(sys.argv[2])

cur_module = __import__(mod_name)

all_genes = ''

misclassied_samples = pd.DataFrame({'Sample': [], 'times_misclassified': [], 'notes': []})

print('rbf_SVM ' + mod_name)

# load gene data
with open('../genes.txt', 'r') as in_f:
    select_genes = in_f.readline().rstrip().split('\t')


avg_auc = cur_module.run(all_genes, random_seed)

print(''.join(['AUCs for ', mod_name, ': ', ', '.join([str(x) for x in avg_auc])]))
