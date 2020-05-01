#!/bin/bash

cd /storage/brno3-cerit/home/kika/prototheca/zopfii/

fw=*trimmed_1*.fq.gz
rv=*trimmed_2*.fq.gz

for file in $fw; do
	unzipped=${file%.gz}
	renamed_fq=${unzipped/trimmed_/trimmed_renamed_}.gz

	echo $file
	zcat $file | awk '{{print (NR%4 == 1) ? "@1_" ++i "/1": $0}}' | gzip -c > $renamed_fq
	echo 'Reads renamed:' $renamed_fq
	echo '==================================================='
done

for file in $fw; do
	unzipped=${file%.gz}
	renamed_fq=${unzipped/trimmed_/trimmed_renamed_}.gz

	echo $file
	zcat $file | awk '{{print (NR%4 == 1) ? "@1_" ++i "/2": $0}}' | gzip -c > $renamed_fq
	echo 'Reads renamed:' $renamed_fq
	echo '==================================================='
done
