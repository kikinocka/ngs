#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NT_filt.py'

datadir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/'
blast=$datadir'rvac_trinity.blast'
transcriptome=$datadir'trinity2/Trinity.fasta'
coverage='50' #default: 50
identity='75' #default: 75
taxon='Amoebozoa'

$filt_script -i $blast -d $datadir -nt $transcriptome -q $coverage -p $identity -g $taxon

# -i: --infile
# -d: --work_dir
# -nt: --fasta_nt
# -q: --qcov_threshold
# -p: --pident_threshold
# -g: --good_groups
# -t: --test_mode
