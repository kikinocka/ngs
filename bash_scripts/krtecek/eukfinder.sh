#!/bin/bash

# #activate in terminal, then run script, then deactivate
# conda activate eukfinder

cd '/home/users/kika/eukfinder/'

#path to databases
databases='/home2/BW2026/Eukfinder/eukfinder_databases/'
plastdb=$databases'PlastDB.fasta'
plastmap=$databases'PlastDB_map.txt'
centrifuge=$databases'Centrifuge_Sept2020'

#path to longreads
longreads='unfiltered_spades_BL_01.fasta'
prefix='BL_01'

eukfinder long_seqs -l $longreads -o $prefix -n 20 -z 2 -t False -p $plastdb -m $plastmap \
	-e 0.001 --pid 60 --cov 20 --cdb $centrifuge --mhlen 50
#-t True - only the first time (or after a long time) because it downloads databases; then False

# conda deactivate
