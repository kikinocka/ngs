#!/bin/sh

#align denovo
# cd '/mnt/mokosz/home/kika/archam_trees/'

# for f in *.fa ; do
# 	aln=${f%.fa}.mafft.aln
# 	log=${f%.fa}.mafft.log
# 	mafft --thread 10 --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
# done

# source ~/.profile
# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT done


#merge alignments
cd '/mnt/mokosz/home/kika/workdir/'

maketable='/mnt/mokosz/home/kika/miniconda3/bin/makemergetable.rb'
aln1='ciliophora_eukref.aln'
aln2='V9_above99.mafft.aln'
input='ciliates_V9.in'
table='ciliates_V9.table'
out='ciliates_V9_above99.mafft.aln'
log='ciliates_V9_above99.mafft.log'

cat $aln1 $aln2 > $input
echo 'Alignments concatenated'
ruby $maketable $aln1 $aln2 > $table
echo 'Table prepared'
mafft --thread 10 --localpair --maxiterate 1000 --merge $table $in > $out 2> $log
echo 'Alignments merged'

source ~/.profile
python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT merge done
