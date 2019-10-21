#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/'
infile=$read_dir'testing_reads.fq'
out_dir='/media/4TB1/blastocrithidia/bexlh/trinity_testing_assembly/'

Trinity --seqType fq --single $infile --run_as_paired --output $out_dir --max_memory 100G --CPU 30
