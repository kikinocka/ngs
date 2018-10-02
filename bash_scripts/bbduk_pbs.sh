#!/bin/bash
#PBS -N BBduk
#PBS -l select=1:ncpus=35:mem=50gb:scratch_local=50gb
#PBS -l walltime=0:20:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

adapt='/auto/brno2/home/kika/tools/bbmap/resources/adapters.fa'

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/preliminary_seq/'
fw='pelo2_s2_l001_r1_001.fastq.gz'
rv='pelo2_s2_l001_r2_001.fastq.gz'

trimdir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/preliminary_seq/'
name='pelo2_001'
trimmed_fw=$name'_trimmed_1.fq.gz'
trimmed_rv=$name'_trimmed_2.fq.gz'
report=$name"_report.txt"

module add bbmap-36.92 

#copy data to scratch
cd $read_dir
cp $adapt $SCRATCHDIR
cp $fw $rv $SCRATCHDIR

cd $SCRATCHDIR
bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=35 2> $report

cp $trimmed_fw $trimmed_rv $report $trimdir
