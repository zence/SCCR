import glob

outputs = glob.glob('output*.txt')
avg_auc = {}

for in_p in outputs:
    aucs = []
    identifier = in_p.replace('.txt', '')
    identifier = identifier.replace('output_', '')
    with open(in_p, 'r') as in_f:
        for line in in_f:
            if line.startswith('0.'):
                aucs.append(float(line.strip()))
        if len(aucs) > 0:
            avg_auc[identifier] = sum(aucs) / len(aucs)

print(avg_auc)
