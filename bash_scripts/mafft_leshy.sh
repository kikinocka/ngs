#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/'

for f in *.fa ; do
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	mafft --thread 5 --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done

source ~/.profile
python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT done
