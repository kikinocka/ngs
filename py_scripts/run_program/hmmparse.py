#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/users/kika/schizosaccharomyces_japonicus/hmms/')
# files = [x for x in os.listdir() if x.endswith('.hmmsearch.tsv')]
files = [x for x in os.listdir() if x.startswith('donna1_Superclade0')]
db = SeqIO.parse('/home/users/kika/schizosaccharomyces_japonicus/donna1.Trinity_translated.fa', 'fasta')

seq_d = {}
for seq in db:
	seq_d[seq.name] = (seq.name, seq.seq)

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
	# if file.startswith('EP00360'):
	print(file)
	name = file.replace('.hmmsearch.tsv', '.hmm_hits.fa')
	with open(file) as infile:
		for line in infile:
			if not line.startswith('#'):
				seqname = line.split()[0]
				evalue = float(line.split()[4])
				# if seqname in written:
				# 	pass
				if evalue < 0.0001:
					#don't forget to delete previously generated files
					with open(name, 'a') as result:
						result.write('>{} eval:{}\n{}\n'.format(seq_d[seqname][0], evalue, seq_d[seqname][1]))
				# 	written.add(seqname)
				# 	multidomain.add(seqname)
				# elif seqname in multidomain: #several domains found in the same seq
				# 	result.write('>{}\n{}\n'.format(seqname, seq_d[seqname]))
				# 	written.add(seqname)
				# else:
				# 	multidomain.add(seqname)


