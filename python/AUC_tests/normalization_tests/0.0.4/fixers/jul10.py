import os

def first_line(frst_ln, root, in_p):
    if 'GB' in root and 'run_' in in_p:
        return 'from sklearn.ensemble import GradientBoostingClassifier\n'
    elif 'LR' in root and 'run_' in in_p:
        return 'from sklearn.linear_model import LogisticRegression\n'
    else:
        return frst_ln

def path_check(line):
    if line.count('../') < 5:
        line = line.split('\'')
        return '\'../'.join([line[0], '\''.join([*line[1:]])])
    else:
        return line

def fix_fun():
    return 'def run(genes, random_seed):\n'

def fix_kfold():
    return '    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_seed)\n'

def fix_clf(line, root):
    if 'GB' in root:
        return '        clf = GradientBoostingClassifier(random_state=random_seed)\n'
    elif 'LR' in root:
        return '        clf = LogisticRegression(random_state=random_seed)\n'
    else:
        return line

for root, dirs, files in os.walk('../.'):
    if '__pycache__' in root or 'fixers' in root or 'MLP' in root:
        continue
    print(root)
    print(files)
    for in_p in files:
        if 'run_' not in in_p:
            continue
        output = ''
        in_f = open('/'.join([root, in_p]), 'r')
        output = first_line(in_f.readline(), root, in_p)
        print(output)
        for line in in_f:
            if 'pd.read' in line:
                line = path_check(line)
            elif 'def run' in line:
                line = fix_fun()
            elif 'StratifiedKFold(' in line:
                line = fix_kfold()
            elif 'clf =' in line:
                line = fix_clf(line, root)
            #print(line)
            output += line
        in_f.close()
        out_f = open('/'.join([root, in_p]), 'w')
        out_f.write(output)
        out_f.close()
        #if 'LR' in root:
            #print(output)
