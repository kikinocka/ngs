#!/bin/bash

blob='/home/kika/tools/blobtools/blobtools'
fasta='/media/4TB1/blastocrithidia/bexlh/lhes2_PRJNA284294_trinity/Trinity.fasta'
bam='/media/4TB1/blastocrithidia/mapping/lhes2_bowtie2_RNA/lhes2_bw2_sorted.bam'
blast='/media/4TB1/blastocrithidia/kika_workdir/lhes2_new.diamond_out'
out='/media/4TB1/blastocrithidia/kika_workdir/lhes2_new/'
input=$out'blobDB.json'

$blob create -i $fasta -b $bam -t $blast -o $out
$blob view -i $input -o $out
$blob plot -i $input -o $out