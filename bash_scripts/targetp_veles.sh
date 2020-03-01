#!/bin/bash

workdir='/mnt/mokosz/home/kika/workdir/'
infile=$workdir'pelo_formate_transporter.fasta'
outfile=$workdir'pelo_formate_transporter.targetp.txt'
plant='P'
non_plant='N'

targetp -$non_plant -c $infile > $outfile
