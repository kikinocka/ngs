#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/Euglena_gracilis/compartments_markers/')
proteins = SeqIO.parse('EG_peroxy.fa', 'fasta')

#kinetoplastids - from Fred
pts1 = r'(S|A|G|C|N|P)(R|H|K|S|N|Q)(L|I|V|F|A|M|Y)'
pts2 = r'^M\w{1,10}(R|K)(L|V|I)\w{5}(H|Q)(L|A|I)'
mito = r'^M(R|H|K|F|L)\w{0,1}(R|H|K|S|T)\w{1,10}(S|T|R|K)'

# #kinetoplastids
# pts1 = r'(S|A|G|C|N|P)(R|H|K|N|Q)(L|I|V|F|A|M|Y)'
# pts2 = r'^M\w{0,20}(R|K)(L|V|I)\w{5}(H|K|Q|R)(L|A|I|V|F|Y)'

# #mastigamoeba very relaxed
# files = [x for x in os.listdir() if x.endswith('.fa')]
# pts1 = r'(S|A|C|H|K|N|P|T)(K|R|H|N|Q|S)(L|I|M|F|A|V|Y)'

# #general
# pts1 = r'(S|A|C)(K|R|H|Q)(L|M)'
# pts2 = r'^\w{1,21}R(L|I|V|Q)\w{2}(L|I|V|Q|H)(L|S|G|A)\w{1}(H|Q)(L|A)'

with open('EG_peroxy.possibly_peroxisomal_kineto-Fred.fa', 'w') as out:
	for protein in proteins:
		if str(protein.seq)[-1:] == '*':
			protein.seq = str(protein.seq)[:-1]
		if re.search(pts1, str(protein.seq)[-3:]):
			out.write('>{} @PTS1:{}\n{}\n'.format(protein.description, protein.seq[-3:], protein.seq))
		elif re.search(pts2, str(protein.seq)):
			match = re.search(pts2, str(protein.seq))
			out.write('>{} @PTS2:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		elif re.search(mito, str(protein.seq)):
			match = re.search(mito, str(protein.seq))
			out.write('>{} @mito:{}\n{}\n'.format(protein.description, match.group(), protein.seq))
		else:
			print(protein.description, '_____no PTS or mito signal')


# #mastigamoeba
# with open('ends_pts1_strict.tsv', 'w') as out:
# 	for file in files:
# 		print(file)
# 		fname = file.split('.')[0]
# 		out.write('{}\t'.format(fname))
# 		for protein in SeqIO.parse(file, 'fasta'):
# 			if re.search(pts1, str(protein.seq)[-3:]):
# 				out.write('{}\t{}\t'.format(protein.description, str(protein.seq)[-3:]))
# 			else:
# 				out.write('{}\t---\t'.format(protein.description))
# 				print(protein.description, '_____no PTS1 signal')
# 		out.write('\n')
