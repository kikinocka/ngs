#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/MEGAsync/diplonema/mt_metabolism/tca_cycle/'
infile=$workdir'tca_cycle.fa'
outfile=$workdir'tca_cycle.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
