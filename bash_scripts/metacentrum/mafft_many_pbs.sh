#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.313

data_dir='/storage/brno3-cerit/home/kika/proteromonas/ACSL_tree/ver3'

#copy files to scratch
cp $data_dir'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *.fa ; do
 aln=${f%.fa}.mafft.aln
 mafft --thread $PBS_NUM_PPN --maxiterate 100 --inputorder --auto ${f} > ${aln}
done


#copy files back
cp *.mafft.aln $data_dir
