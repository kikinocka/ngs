#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/p57/mtDNA/'

#copy files to scratch
cp $data_dir'Bnon_mtDNA.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fa ; do
	echo $genome
	
	#no secondary structures
	fout=${genome%.fa}.aragorn_mtRNA.fa
	$aragorn -mt -fo -o $fout $genome
	
	#with secondary structures
	sout=${genome%.fa}.aragorn_structures_mtRNA.txt
	$aragorn -mt -o $sout $genome
done


#copy files back
rm *.fa
cp * $data_dir
