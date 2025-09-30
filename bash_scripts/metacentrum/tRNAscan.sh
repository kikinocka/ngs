#!/bin/bash
#PBS -N tRNAscan
#PBS -l select=1:ncpus=10:mem=1gb:scratch_local=5gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

tRNAscan='/storage/brno12-cerit/home/kika/miniconda3/bin/tRNAscan-SE'
data_dir='/storage/brno12-cerit/home/kika/tRNA-aaRS/'

#copy files to scratch
# cp $data_dir'/'*_genome.fna $SCRATCHDIR
cp $data_dir'Bsty_genome.fna' $SCRATCHDIR
cp $data_dir'Clep_genome.fna' $SCRATCHDIR
cp $data_dir'Dhan_genome.fna' $SCRATCHDIR
cp $data_dir'Hsap_genome.fna' $SCRATCHDIR
cp $data_dir'Pmar_genome.fna' $SCRATCHDIR
cp $data_dir'Ptan_genome.fna' $SCRATCHDIR
cp $data_dir'Scer_genome.fna' $SCRATCHDIR
cp $data_dir'Tmin_genome.fna' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for genome in *.fna ; do
	echo $genome

	table=${genome%.fna}.tRNAscan_table.tsv
	seq=${genome%.fna}.tRNAscan.fa
	structures=${genome%.fna}.tRNAscan_structures.txt

	#eukaryotic tRNAs
	$tRNAscan --thread $PBS_NUM_PPN -E -o $table -a $seq -f $structures $genome

	# #bacterial tRNAs
	# $tRNAscan --thread $PBS_NUM_PPN -B -o $table -a $seq -f $structures $genome
done


#copy files back
rm *.fna
cp * $data_dir
