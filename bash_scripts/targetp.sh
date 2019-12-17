#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/MEGAsync/diplonema/paramylon/'
infile=$workdir'euglenozoa.fa'
outfile=$workdir'euglenozoa.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
