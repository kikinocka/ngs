#!/bin/bash

data='/mnt/mokosz/home/kika/pelomyxa_schiedti/trees/pnt/ver3/'

cd $data
for aln in *.aln ; do
	echo $aln
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	iqtree -m LG+F+G -nt AUTO -ntmax 20 -quiet -s ${aln} -pre $guide
	iqtree -m LG+C20+F+G -nt AUTO -ntmax 20 -bb $bb -quiet -s ${aln} -ft $guide_tree
done
