#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/MEGAsync/Data/dpapilatum/'
infile=$workdir'dpap_peroxisomal.fa'
outfile=$workdir'dpap_peroxisomal.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
