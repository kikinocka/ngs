#!/bin/bash

codetta='/home/users/kika/codetta/codetta.py'

cd '/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'
genome='p57_polished.fa'

python3 $codetta $genome
