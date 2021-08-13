#!/bin/bash

workdir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/filtration2/rvac_trinity_NT/'
fasta='rvac_trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta
