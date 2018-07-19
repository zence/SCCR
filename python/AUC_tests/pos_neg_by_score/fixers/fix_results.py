output = ''
with open('../results/all_aucs.txt', 'r') as in_f:
    for line in in_f:
        if line.endswith('gb\n') and not line.startswith('GB'):
            line = line.split()
            line = ' '.join(['GB', line[-1]])
            print(line)
        output += line
