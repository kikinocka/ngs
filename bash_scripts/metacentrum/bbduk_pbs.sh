#!/bin/bash
#PBS -N BBduk
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

module add bbmap-36.92

adapt='/storage/brno2/home/kika/tools/bbmap/resources/adapters.fa'

read_dir='/storage/brno3-cerit/home/kika/lsey/'
fw='14II_1.fastq.gz'
rv='14II_2.fastq.gz'

# trimdir='/storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/'
name='14II'
trimmed_fw=$name'_trimmed_1.fq.gz'
trimmed_rv=$name'_trimmed_2.fq.gz'
report=$name"_report.txt"

#copy data to scratch
cd $read_dir
cp $adapt $SCRATCHDIR
cp $fw $rv $SCRATCHDIR

cd $SCRATCHDIR
bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report

cp $trimmed_fw $trimmed_rv $report $read_dir
