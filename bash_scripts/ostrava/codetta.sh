#!/bin/bash

codetta='/home/users/kika/codetta/codetta.py'

cd '/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'
genome='Oeli_genome_final_masked.fa'

python3 $codetta $genome
