#!/bin/bash
#PBS -N trimal
#PBS -l select=1:ncpus=1:mem=15gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trimal-1.4

data_dir='/storage/brno3-cerit/home/kika/sags/alignments'

#copy files to scratch
cp $data_dir'/'*.mafft.aln $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *.mafft.aln ; do
 aln=${f%.mafft.aln}.trimal_0.5.aln
 option=0.5
 trimal -in ${f} -out ${aln} -gt ${option} -fasta
done


#copy files back
cp *.trimal_0.5.aln $data_dir
