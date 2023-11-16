#!/bin/bash
#PBS -N FastTree
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=1gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load fasttree


data_dir='/storage/brno3-cerit/home/kika/metamonads/fasttree'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for aln in *.aln ; do
	echo $aln
	out=${aln%.aln}.fasttree.treefile
	fasttree $aln > $out
done

#copy files back
rm *.aln
cp * $data_dir
