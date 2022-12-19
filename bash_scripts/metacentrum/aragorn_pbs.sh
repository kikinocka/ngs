#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/pkgs/aragorn-1.2.38-h779adbc_4/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes'

#copy files to scratch
cp $data_dir'/Omod_genome_final_masked.fa' $SCRATCHDIR
cp $data_dir'/Oobo_genome_final_masked.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fa ; do
	#no secondary structures
	fout=${genome%.fa}.aragorn.fa
	$aragorn -t -fo -o $fout $genome
	
	#with secondary structures
	sout=${genome%.fa}.aragorn_structures.txt
	$aragorn -t -o $sout $genome
done


#copy files back
rm *masked.fa
cp * $data_dir
