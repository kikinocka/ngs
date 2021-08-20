#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=50:mem=200gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.453

data_dir='/storage/brno3-cerit/home/kika/databases/pr2db/4.14.0'

#copy files to scratch
cp $data_dir'/'*UTAX.cdhit98.fasta $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *.fasta ; do
	aln=${f%.fasta}.mafft.aln
	log=${f%.fasta}.mafft.log
	mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done


#copy files back
rm *.fasta
cp * $data_dir
