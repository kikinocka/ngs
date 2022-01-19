#!/bin/bash

workdir='/mnt/mokosz/home/kika/replisome/'
infile=$workdir'replisome_proteins.fa'
plant='pl'
non_plant='non-pl'

targetp -fasta $infile -org $non_plant -format short

