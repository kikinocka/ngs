#!/bin/bash
#PBS -N bbduk
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load bbmap

read_dir='/storage/brno12-cerit/home/kika/pkld/'

#copy data to scratch
cp $read_dir'raw_reads/'*.fastq.gz $SCRATCHDIR
cp '/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/bbmap-39.01-d3jpcp7p3t2k2qcc2bdkaze4h5njwe5s/bin/resources/adapters.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

adapt='adapters.fa'

#illumina pair-end reads
for file in *_R1.fastq.gz ; do 
	name=${file%_*.fastq.gz}
	fw=$name'_R1.fastq.gz'
	rv=$name'_R2.fastq.gz'
	trimmed_fw=$name'_trimmed_1.fq.gz'
	trimmed_rv=$name'_trimmed_2.fq.gz'
	report=$name'_bbduk_report.txt'

	bbduk.sh overwrite=true \
		in1=$fw in2=$rv \
		out1=$trimmed_fw out2=$trimmed_rv \
		ref=$adapt \
		minlength=75 qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN 2> $report
done

# #illumina single reads
# bbduk.sh overwrite=true \
# 	in=$single \
# 	out=$trimmed \
# 	ref=$adapt \
# 	ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$PBS_NUM_PPN qtrim=rl trimq=20 2> $report
# 	# qtrim=rl trimq=20 ktrim=r t=$PBS_NUM_PPN 2> $report

# #454 reads
# for file in *fastq.gz; do
# 	bbduk.sh in=$file out=${file%.fastq.gz}_trimmed.fq.gz ref=$adapt \
# 	ktrim=r k=23 mink=11 edist=1 qtrim=rl trimq=20 t=$PBS_NUM_PPN 2> ${file%.fastq.gz}_bbduk_report.txt
# done

#copy files back
# rm $fw $rv $adapt
# rm $single $adapt
rm *fastq.gz $adapt
cp -r * $read_dir'trimmed_75'
