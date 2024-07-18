#!/bin/bash
#PBS -N IQT-many2
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=10gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

data_dir='/storage/brno12-cerit/home/kika/metamonads/iqtree/'

#copy files to scratch
cp $data_dir'q2001191.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2001348.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2001360.og_hmm.final.trimal_at1.aln' $SCRATCHDIR
cp $data_dir'q2001382.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2005791.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	bb=1000
	nm=5000
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees -keep-ident
done

#copy files back
rm *.aln
cp * $data_dir
