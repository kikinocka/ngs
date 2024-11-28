#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/transcriptomes/')
genome = SeqIO.parse('Ovol_cufflinks.fa', 'fasta')

with open('ncbi_submission/Ovol_cufflinks.l200.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 200:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
