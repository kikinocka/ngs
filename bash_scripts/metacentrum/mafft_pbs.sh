#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.453

data_dir='/storage/brno3-cerit/home/kika/trafficking/RABs/ver8/'

#copy files to scratch
cp $data_dir'rabs.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fa='rabs.fa'
aln=${fa%.fa}.mafft.aln
log=${fa%.fa}.mafft.log

mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${fa} > ${aln} 2> ${log}


#copy files back
rm *.fa
cp * $data_dir
