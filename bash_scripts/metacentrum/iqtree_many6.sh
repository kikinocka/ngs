#!/bin/bash
#PBS -N IQT-many6
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
cp $data_dir'q2000669.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2000671.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000672.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000673.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2000674.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2000675.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2000676.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000677.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000690.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2000707.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


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
