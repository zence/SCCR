# Third round tests

These tests are near identical to the 0.0.2 tests, however, AUCs are not averaged out before being sent out. `automator.sh` runs all 
`sbatcher.sh` scripts. After all slurm jobs are finished, `results/get_results.py` must be run manually to create `raw_aucs.tsv`,
which will be copied to Kumiko for analysis.
