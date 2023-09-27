#!/bin/bash

data='/mnt/mokosz/home/kika/archam_trees/raxml'
tmp='/tmp/kika/'

cp $data'/transporters.CD.trimal_gt-0.8.aln' $tmp
cd $tmp

for aln in *.aln; do
	echo $aln
	out=${aln%.trimal_gt-0.8.aln}

	#proteins
	raxmlHPC-PTHREADS-AVX  -m PROTGAMMALG4XF -f a -T 20 -x 123 -N autoMRE_IGN -p 12345 -s $aln -n $out

	# #18S
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -N 3 -s $aln -n $out\1 -T $PBS_NUM_PPN
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -b 12345 -N 100 -f d -s $aln -n $out\2 -T $PBS_NUM_PPN
	# raxmlHPC-PTHREADS-AVX  -m GTRCAT -p 12345 -f b -t RAxML_bestTree.$out\1 -z RAxML_bootstrap.$out\2 -n $out\3 -T $PBS_NUM_PPN
done

mv * $data

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py RAxML many done
