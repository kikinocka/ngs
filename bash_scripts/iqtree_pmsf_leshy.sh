#!/bin/bash

cd /mnt/mokosz/home/kika/tvag/rab2-4-14/

for aln in *trimal_gt-0.8.aln ; do
	echo $aln
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	iqtree -m LG+F+G -nt AUTO -ntmax 10 -quiet -s ${aln} -pre $guide
	iqtree -m LG+C20+F+G -nt AUTO -ntmax 10 -bb $bb -nm $nm -quiet -s ${aln} -ft $guide_tree
done

source ~/.profile
python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE PMSF done