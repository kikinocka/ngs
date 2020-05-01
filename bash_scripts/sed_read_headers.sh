#!/bin/bash

cd /storage/brno3-cerit/home/kika/prototheca/zopfii/

files=*trimmed*.fq.gz

for file in $files; do
	unzipped=${file%.gz}
	renamed_fq=${unzipped/trimmed_/trimmed_renamed_}

	echo 'Unzipping ' $file
	gzip -k -d $file

	echo 'Replacing "/" by "_" in ' $unzipped
	sed -E 's/(@.*)\/([[:digit:]]).*/\1_\2/' $unzipped > $renamed_fq
	
	echo 'Zipping ' $renamed_fq
	gzip $renamed_fq

	echo 'Removing ' $unzipped
	rm $unzipped
done
