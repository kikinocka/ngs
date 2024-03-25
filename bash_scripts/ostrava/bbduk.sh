#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00

bbduk='/home/users/kika/bbmap/bbduk.sh'
adapt='/home/users/kika/bbmap/resources/adapters.fa'

cd '/home/users/kika/schizosaccharomyces_japonicus/reads/'

for file in *_1.fastq.gz ; do 
	name=${file%_*.fastq.gz}
	fw=$name'_1.fastq.gz'
	rv=$name'_2.fastq.gz'
	trimmed_name=${file%_R*.fastq.gz}
	trimmed_fw=$trimed_name'_trimmed_1.fq.gz'
	trimmed_rv=$trimed_name'_trimmed_2.fq.gz'
	report=$trimmed_name'_bbduk_report.txt'

	#illumina reads
	$bbduk overwrite=true \
		in1=$fw in2=$rv \
		out1=$trimmed_fw out2=$trimmed_rv \
		ref=$adapt \
		usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report

	echo $name 'trimmed'

done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py OSU: bbduk done
