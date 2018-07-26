import os

## sequentializer.py

#with open('../genes.txt', 'r') as in_f:
#	to
#with open('../../genes.txt', 'r') as in_f:

#cur_auc = run_vsd_svm.run([*important_genes, gene])
#	to
#cur_auc = run_vsd_gb.run([gene])

### NOTE: you did not automate the above issue. In other words, you set all programs to run vsd_gb, you doof

## run_*.py

#total_her2_expr = pd.read_csv('../../../../data/vsd_FeatureCounts.tsv', sep='\t')
#	to
#total_her2_expr = pd.read_csv('../../../../../data/vsd_FeatureCounts.tsv', sep='\t')

no_no_dirs = ['pycache', 'results', 'fixers', 'MLP']

output = ''

for root, dirs, files in os.walk('../'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue 
    for in_n in files:
        output = ''
        if in_n == 'sequentializer.py':
            in_f = open('/'.join([root, in_n]), 'r')
            for line in in_f:
                if line.strip() == "with open('../genes.txt', 'r') as in_f:":
                    output += "with open('../../genes.txt', 'r') as in_f:\n"
                elif line.strip() == 'cur_auc = run_vsd_svm.run([*important_genes, gene])':
                    output += '        cur_auc = run_vsd_gb.run([gene])\n'
                elif line.strip() == 'cur_auc = run_vsd_gb.run([gene])':
                    output += '        cur_auc = run_vsd_gb.run([gene])\n'
                else:
                    output += line
            print(output)
            in_f.close()
            out_f = open('/'.join([root, in_n]), 'w')
            out_f.write(output)
            out_f.close()
        elif 'run_' in in_n:
            in_f = open('/'.join([root, in_n]), 'r')
            print(in_n)
            for line in in_f:
                if "total_her2_expr = pd.read_csv('" in line:
                    if line.count('../') == 5:
                        output += line
                    else:
                        new_line = line.split("('")
                        output += "('".join([new_line[0], ('../' + new_line[1])])
                else:
                    output += line
            print(output)
            in_f.close()
            out_f = open('/'.join([root, in_n]), 'w')
            out_f.write(output)
            out_f.close()
        else:
            continue 
