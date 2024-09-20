#!/bin/sh
#PBS -N mrbayes2
#PBS -l select=1:ncpus=4:mem=15gb:scratch_local=1gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add parallel
module add mrbayes-3.2.7a

data='/storage/brno12-cerit/home/kika/trafficking/mantamonas/rabs/ver3/mrbayes'

#copy files to scratch
cp $data'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

aln='rabs.CD.trimal_gt-0.8.nex'

# ls $aln | parallel -j $PBS_NUM_PPN 'echo Start > {}.log && date >> {}.log && mb {} | \
# 	tee -a {}.log && echo End: >> {}.log && date >> {}.log'
mpirun -n $PBS_NUM_PPN mb-mpi $aln


#copy files back
rm $aln
cp -R * $data
