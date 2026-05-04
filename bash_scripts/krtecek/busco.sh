#!/bin/bash
#SBATCH --job-name=busco
#SBATCH --output=busco.%j.out
#SBATCH --error=busco.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=5
#SBATCH --time=02:00:00
#SBATCH --export=ALL
export OMP_NUM_THREADS=$CPU_count

source activate BUSCO

cd '/home/users/kika/trimastix/'
mkdir BUSCO_summaries

for fasta in *.fasta; do
	echo $fasta
	mode='proteins'
	# mode='genome'
	# mode='transcriptome'
	
	lineage='eukaryota_odb12'
	base=${fasta%.fasta}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c $CPU_count
	cp $base'/short_summary.'*'.json' BUSCO_summaries

	# lineage='stramenopiles_odb12'
	# base=${fasta%.fasta}_$lineage
	# busco -i $fasta -l $lineage -o $base -m $mode -c $CPU_count
	# cp $base'/short_summary.'*'.json' BUSCO_summaries
done

busco --plot BUSCO_summaries --plot_percentages

conda deactivate
