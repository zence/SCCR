import os

no_no_dirs = ['pycache', 'results', 'fixers', 'MLP']

output = ''

for root, dirs, files in os.walk('../'):
    if any(no_no_dir in root for no_no_dir in no_no_dirs):
        continue 
    for in_n in files:
        output = ''
        if 'run_' in in_n:
            in_f = open('/'.join([root, in_n]), 'r')
            for line in in_f:
                if 'posneg_score' in line:
                    line = line.replace('posneg_score', 'FeatureCounts_fish')
                elif 'her2_status_by_ihc' in line:
                    line = line.replace('her2_status_by_ihc', 'her2_fish_status')
                output += line
            in_f.close()
            out_f = open('/'.join([root, in_n]), 'w')
            out_f.write(output)
            out_f.close()
        #print(output)
