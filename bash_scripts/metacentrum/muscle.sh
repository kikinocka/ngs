#!/bin/bash
#PBS -N muscle
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

muscle='/storage/brno3-cerit/home/kika/miniconda3/bin/muscle'
datadir='/storage/brno3-cerit/home/kika/blasto_comparative/orthofinder/all_species/'

#copy files to scratch
cp $datadir'OGs_fasta/more/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for fasta in *.fa; do
	echo $fasta
	aln=${fasta%.fa}.muscle.aln
	log=${fasta%.fa}.muscle.log

	# #short alns
	# $muscle -threads $PBS_NUM_PPN -align $fasta -output $aln 2> $log
	
	#long alns
	$muscle -threads $PBS_NUM_PPN -super5 $fasta -output $aln 2> $log
done

#copy files back
rm *.fa
cp * $datadir'OGs_muscle'