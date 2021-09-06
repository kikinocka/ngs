#!/bin/sh

cd '/mnt/mokosz/home/kika/pelomyxa_schiedti/trees/vdac/'

for f in *.fa ; do
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	mafft --thread 15 --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done
