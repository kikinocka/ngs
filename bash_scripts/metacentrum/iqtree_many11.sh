#!/bin/bash
#PBS -N IQT-many11
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
cp $data_dir'q2000889.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000890.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000891.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000894.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000898.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000914.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2000915.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000916.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000918.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000922.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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
