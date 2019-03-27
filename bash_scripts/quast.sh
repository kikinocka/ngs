#!/bin/sh

f='/home/kika/ownCloud/blastocrithidia/genome_assembly/p57_ra_untrimmed.fa'
output='/home/kika/ownCloud/blastocrithidia/genome_assembly/quast/p57_ra_untrimmed/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 1
