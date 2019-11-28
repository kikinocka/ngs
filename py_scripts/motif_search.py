#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/Data/dpapilatum/')
proteins = SeqIO.parse('dpap_predicted_proteins.fa', 'fasta')

pts1 = r'(S|A|G|C|N|P)(R|H|K|N|Q)(L|I|V|F|A|M|Y)$'
pts2 = r'^M\w{0,20}(R|K)(L|V|I)\w{5}(H|K|Q|R)(L|A|I|V|F|Y)'

with open('dpap_peroxisomal.fa', 'w') as out:
	for protein in proteins:
		if re.search(pts1, str(protein.seq)):
			out.write('>{} @PTS1:{}\n{}\n'.format(protein.description, protein.seq[-3:], protein.seq))
		elif re.search(pts2, str(protein.seq)):
			match = re.match(pts2, str(protein.seq))
			out.write('>{} @PTS2:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		else:
			print(protein.description, '_____no PTS signal')
