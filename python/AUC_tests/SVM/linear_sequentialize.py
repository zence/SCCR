import run_svm_linear
import math
import itertools

def sequence(genes, best_string='', best_auc=0, ix=0, *args):
    for i in range(len(genes)):
        if i >= ix:
            temp_genes = genes[:i + 1]
            cur_auc = run_svm_linear.run(temp_genes)
            print(', '.join(temp_genes) + ': ' + str(cur_auc), flush=True)
            if cur_auc > best_auc:
                best_auc = cur_auc
                best_string = ', '.join(temp_genes)
            else:
                ix = i
                break
    print("**BEST**\n" + best_string + ': ' + str(best_auc), flush=True)
    return best_string, best_auc, ix
    
def scramble(genes, add_genes=None):
    ix_genes = []
    ix = 0
    best_string = ''
    best_auc = 0
    if add_genes is not None:
        genes.remove(*add_genes)
        for perm in itertools.permutations(genes, len(genes)):
            temp = [*add_genes, *perm]
            #print(temp, flush=True)
            #print("IX: " + str(ix), flush=True)
            #print(ix_genes, flush=True)
            #print(temp[:ix + 1], flush=True)
            if ix == 0 or ix_genes != temp[:ix + 1]:
                best_string, best_auc, ix = sequence(temp, best_string, best_auc, ix)
            if ix > 0:
                ix_genes = temp[:ix + 1]
    else:
        for perm in itertools.permutations(genes, len(genes)):
            print(perm)
            if ix == 0 or ix_genes != perm[:ix + 1]:
                best_string, best_auc, ix = sequence(perm, best_string, best_auc, ix)
            if ix > 0:
                ix_genes = perm[:ix + 1]



all_genes = ''

with open("../../../data/all_genes_TPM.tsv", 'r') as in_f:
    all_genes = in_f.readline().split('\t')

spec_genes = ['FGFR1', 'EGFR', 'IGF1R', 'FGF1', 'EGF', 'IGF1']
just_ERBB2 = ['ERBB2']

all_genes = [x if x not in spec_genes and x not in just_ERBB2 else None for x in all_genes]

#auc_ERBB2 = run_svm.run(just_ERBB2)

#sequence([*just_ERBB2, *spec_genes])
#print("No add_genes")
scramble([*just_ERBB2, *spec_genes])
#print("add_genes = just_ERBB2")
#scramble([*just_ERBB2, *spec_genes], add_genes=just_ERBB2)
