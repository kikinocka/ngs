#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/UGA_decoding/condy_sp/'

#copy files to scratch
cp $data_dir'spades/scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fasta ; do
	echo $genome
	
	#no secondary structures
	fout=${genome%.fasta}.aragorn_mtRNA.fa
	$aragorn -fo -o $fout $genome
	
	#with secondary structures
	sout=${genome%.fasta}.aragorn_structures_mtRNA.txt
	$aragorn -o $sout $genome
done


#copy files back
rm *.fasta
cp * $data_dir
