#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=15gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.313

data_dir='/storage/brno3-cerit/home/kika/sags/alignments'

#copy files to scratch
cp $data_dir'/'*.faa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *.faa ; do
 aln=${f%.faa}.mafft.aln
 mafft --thread $PBS_NUM_PPN --maxiterate 100 --inputorder --auto ${f} > ${aln}
done


#copy files back
cp *.mafft.aln $data_dir
