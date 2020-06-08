#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add bbmap-36.92


read_dir='/storage/brno3-cerit/home/kika/kinetoplastids/lpyr_genome/reads/454/'

#copy data to scratch
cp '/storage/brno2/home/kika/tools/bbmap/resources/adapters.fa' $SCRATCHDIR
cp $read_dir'454_all.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

adapt='adapters.fa'
name='454_all'
fw=$name'.fq.gz'
# rv=$name'2.fastq.gz'
trimmed_fw=$name'_trimmed_20.fq.gz'
# trimmed_rv=$name'trimmed_2.fq.gz'
report=$name'_bbduk_report.txt'

# bbduk.sh overwrite=true \
# 	in1=$fw in2=$rv \
# 	out1=$trimmed_fw out2=$trimmed_rv \
# 	ref=$adapt \
# 	usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report

bbduk.sh in=$fw out=$trimmed_fw ref=$adapt k=23 ktrim=r mink=11 edist=1 qtrim=rl trimq=20 t=$PBS_NUM_PPN 2> $report

#copy files back
rm $fw $adapt
cp -r * $read_dir
