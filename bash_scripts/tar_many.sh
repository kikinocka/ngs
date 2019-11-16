#!/bin/bash

datadir='/storage/brno3-cerit/home/kika/ncbi_db_preformatted/'
files=$datadir'.tar.gz'

for file in files; do
	echo 'Extracting ' $file
	tar -xvzf $file
	echo $file ' extracted'
	echo '-------------'
	echo
done
