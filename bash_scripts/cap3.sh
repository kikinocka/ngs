#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1608/transcripts/y3/y3_hits.txt'
outfile='/home/kika/MEGAsync/diplonema_mt/1608/transcripts/y3/y3_cap3.out'

$cap3 $infile > $outfile