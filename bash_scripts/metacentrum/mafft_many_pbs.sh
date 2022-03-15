#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.453

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/decontaminated/stramenopiles/placement'

#copy files to scratch
cp $data_dir'/'*fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *fa ; do
	aln=${f%.fasta}.mafft.aln
	log=${f%.fasta}.mafft.log
	mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done


#copy files back
rm *fa
cp * $data_dir
