#!/bin/bash

cd '/mnt/mokosz/home/kika/archam_trees/orc1-cdc6/'

for aln in *.aln ; do
	echo $aln
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	iqtree -m TEST -nt AUTO -ntmax 10 -bb $bb -nm $nm -quiet -s ${aln}
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE TEST done
