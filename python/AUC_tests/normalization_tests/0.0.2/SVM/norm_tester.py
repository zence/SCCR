import sys

mod_name = sys.argv[1].replace('.py', '')
random_seed = int(sys.argv[2])

cur_module = __import__(mod_name)

all_genes = ''

print('rbf_SVM ' + mod_name)

# load gene data
with open('../../../../../data/all_genes_TPM.tsv', 'r') as in_f:
    all_genes = in_f.readline().rstrip().split('\t')

all_genes = [x for x in all_genes if x not in ['Sample', 'her2_status_by_ihc']]

avg_auc = cur_module.run(all_genes, random_seed)

print(''.join(['AUC for ', mod_name, ': ', str(avg_auc)]))
