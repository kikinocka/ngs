#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/UGA_decoding/uronychia'

#copy files to scratch
cp $data_dir'/'*.fna $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fna ; do
	echo $genome
	
	#no secondary structures
	fout=${genome%.fna}.aragorn_mtRNA.fa
	$aragorn -mt -fo -o $fout $genome
	
	#with secondary structures
	sout=${genome%.fna}.aragorn_structures_mtRNA.txt
	$aragorn -mt -o $sout $genome
done


#copy files back
rm *.fna
cp * $data_dir
