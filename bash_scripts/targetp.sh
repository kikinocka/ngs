#!/bin/sh
targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa/mito_proteins/pyruvate_metabolism/'
infile=$workdir'pelo_pyruvate_aa.fa'
outfile=$workdir'pelo_pyruvate_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
