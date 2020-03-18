#!/bin/bash
#PBS -N Pilon
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add openjdk-10

data_dir='/storage/brno3-cerit/home/kika/kinetoplastids/lmex_genome/ku70/'

#copy files to scratch
cp $data_dir'ku70_ra.fa' $SCRATCHDIR
cp $data_dir'bw2_mapping/ra/ku70_ra_bw2_sorted.bam' $SCRATCHDIR
cp $data_dir'bw2_mapping/ra/ku70_ra_bw2_sorted.bam.bai' $SCRATCHDIR

pilon='/storage/brno2/home/kika/tools/pilon-1.23.jar'
assembly='ku70_ra.fa'
bam='ku70_ra_bw2_sorted.bam'
index='ku70_ra_bw2_sorted.bam.bai'

#compute on scratch
cd $SCRATCHDIR
java -jar -Xmx20G $pilon --genome $assembly --bam $bam --threads $PBS_NUM_PPN

#copy results to your folder
rm $assembly $bam $index
cp -r * $data_dir
