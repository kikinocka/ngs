#!/bin/sh

f='/home/kika/ownCloud/mastigamoeba_balamuthi/mbal_genome.CBKX01.1.fa'
output='/home/kika/ownCloud/mastigamoeba_balamuthi/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
