#!/bin/bash
#SBATCH --job-name=busco
#SBATCH --output=busco.out
#SBATCH --error=busco.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=5
#SBATCH --time=02:00:00
#SBATCH --export=ALL

# #activate in terminal, then run script, then deactivate
# conda activate BUSCO

cd '/home/users/kika/trimastix/'
mkdir BUSCO_summaries

for fasta in *.fasta; do
	echo $fasta
	# mode='proteins'
	# mode='genome'
	mode='transcriptome'
	
	lineage='eukaryota_odb12'
	base=${fasta%.fasta}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c 5
	cp $base'/short_summary.'*'.json' BUSCO_summaries

	# lineage='stramenopiles_odb12'
	# base=${fasta%.fasta}_$lineage
	# busco -i $fasta -l $lineage -o $base -m $mode -c 5
	# cp $base'/short_summary.'*'.json' BUSCO_summaries
done

busco --plot BUSCO_summaries --plot_percentages

# conda deactivate
