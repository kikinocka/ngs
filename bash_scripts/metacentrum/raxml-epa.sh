#!/bin/sh
#PBS -N raxml-epa
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add raxml-8.2.8
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add raxml/8.2.12-gcc-10.2.1-nu7c3k5


data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/mesozoa/'

#copy files to scratch
cp $data'placement/mesozoa_V9.trimal_gt-0.25_cons-50.aln' $SCRATCHDIR
cp $data'ref_tree/RAxML_bipartitions.mesozoa3' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

aln='mesozoa_V9.trimal_gt-0.25_cons-50.aln'
tree='RAxML_bipartitions.mesozoa3'
out='EPARUN_mesozoa'

raxmlHPC-PTHREADS -f v -G 0.2 -m GTRCAT -n $out -s $aln -t $tree -T $PBS_NUM_PPN


#copy files back
rm $aln $tree
cp -R * $data'placement/'
