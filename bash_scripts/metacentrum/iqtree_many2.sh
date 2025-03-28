#!/bin/bash
#PBS -N IQT-many2
#PBS -l select=1:ncpus=15:mem=25gb:scratch_local=10gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

data_dir='/storage/brno12-cerit/home/kika/metamonads/MRO_proteins/iqtree/'

#copy files to scratch
cp $data_dir'CT.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'DnaJ.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'FBD.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'FDPA.mro+hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'Fdx.mro+hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'Fra.mro+hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'GCS-H.mro+hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'GCS-L.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'GCS-P.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'GCS-T.mro+hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	bb=1000
	nm=10000
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees
done

#copy files back
rm *.aln
cp * $data_dir
