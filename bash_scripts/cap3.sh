#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1618/transcripts/y6/y6_hits.txt'
outfile='/home/kika/MEGAsync/diplonema_mt/1618/transcripts/y6/y6_cap3.out'

$cap3 $infile > $outfile