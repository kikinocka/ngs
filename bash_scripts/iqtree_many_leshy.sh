#!/bin/bash

cd /mnt/mokosz/home/kika/archam_trees/hydA/ver2/

for aln in *trimal_gt_0.8.aln ; do
	echo $aln
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	iqtree -m LG+F+G -nt AUTO -ntmax 10 -quiet -s ${aln} -pre $guide
	iqtree -m LG+C20+F+G -nt AUTO -ntmax 10 -bb $bb -quiet -s ${aln} -ft $guide_tree
done
