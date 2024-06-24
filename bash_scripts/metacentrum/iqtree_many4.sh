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
cp $data_dir'q2003663.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003664.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003666.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003675.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003686.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003690.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003697.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003698.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003700.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2003702.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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
