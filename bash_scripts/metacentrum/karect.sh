#!/bin/sh
#PBS -N karect
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=100gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module load fastqc

karect='/storage/brno12-cerit/home/kika/tools/karect/karect'
read_dir='/storage/brno12-cerit/home/kika/pkld/trimmed_all'

#copy data to scratch
cp $read_dir'/'*fq.gz $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

gzip -d *fq.gz

for file in *_1.fq ; do 
      name=${file%_*.fq}
      fw=$name'_1.fq'
      rv=$name'_2.fq'
      report=$name'_karect_report.txt'

      $karect -correct -threads=$PBS_NUM_PPN -matchtype=hamming -celltype=diploid \
            -inputfile=$fwd -inputfile=$rev 2> $report
done


#copy files back
cp -r * $read_dir
