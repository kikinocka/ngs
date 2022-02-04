#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NT_filt.py'

datadir='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/'
blast=$datadir'mei_trinity.blast'
transcriptome=$datadir'Trinity_Mastigella_150316_renamed_nucl.fasta'
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

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py NT_filt done
