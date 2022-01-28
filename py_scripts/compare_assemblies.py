#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/rhizomastix_vacuolata/')
old = SeqIO.parse('trinity-filt2/rvac.trinity.NRfilt-p70.faa', 'fasta')
new = SeqIO.parse('filtration-20220127/rvac.trinity.NRfilt.faa', 'fasta')

old_d = {}
for seq in old:
	old_d[seq.name] = seq.seq

with open('rlib.added.fa', 'w') as added:
	for seq in new:
		if seq.name not in old_d.keys():
			added.write('>{}\n{}\n'.format(seq.description, seq.seq))
			# print(seq.name)
		else:
			pass


# new_d = {}
# for seq in new:
# 	new_d[seq.name] = seq.seq

# with open('rvac.removed.fa', 'w') as removed:
# 	for seq in old:
# 		if seq.name not in new_d.keys():
# 			removed.write('>{}\n{}\n'.format(seq.description, seq.seq))
# 			# print(seq.name)
# 		else:
# 			pass

