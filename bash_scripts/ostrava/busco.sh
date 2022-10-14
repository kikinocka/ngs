#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N busco
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00


workdir='/mnt/data/kika/blastocrithidia/o_eliasi/genome_final/'
mode='genome'

cd $workdir
mkdir BUSCO_summaries_$lineage

for fasta in *.fasta; do
	echo $fasta
	lineage='eukaryota_odb10'
	base=${fasta}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c 5
	cp $base'/short_summary.specific.'$lineage'.'$base'.txt' BUSCO_summaries_$lineage

	lineage='euglenozoa_odb10'
	base=${fasta}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c 5
	cp $base'/short_summary.specific.'$lineage'.'$base'.txt' BUSCO_summaries_$lineage
done

generate_plot.py -wd BUSCO_summaries_$lineage
