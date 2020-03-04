#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/Dcko/MEGAsync/diplonema/catalase/targeting/')
proteins = SeqIO.parse('all.fa', 'fasta')

#kinetoplastids
pts1 = r'(S|A|G|C|N|P)(R|H|K|N|Q)(L|I|V|F|A|M|Y)'
pts2 = r'^M\w{0,20}(R|K)(L|V|I)\w{5}(H|K|Q|R)(L|A|I|V|F|Y)'

# pts1 = r'(S|A|C)(K|R|H|Q)(L|M)'
# pts2 = r'^\w{1,21}R(L|I|V|Q)\w{2}(L|I|V|Q|H)(L|S|G|A)\w{1}(H|Q)(L|A)'

with open('all.possibly_peroxisomal.fa', 'w') as out:
	for protein in proteins:
		# print(protein.seq)
		# print(str(protein.seq)[-3:])
		# if str(protein.seq)[-3:] == pts1:
		if re.search(pts1, str(protein.seq)[-3:]):
			out.write('>{} @PTS1:{}\n{}\n'.format(protein.description, protein.seq[-3:], protein.seq))
		elif re.search(pts2, str(protein.seq)):
			# match = re.match(pts2, str(protein.seq))
			match = re.search(pts2, str(protein.seq))
			out.write('>{} @PTS2:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		else:
			print(protein.description, '_____no PTS signal')
