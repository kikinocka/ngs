#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NR_filt.py'

datadir='/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM1/'
diamond=$datadir'mab.trinity.NTfilt.dmnd.out'
transcriptome=$datadir'mab_trinity_NT/mab.trinity.NTfilt.fasta'
proteins=$datadir'mab_trinity_NT/mab.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
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

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py NR_filt done
