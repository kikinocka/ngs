#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa/mito_proteins/chaperones/'
infile=$workdir'pelo_chaperones_aa.fa'
outfile=$workdir'pelo_chaperones_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
