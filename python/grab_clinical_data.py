import sys

keyword = sys.argv[1]

out_f = open("../data/" + keyword + "_Clinical_Data.tsv",'w')

with open("../../cancerproject/proj_090817/data/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt", 'r') as in_f:
    out_f.write(in_f.readline())
    for line in in_f:
        line = line.split('\t')
        if keyword in line[0]:
            out_f.write('\t'.join(line))
    out_f.close()
