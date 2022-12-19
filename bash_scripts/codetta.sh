#!/bin/bash

cd '/Users/kika/ownCloud/blasto_comparative/codetta/'

genome='/Users/kika/ownCloud/blasto_comparative/genomes/Braa_genome_final_masked.fa'
codetta_dir='/Users/kika/programs/codetta/'
codetta=$codetta_dir'codetta.py'

python3 $codetta $genome
