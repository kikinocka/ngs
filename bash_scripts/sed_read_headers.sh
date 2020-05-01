#!/bin/bash

cd /storage/brno3-cerit/home/kika/prototheca/zopfii/

files=*trimmed*.fq.gz

for file in $files; do
	echo $file
done	
# sed -E 's/(@.*)\/([[:digit:]]).*/\1_\2/' SRR8447029_1.fastq > SRR8447029_renamed_1.fastq
