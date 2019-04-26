#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa/mito_proteins/pyruvate_metabolism/hyd_maturase/'
infile=$workdir'pelo_hyd_maturase.fa'
outfile=$workdir'pelo_hyd_maturase_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
