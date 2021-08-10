#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/NR_filt.py'

datadir='/mnt/mokosz/home/kika/endolimax_nana/'
outdir=$datadir'filtration3b_NR-amoebozoa/'
diamond=$datadir'filtration2/enan_NR/enan.trinity.NTfilt.dmnd.out'
transcriptome=$datadir'filtration3a_NR-only_eukaryota/enan_NR/enan.trinity.NRfilt.fna'
proteins=$datadir'filtration3a_NR-only_eukaryota/enan_NR/enan.trinity.NRfilt.faa'
coverage='70' #default: 50
identity='90' #default: 75
taxon='Amoebozoa'

cd $outdir
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
