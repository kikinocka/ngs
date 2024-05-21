#!/bin/bash
#PBS -N IQT-many2
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
cp $data_dir'q2000398.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000417.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000418.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000438.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000465.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000492.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000493.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000496.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000507.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000523.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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
