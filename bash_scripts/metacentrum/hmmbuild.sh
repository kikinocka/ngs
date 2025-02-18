#!/bin/bash
#PBS -N hmmbuild
#PBS -l select=1:ncpus=10:mem=6gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer

data_dir='/storage/brno12-cerit/home/kika/kinetoplastids/angomonas/EAPs'

#copy files to scratch
cp $data_dir'/'*.mafft.aln $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for msa in *.aln ; do
	echo $msa
	name=${msa%mafft.aln}
	hmm=${msa%.mafft.aln}.hmm
	summary=${msa%.mafft.aln}.hmmbuild.log
	hmmbuild -n $name -o $summary --amino --cpu $PBS_NUM_PPN $hmm $msa
done

#copy files back
rm *.mafft.aln
cp *hmm* $data_dir
