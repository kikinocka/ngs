#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add bbmap-36.92


raw_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'
# trim_dir='/storage/brno3-cerit/home/kika/archamoebae/rhizomastix_libera/trimmed_reads/'

#copy data to scratch
cp '/storage/brno2/home/kika/tools/bbmap/resources/adapters.fa' $SCRATCHDIR
cp $raw_dir'P1B_S3_L001_R1_001.fastq.gz' $SCRATCHDIR
cp $raw_dir'P1B_S3_L001_R2_001.fastq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

adapt='adapters.fa'
name='P1B'
fw=$name'_S3_L001_R1_001.fastq.gz'
rv=$name'_S3_L001_R2_001.fastq.gz'
trimmed_fw=$name'_trimmed_1.fq.gz'
trimmed_rv=$name'_trimmed_2.fq.gz'
report=$name'_bbduk_report.txt'

#illumina reads
bbduk.sh overwrite=true \
	in1=$fw in2=$rv \
	out1=$trimmed_fw out2=$trimmed_rv \
	ref=$adapt \
	usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report

# #454 reads
# bbduk.sh in=$fw out=$trimmed_fw ref=$adapt k=23 ktrim=r mink=11 edist=1 qtrim=rl trimq=20 t=$PBS_NUM_PPN 2> $report

#copy files back
rm $fw $rv $adapt
cp -r * $raw_dir
