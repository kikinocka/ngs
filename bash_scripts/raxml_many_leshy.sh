#!/bin/bash

data='/mnt/mokosz/home/kika/archam_trees/raxml'
tmp='/tmp/kika/'

cp $data'/'*.aln $tmp
cd $tmp

for aln in *.aln; do
	echo $aln
	out=${aln%.trimal_gt-0.8.aln}

	#proteins
	raxmlHPC-PTHREADS-AVX  -m PROTGAMMALG4XF -f a -T 10 -x 123 -N 100 -p 12345 -s $aln -n $out

	# #18S
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -N 3 -s $aln -n $out\1 -T $PBS_NUM_PPN
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -b 12345 -N 100 -f d -s $aln -n $out\2 -T $PBS_NUM_PPN
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -f b -t RAxML_bestTree.$out\1 -z RAxML_bootstrap.$out\2 -n $out\3 -T 1$PBS_NUM_PPN
done

cp * $data

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py RAxML done