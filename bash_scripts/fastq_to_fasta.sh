#!/bin/bash

input='/home/kika/el/el_reads.fastq'
output='/home/kika/el/el_reads.fasta'

fastq_to_fasta -n -i $input -o $output