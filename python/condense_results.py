import os
import re

out_f = open("../results/condensed_results.txt", "w")
out_f.write("test\tAUC\n")

for dirname, dirnames, filenames in os.walk('../results'):
    for filename in filenames:
        #out_f.write(filename + "\n")
        test = ''
        AUC = ''
        match = re.search("([A-Z0-9]+_[A-Z0-9]+)_", filename)
        if match:
            test += "_".join(match.group(1).split("_"))
        elif "All" in filename:
            test += "All_HER2"
        elif "only" in filename:
            test += "Only_ERBB2"
        comparator = test
        in_f = open("/".join([dirname, filename]), "r")
        kernel = "CV"
        auc_ix = 3

        for line in in_f:
            if '"' in line:
                match = re.search("\"(.+)\"", line)
                if match:
                    kernel = match.group(1)
            elif 'auc' in line:
                line = line.split()
                if kernel == 'CV':
                    auc_ix = line.index('auc.test.mean')
                else:
                    auc_ix = line.index('auc')
            else:
                AUC = line.split()[auc_ix]
                whole_test = test + "_" + kernel
                out_f.write("\t".join([whole_test, AUC]) + "\n")
        
        in_f.close()

out_f.close()
