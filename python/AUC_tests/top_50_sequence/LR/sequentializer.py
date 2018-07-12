import sys
import run_vsd_robust_lr


all_genes = ''

print('LR Sequence 50', flush=True)

# load gene data
with open('../../../../data/all_genes_TPM.tsv', 'r') as in_f:
    all_genes = in_f.readline().rstrip().split('\t')

all_genes = [x for x in all_genes if x not in ['Sample', 'her2_status_by_ihc']]

erbb2_auc = run_vsd_svm.run(['ERBB2'])
important_genes = ['ERBB2']
# Declaring here just in case python throws a fit
cur_best_auc = 0
cur_auc = []

for ix in range(10):
    cur_best_auc = 0
    cur_auc = 0
    for gene in all_genes:
        if gene in important_genes:
            continue
        cur_auc = run_vsd_svm.run([*important_genes, gene])
        if cur_auc > cur_best_auc:
            cur_best_auc = cur_auc
            winner = gene
            print("Current best AUC: " + str(cur_auc), flush=True)
    important_genes.append(winner)
    print(': '.join(['The winners so far: ', ', '.join(important_genes)])) 

print('WINNER: ' + ', '.join(important_genes), + '\nAUC: ' + cur_best_auc)
