#!/bin/bash

workdir='/mnt/mokosz/home/kika/endolimax_nana/filtration2/enan_trinity_NT/'
fasta='enan_trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta
