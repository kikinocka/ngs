#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/mycobacterium_smegmatis/')
proteins = SeqIO.parse('GCF_013349145.1_ASM1334914v1_protein.faa', 'fasta')

# #beta-barrel
motif = r'[KRHSTNQ]\w{1}G[AC]\w{1}[LIVFMWY]\w{1}[LIVFMWY]'

#clathrin-binding
# motif = r'L[LI][DEN][LF][DE]')
# motif = r'L[V/I/L/F/W/Y/M][N/Q/S/T][V/I/L/F/W/Y/M][DE]')
# motif = r'PWDLW'
# motif = r'LLDLL'

with open('GCF_013349145.beta-barrel.fa', 'w') as out:
	for protein in proteins:
		if re.search(motif, str(protein.seq)):
			match = re.search(motif, str(protein.seq))
			out.write('>{}__motif:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		else:
			print(protein.description, '_____no signal')
