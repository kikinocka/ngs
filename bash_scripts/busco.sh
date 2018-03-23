#!/bin/bash
cd /home/tomas/GIT/busco

python BUSCO.py -m tran -i /home/kika/work_dir/CA_Trinity.fasta -o BUSCO_CA_protists -sp chlamydomonas_reinhardtii -l /home/tomas/GIT/busco/protists_ensembl -c 16 --long -f
