#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1601/transcripts/nad5/nad5_hits.txt'
outfile='/home/kika/MEGAsync/diplonema_mt/1601/transcripts/nad5/nad5_cap3.out'

$cap3 $infile > $outfile