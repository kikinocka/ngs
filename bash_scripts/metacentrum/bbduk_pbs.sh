#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add bbmap-36.92

adapt='/storage/brno2/home/kika/tools/bbmap/resources/adapters.fa'

read_dir='/storage/brno3-cerit/home/kika/kinetoplastids/lguy_genome/reads/'
fw=$read_dir'SRR8179913_1.fastq.gz'
rv=$read_dir'SRR8179913_2.fastq.gz'

#copy data to scratch
cp $adapt $SCRATCHDIR
cp $fw $rv $SCRATCHDIR

name='SRR8179913_'
trimmed_fw=$name'trimmed_1.fq.gz'
trimmed_rv=$name'trimmed_2.fq.gz'
report=$name'bbduk_report.txt'


#compute on scratch
cd $SCRATCHDIR
bbduk.sh overwrite=true \
	in1=$fw in2=$rv \
	out1=$trimmed_fw out2=$trimmed_rv \
	ref=$adapt \
	usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report

#copy files back
rm $fw $rv $adapt
cp -r * $read_dir
