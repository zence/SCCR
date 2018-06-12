import sys

in_p = sys.argv[1]

total = 0
instances = 0

with open(in_p, 'r') as in_f:
    for line in in_f:
        if line.startswith("AUC"):
            total += float(line.split()[2])
            instances += 1

mean = total / instances 
print(mean)

