#!/bin/bash
#PBS -N IQT-many10
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
cp $data_dir'q2000856.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000861.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000879.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000880.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000881.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000882.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000883.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000884.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000885.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000886.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	guide=guide_${f%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --tree-freq $guide_tree --boot-trees

done

#copy files back
rm *.aln
cp * $data_dir
