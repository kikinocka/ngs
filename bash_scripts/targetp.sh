#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/MEGAsync/diplonema/mt_metabolism/pyruvate_degradation/'
infile=$workdir'pyruvate_degradation.fasta'
outfile=$workdir'pyruvate_degradation.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
