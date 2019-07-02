#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/electron_transfer/'
infile=$workdir'pelo_MDH_aa.fa'
outfile=$workdir'pelo_MDH_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
