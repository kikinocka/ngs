#!/bin/sh
#PBS -N busco5
#PBS -q default
#PBS -l select=1:ncpus=4:mem=8gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37
conda activate busco

# #available datasets
# busco --list-datasets

assembly_dir='/storage/brno3-cerit/home/kika/eupelagonemids/assemblies/'

#copy files to scratch
cp $assembly_dir'*.pep' $SCRATCHDIR

assemblies='*.pep'
mode='proteins'
lineage='protist_odb10'


#compute on scratch
cd $SCRATCHDIR

mkdir BUSCO_summaries

for fasta in $assemblies; do
	echo $fasta
	base=${fasta%.fasta}_pep_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
	
	cp $base'/shortshort_summary.specific.'$lineage$base'.txt' BUSCO_summaries
done

generate_plot.py -wd BUSCO_summaries


#copy files back
rm $assemblies
cp -r * $assembly_dir
