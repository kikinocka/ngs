#!/bin/bash

codetta='/Users/kika/programs/codetta/codetta.py'

cd '/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'
genome='Btri_genome_final_masked.fa'

python3 $codetta $genome
