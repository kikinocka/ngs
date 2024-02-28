#!/bin/bash

cd '/Users/kika/ownCloud/blasto_comparative/genomes/codetta/'

codetta='/Users/kika/programs/codetta/codetta.py'
genome='/Users/kika/ownCloud/blastocrithidia/genome_assembly/p57_polished.fa'

python3 $codetta $genome
