#!/bin/sh
#PBS -N busco5
#PBS -q default
#PBS -l select=1:ncpus=5:mem=8gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mambaforge
conda activate busco

# #available datasets
# busco --list-datasets

assembly_dir='/storage/brno12-cerit/home/kika/blastocystis/braker/'

#copy files to scratch
cp $assembly_dir'braker.aa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mkdir BUSCO_summaries

for fasta in *.aa; do
	echo $fasta
	mode='proteins'
	# mode='genome'
	# mode='transcriptome'
	
	lineage='eukaryota_odb10'
	base=${fasta%.aa}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
	cp $base'/short_summary.'*'.txt' BUSCO_summaries

	lineage='stramenopiles_odb10'
	base=${fasta%.aa}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
	cp $base'/short_summary.'*'.txt' BUSCO_summaries
done

generate_plot.py -wd BUSCO_summaries
mamba deactivate


#copy files back
rm *.aa
cp -r * $assembly_dir && clean_scratch
