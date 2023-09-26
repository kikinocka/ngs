#!/bin/bash

cd /mnt/mokosz/home/kika/archam_trees/raxml/not_converged/

for bs in RAxML_bootstrap.*; do
	echo $bs
	out=$bs'.conv.txt'

	raxmlHPC-PTHREADS-AVX -m PROTGAMMALG4XF -p 12345 -z $bs -I autoMRE_IGN -n $out -T 10
done

mv *.conv.txt ./convergence

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py RAxML-convergence done
