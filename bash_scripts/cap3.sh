#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1601/transcripts/tadpole/cob/cob_hits.txt'
outfile='/home/kika/MEGAsync/diplonema_mt/1601/transcripts/tadpole/cob/cob_hits_cap3.out'

$cap3 $infile > $outfile