#!/bin/bash

workdir='/mnt/mokosz/home/kika/replisome/'
infile=$workdir'replisome_proteins.fa'
plant='P'
non_plant='N'

targetp -fasta $infile -org $non_plant -format short

