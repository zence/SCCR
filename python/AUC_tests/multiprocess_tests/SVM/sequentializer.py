import sys
import run_vsd_svm
from multiprocessing.pool import Pool


all_genes = ''

print('SVM Sequence All', flush=True)

# load gene data
with open('../../../../data/all_genes_TPM.tsv', 'r') as in_f:
    all_genes = in_f.readline().rstrip().split('\t')

all_genes = [x for x in all_genes if x not in ['Sample', 'her2_status_by_ihc']]

erbb2_auc = run_vsd_svm.run(['ERBB2'])
important_genes = ['ERBB2']
# Declaring here just in case python throws a fit
cur_best_auc = 0
cur_auc = []

for ix in range(30):
    cur_best_auc = 0
    cur_auc = 0
    pools = [None] * len(all_genes)
    for j, gene in enumerate(all_genes):
        pools[j] = 
        if gene in important_genes:
            continue
        aucs.append(
        cur_auc = run_vsd_svm.run([*important_genes, gene])
        
        print("Current best AUC: " + str(cur_auc), flush=True)
    important_genes.append(winner)
    print(': '.join(['The winners so far: ', ', '.join(important_genes)])) 

print('WINNER: ' + ', '.join(important_genes), + '\nAUC: ' + cur_best_auc)
