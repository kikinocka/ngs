#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NR_filt.py'

datadir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/filtration-NR_20220127/'
diamond=$datadir'rvac.trinity.NTfilt.dmnd.out'
transcriptome=$datadir'rvac_trinity.NTfilt.fasta'
proteins=$datadir'longest_orfs.pep'
coverage='50' #default: 50
identity='70' #default: 75
taxon='Amoebozoa'

$filt_script -i $diamond -d $datadir -nt $transcriptome -aa $proteins -q $coverage -p $identity -g $taxon

# -i: --infile
# -d: --work_dir
# -nt: --fasta_nt #NT filtered transcriptome
# -aa: --fasta_aa #proteins from NT filtered transcriptome
# -q: --qcov_threshold
# -p: --pident_threshold
# -s: --scaffold_coverage_threshold
# -g: --good_groups
# -t: --test_mode
# --genomic
