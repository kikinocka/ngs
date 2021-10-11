#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/')
proteins = SeqIO.parse('pelomyxa_predicted_proteins_corr.fa', 'fasta')

#beta-barrel
motif = r'[KRHSTNQ]\w{1}G[AC]\w{1}[LIVFMWY]\w{1}[LIVFMWY]'

with open('pelo.beta-barrel.fa', 'w') as out:
	for protein in proteins:
		if re.search(motif, str(protein.seq)):
			match = re.search(motif, str(protein.seq))
			out.write('>{}__motif:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		else:
			print(protein.description, '_____no beta-barrel signal')
