#!/bin/bash

workdir='/mnt/mokosz/home/kika/rhizomastix_reassembly/'
fasta='rhizomastix_reassembly.trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta
