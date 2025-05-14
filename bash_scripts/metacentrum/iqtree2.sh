#!/bin/bash
#PBS -N IQT2
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/trafficking/clathrin/CLC/ver2/'

#copy files to scratch
cp $datadir'CLC_opisthokonta.man_trim.aln' $SCRATCHDIR
cp $datadir'spp_constr.tre' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='CLC_opisthokonta.man_trim.aln'
guide='guide_CLC_opist'
guide_tree=$guide'.treefile'
constr='spp_constr.tre'
bb=1000
nm=5000


iqtree -m LG+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
iqtree -m LG+C20+G4 -T $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree -g $constr --boot-trees
# 

# iqtree -m MFP --mset C20,C40,C60,LG4M,LG4X,LG+F+G,LG+C20+G,LG+C40+G,LG+C60+G,LG+PMSF+G \
# 	-T AUTO --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln

#copy files back
rm $aln $constr
cp * $datadir
