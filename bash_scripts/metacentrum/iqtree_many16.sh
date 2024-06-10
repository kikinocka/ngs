#!/bin/bash
#PBS -N IQT-many16
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=10gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/metamonads/iqtree/'

#copy files to scratch
cp $data_dir'q2001772.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2001773.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001774.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001777.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001778.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001779.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001784.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001785.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001786.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001787.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	bb=1000
	nm=5000
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees
done

#copy files back
rm *.aln
cp * $data_dir
