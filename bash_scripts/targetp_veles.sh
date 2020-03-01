#!/bin/bash

workdir='/mnt/mokosz/home/kika/workdir/'
infile=$workdir'pelo_formate.fasta'
outfile=$workdir'pelo_formate.clustered.targetp.txt'
plant='P'
non_plant='N'

targetp -$non_plant -c $infile > $outfile
