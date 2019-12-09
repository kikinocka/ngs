#!/usr/bin/env python3
import os
import subprocess
from Bio import SeqIO

mitoprot='/home/kika/programs/mitoprotII/mitoprot'
os.chdir('/home/kika/MEGAsync/diplonema/metabolism/')
infile = SeqIO.parse('diplo_all.fa', 'fasta')

with open('diplo_all.mitoprot.txt', 'a') as out:
	for seq in infile:
		print(seq.description)
		subprocess.call('{} -o {} {}'.format(mitoprot, out, seq.seq), shell=True)
