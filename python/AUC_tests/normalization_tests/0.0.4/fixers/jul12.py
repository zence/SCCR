import os

no_no_dirs = ['pycache', 'results', 'fixers', 'MLP']

for root, dirs, files in os.walk('../.'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue
    for in_n in files:
        output = ''
        in_f = open('/'.join([root, in_n]), 'r')
        if 'run_' in in_n:
            for line in in_f:
                if 'return (sum' in line:
                    line = '    return auc_vals'
                output += line
        elif 'norm' in in_n:
            for line in in_f:
                if "print(''.join" in line:
                    line = "print(''.join(['AUCs for ', mod_name, ': ', ', '.join([str(x) for x in avg_auc])]))"
                output += line
        else:
            continue
        print(output)
        in_f.close()
        out_f = open('/'.join([root, in_n]), 'w')
        out_f.write(output)
        out_f.close()


#print(''.join(['AUCs for ', mod_name, ': ', ', '.join(avg_auc)]))
