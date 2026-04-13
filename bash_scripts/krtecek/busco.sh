#!/bin/bash
source activate BUSCO

cd '/home/users/kika/blastocystis/'
mkdir BUSCO_summaries

for fasta in *.faa; do
	echo $fasta
	mode='proteins'
	# mode='genome'
	# mode='transcriptome'
	
	# lineage='eukaryota_odb12'
	# base=${fasta%.faa}_$lineage
	# busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
	# cp $base'/short_summary.'*'.json' BUSCO_summaries

	lineage='stramenopiles_odb12'
	base=${fasta%.faa}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c 5
	cp $base'/short_summary.'*'.json' BUSCO_summaries
done

busco --plot BUSCO_summaries --plot_percentages

conda deactivate
