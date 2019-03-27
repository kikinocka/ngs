#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa/mito_proteins/import/tom-tim/hmm/'
infile=$workdir'pelo_Sam50_aa.fa'
outfile=$workdir'pelo_Sam50_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
