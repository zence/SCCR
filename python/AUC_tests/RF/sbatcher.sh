scripts=$(echo do_the*)

for script in $scripts;
do
  sbatch $script
done
