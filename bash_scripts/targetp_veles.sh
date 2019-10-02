#!/bin/bash

targetp='/home/kika/tools/targetp-1.1/targetp'
workdir='/home/kika/pelomyxa_schiedti/predicted_proteins/'
infile=$workdir'test.fa'
outfile=$workdir'test.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
