#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/pkgs/aragorn-1.2.38-h779adbc_4/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/gln-tRNA'

#copy files to scratch
cp $data_dir'/'*.fna $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fna ; do
	#no secondary structures
	fout=${genome%.fna}.aragorn.fa
	$aragorn -t -fo -o $fout $genome
	
	#with secondary structures
	sout=${genome%.fna}.aragorn_structures.txt
	$aragorn -t -o $sout $genome
done


#copy files back
rm *.fna
cp * $data_dir
