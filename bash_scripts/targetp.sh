#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/sulfate_activation/'
infile=$workdir'pelo_SULTs.fasta'
outfile=$workdir'pelo_SULTs_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
