#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/storage/brno3-cerit/home/kika/databases/pr2db/4.14.0/')
db = SeqIO.parse('pr2_version_4.14.0_SSU_UTAX.fasta', 'fasta')

with open('pr2_version_4.14.0_SSU_UTAX.longer1000.fasta', 'w') as update:
	for seq in db:
		print(seq.name)
		if len(seq.seq) < 1000:
			pass
		else:
			update.write('>{}\n{}\n'.format(seq.description, seq.seq))
