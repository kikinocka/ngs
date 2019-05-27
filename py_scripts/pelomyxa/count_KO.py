#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/augustus_training_set/')
gff = open('pelo_final.corrected.gff')

ko_set = set()
for line in gff:
	ko = line.split('\t')[8].split('"')[1]
	ko_set.add(ko)

print(len(ko_set))
