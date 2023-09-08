#!/bin/sh

#align denovo
cd '/mnt/mokosz/home/kika/workdir/'

for f in *.fa ; do
	echo $f
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	# mafft --thread 15 --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
	mafft --thread 15 --auto --inputorder ${f} > ${aln} 2> ${log}
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT done


# #add to aligned sequences
# cd '/mnt/mokosz/home/kika/workdir/'

# existing='ciliates.mafft.aln'
# add='v9.fa'
# out='ciliates_v9.mafft.aln'
# log='ciliates_v9.mafft.log'
# # mafft --add ${add} --thread 10 --inputorder ${existing} > ${out} 2> ${log}
# mafft --addfragments ${add} --thread 10 --inputorder ${existing} > ${out} 2> ${log}

# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT add done


# #merge alignments
# cd '/mnt/mokosz/home/kika/workdir/'

# aln1='euglenozoa_V9_above99.mafft.aln'
# aln2='sags.mafft.aln'
# # fasta='outgroup_nogaps.fa'
# input='euglenozoa_sags_V9_above99.in'
# table='euglenozoa_sags_V9_above99.table'
# out='euglenozoa_sags_V9_above99.mafft.aln'
# log='euglenozoa_sags_V9_above99.mafft.log'

# cat $aln1 $aln2 > $input
# # cat $aln1 $fasta > $input
# echo 'Alignments concatenated'
# makemergetable $aln1 $aln2 > $table
# # makemergetable $aln1 > $table
# echo 'Table prepared'
# mafft --thread 10 --localpair --maxiterate 1000 --merge $table $input > $out 2> $log
# echo 'Alignments merged'

# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT merge done
