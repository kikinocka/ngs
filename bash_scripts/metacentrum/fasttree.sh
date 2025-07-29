#!/bin/bash
#PBS -N FastTree
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load fasttree


data_dir='/storage/brno12-cerit/home/kika/metamonads/MRO_proteins'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for aln in *.aln ; do
	echo $aln
	out=${aln%.aln}.fasttree.treefile
	log=${aln%.aln}.fasttree.log
	fasttree -log $log -out $out $aln
	echo ''
done

#copy files back
rm *.aln
cp * $data_dir
