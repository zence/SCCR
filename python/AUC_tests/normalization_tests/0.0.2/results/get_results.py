import os

no_no_dirs = ['pycache', 'fixers', 'MLP', 'results']

output = ''

for root, dirs, files in os.walk('../.'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue
    #output = ''
    for in_p in files:
        if 'slurm' in in_p:
            aucs = []
            in_f = open('/'.join([root, in_p]), 'r')
            in_f.readline()
            output += in_f.readline()
            for line in in_f:
                if line.startswith('AUC'):
                    aucs.append(float(line.split(': ')[1]))
            avg_auc = sum(aucs) / len(aucs)
            output += str(avg_auc) + '\n'
            in_f.close()
    output += '\n'
    #print(output)
out_f = open('avg_aucs.txt', 'w')
out_f.write(output)
out_f.close()
