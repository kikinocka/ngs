#!/bin/sh

f='/home/kika/ownCloud/SAGs/reassembly/EU1718_contigs.fa'
output='/home/kika/ownCloud/SAGs/reassembly/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
