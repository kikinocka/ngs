#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/')
files = [x for x in os.listdir() if x.endswith('.hmm_search.table')]
db = SeqIO.parse('/Users/kika/ownCloud/data/dpapilatum/dpap_genome_translated.fa', 'fasta')

alltables = set()
for file in files:
	data = open(file).read().split()
	for item in data:
		alltables.add(item)

seq_d = {}
for seq in db:
	if seq.name in alltables:
		seq_d[seq.name] = seq.seq

# #get first hit only
# for file in files:
# 	print(file)
# 	name = file.replace('.hmm_search.table', '.hmm_hits.fa')
# 	with open(file) as infile, open(name, 'w') as result:
# 		for i, line in enumerate(infile):
# 			if i == 3:
# 				if not line.startswith('#'):
# 					seqname = line.split()[0]
# 					protein = name.split('_')[1].split('.')[0]
# 					result.write('>{} {}\n{}\n'.format(seqname, protein, seq_d[seqname]))

#get all hits above certain threshold
multidomain = set()
written = set() #move multidomain, written into the for loop to have domain-specific files
for file in files:
	print(file)
	name = file.replace('.hmm_search.table', '.hmm_hits.fa')
	with open(file) as infile, open(name, 'w') as result:
		for line in infile:
			if not line.startswith('#'):
				data = line.split()
				seqname = data[0]
				evalue = float(data[4])
				if seqname in written:				
					pass
				elif evalue < 0.0001:
					result.write('>{}\n{}\n'.format(seqname, seq_d[seqname]))
					written.add(seqname)
					multidomain.add(seqname)
				elif seqname in multidomain: #several domains found in the same seq
					result.write('>{}\n{}\n'.format(seqname, seq_d[seqname]))
					written.add(seqname)
				else:
					multidomain.add(seqname)
