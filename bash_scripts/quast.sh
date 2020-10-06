#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/archamoebae/mastigamoeba_balamuthi/'
assembly='mastiga_genome_v5.1.fasta'
output='/quast/'

python $quast --eukaryote -o $output -t 4 $assembly
