import os

output = ''

for root, dirs, files in os.walk('../'):
    for in_n in files:
        output = ''
        if in_n == 'sequentializer.py':
            in_f = open('/'.join([root, in_n]), 'r')
            for line in in_f:
                if line.strip() == "all_genes = ''":
                    output += 'all_genes = []\n'
                elif line.startswith('with'):
                    output += "with open('../genes.txt', 'r') as in_f:\n    for line in in_f:\n        all_genes.append(line.strip())"
                elif line.startswith('    all_genes'):
                    continue
                elif line.endswith("ihc']]\n"):
                    continue
                else:
                    output += line
            print(output)
            in_f.close()
            out_f = open('/'.join([root, in_n]), 'w')
            out_f.write(output)
            out_f.close()
