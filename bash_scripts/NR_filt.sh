#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NR_filt.py'

datadir='/mnt/mokosz/home/kika/endolimax_nana/'
diamond=$datadir'filtration2/enan_NR/enan.trinity.NTfilt.dmnd.out'
transcriptome=$datadir'filtration2/enan_trinity_NT/enan_trinity.NTfilt.fasta'
proteins=$datadir'filtration2/enan_trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
coverage='50' #default: 50
identity='70' #default: 75
taxon='Eukaryota'

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
