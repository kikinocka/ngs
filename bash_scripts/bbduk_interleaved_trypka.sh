#!/bin/bash

infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_A2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_A2'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_A3.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_A3'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_B1.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_B1'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_B2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_B2'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_B3.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_B3'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_C1.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_C1'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_C2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_C2'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_C3.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_C3'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_sraA.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_sraA'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_sraB.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_sraB'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20


infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_sraC.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_sraC'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20