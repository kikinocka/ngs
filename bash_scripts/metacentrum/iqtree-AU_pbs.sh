#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-2.2.0

datadir='/storage/brno3-cerit/home/kika/trafficking/diplonemids_COPII/ver7/sec13_AU/ver5'

#copy files to scratch
cp $datadir'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
pref='sec13'
aln='sec13.trimal_gt-0.8.aln'
# trees='sec13_topologies.trees'
constr1='sec13.constr1'
constr2='sec13.constr2'

# iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN --test-weight --test-au --test 10000 -n 100 -s $aln --trees $trees
iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN -s $aln --prefix $pref.unconstr
iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN -s $aln -g $constr1 --prefix $pref.constr1
iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN -s $aln -g $constr2 --prefix $pref.constr2
cat *constr*.treefile > $pref.trees
iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN -s $aln -z $pref.trees --test-weight --test-au --test 10000 -n 0

#copy files back
rm $aln
cp * $datadir
