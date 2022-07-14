#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.453

data_dir='/storage/brno3-cerit/home/kika/trafficking/wdr/ver2'

#copy files to scratch
cp $data_dir'/'*fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *fa ; do
	aln=${f%.fa}.mafft.aln
	log=${f%.fa}.mafft.log
	mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${f} > ${aln} 2> ${log}
done


#copy files back
rm *fa
cp * $data_dir
