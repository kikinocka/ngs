#!/bin/bash

# targetp='/home/kika/programs/targetp-1.1/targetp'
targetp='/home/osboxes/programs/targetp-2.0/bin/targetp'
workdir='/Dcko/MEGAsync/diplonema/catalase/targeting/'
infile=$workdir'skompletovane.fa'
outfile=$workdir'skompletovane.targetp.tsv'

# plant='P'
# non_plant='N'
# $targetp -$non_plant -c $infile > $outfile

plant='pl'
non_plant='non-pl'
$targetp -fasta $infile -org $non_plant -format short -prefix $outfile
