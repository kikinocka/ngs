#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NR_filt.py'

datadir='/mnt/mokosz/home/kika/endolimax_nana/'
diamond=$datadir'enan.trinity.NTfilt.dmnd.out'
transcriptome=$datadir'trinity_out_dir/Trinity.fasta'
proteins=$datadir'enan_trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
coverage='50' #default: 50
identity='70' #default: 75
taxon='Amoebozoa'

$filt_script -i $diamond -d $datadir -nt $transcriptome -aa $proteins -q $coverage -p $identity -g $taxon #--test_mode

# -i: --infile
# -d: --work_dir
# -nt: --fasta_nt
# -aa: --fasta_aa
# -q: --qcov_threshold
# -p: --pident_threshold
# -s: --scaffold_coverage_threshold
# -g: --good_groups
# -t: --test_mode
# --genomic
