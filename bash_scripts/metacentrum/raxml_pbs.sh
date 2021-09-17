#!/bin/sh
#PBS -N raxml
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add raxml-8.2.8

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/metamonada/reference_tree/'

#copy files to scratch
cp $data'metamonads_eukref.trimal_gt-0.25_cons-50.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

aln='metamonads_eukref.trimal_gt-0.25_cons-50.aln'
out='metamonads_eukref.RAxML'

raxmlHPC-PTHREADS -f d -m GTRCATI -p 12345 -b 12345 -# 100 -s $aln -n $out -T $PBS_NUM_PPN 


#copy files back
rm $aln
cp -R * $data
