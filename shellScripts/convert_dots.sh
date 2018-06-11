#! /bin/bash

final_num=19

for i in $(seq 0 $final_num);
do
  echo $i
  dot -o../graphs/classif_"$i".png -Tpng ../graphs/classif_"$i".dot
done
