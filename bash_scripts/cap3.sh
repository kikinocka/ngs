#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1608/transcripts/rnl/rnl_hits.txt'
outfile='/home/kika/MEGAsync/diplonema_mt/1608/transcripts/rnl/rnl_cap3.out'

$cap3 $infile > $outfile