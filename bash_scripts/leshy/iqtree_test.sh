#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_gt-0.8/'

for aln in *.aln ; do
	echo $aln
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	# iqtree -m TEST -nt AUTO -ntmax 10 -bb $bb -nm $nm -quiet -s ${aln}
	iqtree -m LG+C20+G -nt AUTO -ntmax 10 -bb 1000 -nm 5000 -quiet -safe -s ${aln} -pre ${aln%.aln}

done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE TEST done
