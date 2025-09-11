#!/bin/sh
#PBS -N busco5
#PBS -q default
#PBS -l select=1:ncpus=5:mem=8gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37
conda activate busco

# #available datasets
# busco --list-datasets

assembly_dir='/storage/brno12-cerit/home/kika/Egr_2024'

#copy files to scratch
cp -r $assembly_dir'/BUSCO_summaries_eug' $SCRATCHDIR
cp -r $assembly_dir'/BUSCO_summaries_euk' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

# # mkdir BUSCO_summaries

# for fasta in *.fsa_nt; do
# 	echo $fasta
# 	# mode='proteins'
# 	# mode='genome'
# 	mode='transcriptome'
	
# 	lineage='eukaryota_odb10'
# 	base=${fasta%.fa}_$lineage
# 	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
# 	cp $base'/short_summary.specific.'$base'.txt' BUSCO_summaries

# 	lineage='euglenozoa_odb10'
# 	base=${fasta%.fa}_$lineage
# 	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
# 	cp $base'/short_summary.specific.'$base'.txt' BUSCO_summaries
# done

generate_plot.py -wd BUSCO_summaries_eug
generate_plot.py -wd BUSCO_summaries_euk


#copy files back
# rm *.fsa_nt
cp -r * $assembly_dir
