#!/bin/sh
#PBS -N raxml-eug
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add raxml-8.2.8

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/euglenozoa/'

#copy files to scratch
cp $data'euglenozoa_v9.trimal_gt-0.5.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

aln='euglenozoa_v9.trimal_gt-0.5.aln'
out='euglenozoa'

raxmlHPC-PTHREADS -m GTRCAT -p 12345 -N 3 -s $aln -n $out\1 -T $PBS_NUM_PPN
raxmlHPC-PTHREADS -m GTRCAT -p 12345 -b 12345 -N 100 -f d -s $aln -n $out\2 -T $PBS_NUM_PPN
raxmlHPC-PTHREADS -m GTRCAT -p 12345 -f b -t RAxML_bestTree.$out\1 -z RAxML_bootstrap.$out\2 -n $out\3 -T 1$PBS_NUM_PPN


#copy files back
rm $aln
cp -R * $data