#!/bin/sh
targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa/mito_proteins/import/'
infile=$workdir'pelo_MPP_aa.fa'
outfile=$workdir'pelo_MPP_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
