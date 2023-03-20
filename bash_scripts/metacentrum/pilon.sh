#!/bin/bash
#PBS -N Pilon
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add openjdk-10

data_dir='/storage/brno3-cerit/home/kika/kinetoplastids/lmex_genome/ku80/'

#copy files to scratch
cp $data_dir'ku80_pilon9.fa' $SCRATCHDIR
cp $data_dir'bw2_mapping/pilon9/ku80_p9_bw2_sorted.bam' $SCRATCHDIR
cp $data_dir'bw2_mapping/pilon9/ku80_p9_bw2_sorted.bam.bai' $SCRATCHDIR

pilon='/storage/brno2/home/kika/tools/pilon-1.23.jar'
assembly='ku80_pilon9.fa'
bam='ku80_p9_bw2_sorted.bam'
index='ku80_p9_bw2_sorted.bam.bai'

#compute on scratch
cd $SCRATCHDIR
java -jar -Xmx20G $pilon --genome $assembly --bam $bam --threads $PBS_NUM_PPN

#copy results to your folder
rm $assembly $bam $index
cp -r * $data_dir
