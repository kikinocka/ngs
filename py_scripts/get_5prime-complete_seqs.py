#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/transcriptome_assembly/')
proteins = SeqIO.parse('pelomyxa_transcriptome_clean.fa.transdecoder.pep', 'fasta')

with open('pelomyxa_transcriptome_clean.fa.transdecoder.5prime_complete.pep', 'w') as output:
	for protein in proteins:
		if '5prime' in protein.description:
			print(protein.description)
		elif 'internal' in protein.description:
			print(protein.description)
		else:
			output.write('>{}\n{}\n'.format(protein.description, protein.seq))
