#!/bin/sh

#align denovo
cd '/mnt/mokosz/home/kika/archam_trees/tom60/ver2'

for f in *.fa ; do
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	mafft --thread 10 --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT done


# #merge alignments
# cd '/mnt/mokosz/home/kika/workdir/'

# aln1='ciliates_ref.mafft.aln'
# aln2='V9_above99.mafft.aln'
# # fasta='outgroup_nogaps.fa'
# input='ciliates_V9_above99.in'
# table='ciliates_V9_above99.table'
# out='ciliates_V9_above99.mafft.aln'
# log='ciliates_V9_above99.mafft.log'

# cat $aln1 $aln2 > $input
# # cat $aln1 $fasta > $input
# echo 'Alignments concatenated'
# makemergetable $aln1 $aln2 > $table
# # makemergetable $aln1 > $table
# echo 'Table prepared'
# mafft --thread 10 --localpair --maxiterate 1000 --merge $table $input > $out 2> $log
# echo 'Alignments merged'

# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT merge done
