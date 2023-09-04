#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load bbmap


raw_dir='/storage/brno3-cerit/home/kika/UGA_decoding/peritromus/reads/'
# trim_dir='/storage/brno3-cerit/home/kika/archamoebae/rhizomastix_libera/trimmed_reads/'

#copy data to scratch
cp '/storage/brno2/home/kika/tools/bbmap/resources/adapters.fa' $SCRATCHDIR
cp $raw_dir'CRR626409_f1.fq.gz' $SCRATCHDIR
cp $raw_dir'CRR626409_r2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

adapt='adapters.fa'
name='pkah'
fw='CRR626409_f1.fq.gz'
rv='CRR626409_r2.fq.gz'
trimmed_fw=$name'_trimmed_1.fq.gz'
trimmed_rv=$name'_trimmed_2.fq.gz'
# single='all_reads.fq.gz'
# trimmed='all_reads_trimmed.fq.gz'
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
cp -r * $raw_dir
