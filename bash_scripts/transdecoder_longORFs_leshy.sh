#!/bin/bash

workdir='/mnt/mokosz/home/kika/endolimax_nana/enan_trinity_NT/'
fasta='enan_trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta
