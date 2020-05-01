#!/bin/bash

cd /storage/brno3-cerit/home/kika/prototheca/zopfii/

files=*trimmed*.fq.gz

for file in $files; do
	echo $file
	new=${file_trimmed%_\d.fq.gz}._renamed
	echo $new
done	
# sed -E 's/(@.*)\/([[:digit:]]).*/\1_\2/' SRR8447029_1.fastq > SRR8447029_renamed_1.fastq
# SRR8447029_trimmed_1.fq.gz 

# for f in *.mafft.aln ; do
#  aln=${f%.mafft.aln}.trimal_0.5.aln
