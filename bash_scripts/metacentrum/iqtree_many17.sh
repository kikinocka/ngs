#!/bin/bash
#PBS -N IQT-many17
#PBS -l select=1:ncpus=15:mem=5gb:scratch_local=10gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/metamonads/iqtree/'

#copy files to scratch
# cp $data_dir'/'*.aln $SCRATCHDIR
cp $data_dir'q2001110.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001114.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001119.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001120.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001123.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2001125.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001127.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001162.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001163.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001164.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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