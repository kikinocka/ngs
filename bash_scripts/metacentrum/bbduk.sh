#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load bbmap


read_dir='/storage/brno12-cerit/home/kika/paratrimastix/RNA_reads/'

#copy data to scratch
cp $read_dir'SRR33713718_'*'.fastq.gz' $SCRATCHDIR
cp '/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/bbmap-39.01-d3jpcp7p3t2k2qcc2bdkaze4h5njwe5s/bin/resources/adapters.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

adapt='adapters.fa'
name='SRR33713718'
fw='SRR33713718_1.fastq.gz'
rv='SRR33713718_2.fastq.gz'
trimmed_fw=$name'_trimmed_1.fq.gz'
trimmed_rv=$name'_trimmed_2.fq.gz'
# single='all_RNA.fq.gz'
# trimmed='all_RNA_trimmed.fq.gz'
report=$name'_bbduk_report.txt'

#illumina pair-end reads
bbduk.sh overwrite=true \
	in1=$fw in2=$rv \
	out1=$trimmed_fw out2=$trimmed_rv \
	ref=$adapt \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report

# #illumina single reads
# bbduk.sh overwrite=true \
# 	in=$single \
# 	out=$trimmed \
# 	ref=$adapt \
# 	ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN qtrim=rl trimq=20 2> $report
# 	# qtrim=rl trimq=20 ktrim=r t=$PBS_NUM_PPN 2> $report

# #454 reads
# bbduk.sh in=$fw out=$trimmed_fw ref=$adapt k=23 ktrim=r mink=11 edist=1 qtrim=rl trimq=20 t=$PBS_NUM_PPN 2> $report

#copy files back
rm $fw $rv $adapt
# rm $single $adapt
cp -r * $read_dir
