import run_vsd_rf
import math
import itertools

def sequence(genes, *args):
    best_auc = 0
    best_string = ''
    for i in range(len(genes)):
        temp_genes = genes[:i + 1]
        cur_auc = run_vsd_rf.run(temp_genes)
        print(', '.join(temp_genes) + ': ' + str(cur_auc), flush=True)
        if cur_auc > best_auc:
            best_auc = cur_auc
            best_string = ', '.join(temp_genes)
    print("**BEST**\n" + best_string + ': ' + str(best_auc), flush=True)
    
def scramble(genes, add_genes=None):
    if add_genes is not None:
        genes.remove(*add_genes)
        for perm in itertools.permutations(genes, len(genes)):
            print([*add_genes, *perm], flush=True)
            sequence([*add_genes, *perm])
    else:
        for perm in itertools.permutations(genes, len(genes)):
            print(perm)



all_genes = ''

print("VSD RF")

with open("../../../data/vsd_FeatureCounts.tsv", 'r') as in_f:
    all_genes = in_f.readline().split('\t')

spec_genes = ['FGFR1', 'EGFR', 'IGF1R', 'FGF1', 'EGF', 'IGF1']
just_ERBB2 = ['ERBB2']

all_genes = [x for x in all_genes if x not in spec_genes and x not in just_ERBB2]
all_genes = [x for x in all_genes if x != 'Sample' and 'her2' not in x]

#auc_ERBB2 = run_svm.run(just_ERBB2)

#sequence([*just_ERBB2, *spec_genes])
#print("No add_genes")
#scramble([*just_ERBB2, *spec_genes])
#print("add_genes = just_ERBB2")
scramble([*just_ERBB2, *spec_genes], add_genes=just_ERBB2)
