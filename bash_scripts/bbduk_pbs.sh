#!/bin/bash
#PBS -N BBduk
#PBS -l select=1:ncpus=40:mem=50gb:scratch_local=50gb
#PBS -l walltime=1:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

# bbduk='/auto/brno2/home/kika/tools/bbmap/bbduk.sh'
adapt='/auto/brno2/home/kika/tools/bbmap/resources/adapters.fa'

read_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/genome/deep_hiseq/'
fw='p3_r1.fastq.gz'
rv='p3_r2.fastq.gz'

trimdir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/genome/deep_hiseq/'
name='p3'
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
