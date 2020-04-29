#!/bin/bash

datasethandler='/mnt/mokosz/home/kika/scripts/py_scripts/datasethandler-server.py'

datadir='/mnt/mokosz/home/kika/pelomyxa_schiedti/trees/fdhA'

python3 $datasethandler \
	-d $datadir \
	-i batch \
	-a mafft \
	--trimalparams='-gt 0.5' \
	-t iqtree \
	-b \
	--maxcores 20

#'-d', '--directory', help='Change working directory', default='.'
#'-i', '--infile', help='Fasta/Phylip set to be analyzed', default="batch"
#'--maxcores', help='Maximum cores to use for multithreading', default=20
#'-a', '--aligner', help='Aligner', default='mafft'
#'-t', '--treemaker', help='Program for tree inference', default='iqtree'
#'-n', '--no_dedupe', help='Do not filter duplicates', action='store_true'
#'--alignerparams', help='Custom aligner parameters, check with manual', default=''
#'--trimalparams', help='Custom TrimAl parameters, check with manual', default=''
#'-b', '--ufbootstrap', help='Ultra-fast boostrap calculation', action='store_true'
#'-B', '--bootstrap', help='Boostrap calculation', action='store_true'
#'--shalrt', help='Calculate SH-aLRT', action='store_true'
#'-g', '--no_guide', help='Do not perform guide tree inference', action='store_true'
#'--treeparams', help='Custom tree inference parameters, check with manual', default=''
#'-s', '--mark_similarity', help='Mark similarity on branches', action='store_true'
