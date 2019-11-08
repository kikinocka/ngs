#!/bin/sh

raw_dir='/home/kika/'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652
