import sys
import run_norm_quan_rf


all_genes = []

print('RF Sequence All', flush=True)

# load gene data
with open('../../genes.txt', 'r') as in_f:
    for line in in_f:
        all_genes.append(line.strip())

#erbb2_auc = run_norm_quan_rf.run(['ERBB2'])
important_genes = []
# Declaring here just in case python throws a fit
cur_best_auc = 0
cur_auc = []

for ix in range(20):
    cur_best_auc = 0
    cur_auc = 0
    for gene in all_genes:
        if gene in important_genes:
            continue
        cur_auc = run_norm_quan_rf.run([*important_genes, gene])
        if cur_auc > cur_best_auc:
            cur_best_auc = cur_auc
            winner = gene
            print("Current best AUC: " + str(cur_best_auc), flush=True)
    important_genes.append(winner)
    print(': '.join(['The winners so far: ', ', '.join(important_genes)]), flush=True) 

print('WINNER: ' + ', '.join(important_genes) + '\nAUC: ' + str(cur_best_auc))
