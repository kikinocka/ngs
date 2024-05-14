#!/bin/sh
#PBS -N mrbayes
#PBS -l select=1:ncpus=4:mem=3gb:scratch_local=1gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add parallel
module add mrbayes-3.2.7a

data='/storage/brno12-cerit/home/kika/trafficking/diplonemids_all/ARFs/ph-arf/ver2/mrbayes'

#copy files to scratch
cp $data'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

aln='arfs_reduced.CD.trimal_gt-0.8.nex'

# ls $aln | parallel -j $PBS_NUM_PPN 'echo Start > {}.log && date >> {}.log && mb {} | \
# 	tee -a {}.log && echo End: >> {}.log && date >> {}.log'
mpirun -n $PBS_NUM_PPN mb-mpi $aln


#copy files back
rm $aln
cp -R * $data
