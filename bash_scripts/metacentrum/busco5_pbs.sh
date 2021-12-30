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

assembly_dir='/storage/brno3-cerit/home/kika/p57/predicted_proteins/'

#copy files to scratch
cp $assembly_dir'annotation_peptides.fasta' $SCRATCHDIR

assemblies='*.fasta'
mode='proteins'
lineage='eukaryota_odb10'

#compute on scratch
cd $SCRATCHDIR

for fasta in $assemblies; do
	echo $fasta
	base=${fasta%.fasta}_eukaryota_odb10
	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
done

#copy files back
cp -r * $assembly_dir
