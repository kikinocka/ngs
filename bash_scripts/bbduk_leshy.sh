#!/bin/bash

bbduk='/mnt/mokosz/home/kika/tools/bbmap/bbduk.sh'
adapt='/mnt/mokosz/home/kika/tools/bbmap/resources/adapters.fa'

cd '/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM/reads/'

for file in *_1.fastq.gz ; do 
	name=${file%_*.fastq.gz}
	fw=$name'_1.fastq.gz'
	rv=$name'_2.fastq.gz'
	trimmed_fw=$name'_trimmed_1.fq.gz'
	trimmed_rv=$name'_trimmed_2.fq.gz'
	report=$name'_bbduk_report.txt'

	#illumina reads
	$bbduk overwrite=true \
		in1=$fw in2=$rv \
		out1=$trimmed_fw out2=$trimmed_rv \
		ref=$adapt \
		usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report

	echo $name 'trimmed'

done
