#!/bin/bash
#PBS -N mafft-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load mafft

data_dir='/storage/brno12-cerit/home/kika/membrane-trafficking/tset_haptophytes'

#copy files to scratch
cp $data_dir'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *fa ; do
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
	# mafft --thread $PBS_NUM_PPN --auto --inputorder ${f} > ${aln} 2> ${log}
done


#copy files back
rm *fa
cp * $data_dir
