#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/pkgs/aragorn-1.2.38-h779adbc_4/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/p57/'

#copy files to scratch
cp $data_dir'GC'*'/'*.fna $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fna ; do
	out=${genome%.fna}.aragorn_structures.txt
	# #no secondary structures
	# $aragorn -t -fo -o $out $genome
	
	#with secondary structures
	$aragorn -t -o $out $genome
done


#copy files back
rm *fna
cp * $data_dir
