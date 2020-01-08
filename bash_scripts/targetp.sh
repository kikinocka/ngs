#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/'
infile=$workdir'pelo_others.fa'
outfile=$workdir'pelo_others.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
