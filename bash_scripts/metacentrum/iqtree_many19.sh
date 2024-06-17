#!/bin/bash
#PBS -N IQT-many19
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=10gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

data_dir='/storage/brno12-cerit/home/kika/metamonads/iqtree/'

#copy files to scratch
cp $data_dir'q2002144.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002151.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002158.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002159.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002167.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002174.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002175.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002176.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002181.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'q2002194.og_hmm.final.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	bb=1000
	nm=5000
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees --keep-ident
done

#copy files back
rm *.aln
cp * $data_dir
