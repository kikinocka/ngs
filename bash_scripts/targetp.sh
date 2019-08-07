#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/sulfate_activation/'
infile=$workdir'pelo_PAPase.fasta'
outfile=$workdir'pelo_PAPase_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
