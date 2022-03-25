#!/usr/bin/env python3
import os
from Bio import SeqIO

# os.chdir('/Users/kika/ownCloud/archamoebae/replisome/amoebae/alns_updated/')
# files = [x for x in os.listdir() if x.endswith('.aln')]

# with open('replisome.fa', 'w') as out:
# 	for file in files:
# 		print(file)
# 		file_name = file.split('_')[0]
# 		for seq in SeqIO.parse(file, 'fasta'):
# 			if 'Homo' in seq.name or 'Dictyostelium' in seq.name:
# 				pass
# 			else:
# 				out.write('>{}__{}\n{}\n'.format(file_name, seq.name, str(seq.seq).replace('-', '')))

os.chdir('/storage/brno3-cerit/home/kika/archamoebae/prot_assemblies_filtration-20220127/')
assembly = SeqIO.parse('rlib.trinity.NRfilt.faa', 'fasta')

with open('rlib.trinity.NRfilt_renamed.faa', 'w') as out:
	for seq in assembly:
		out.write('>rli_{}\n{}\n'.format(seq.description, seq.seq))
