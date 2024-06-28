#!/bin/bash
#PBS -N IQT-many4
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=10gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

data_dir='/storage/brno12-cerit/home/kika/metamonads/iqtree/'

#copy files to scratch
cp $data_dir'q2004791.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004827.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004838.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004851.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004855.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004884.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004920.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004943.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004965.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2004981.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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
