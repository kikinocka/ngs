#!/bin/sh

f='/home/kika/ownCloud/SAGs/reassembly/EU1718_contigs.fa'
output='/home/kika/ownCloud/SAGs/reassembly/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-5.0.2/quast.py $f --glimmer --min-contig 500 --k-mer-stats --rna-finding --eukaryote -o $output -t 4
