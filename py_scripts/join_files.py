#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/metamonada/OGs/')
ogs = [x for x in os.listdir() if x.endswith('renamed.fa')]
hits = [x for x in os.listdir() if x.endswith('reduced.fa')]


for og in ogs:
	# print(file)
	# os.chdir('/Users/kika/ownCloud/metamonada/OGs/')
	for hit in hits:
		# print(file)
		# print(hit)
		if og.split('_')[0] == hit.split('.')[0]:
			print(og)
			print(hit)
			os.system('cat {} {} > {}.og_hmm.fa'.format(og, hit, og.split('_')[0]))



# for file in files:
# 	if '_aa.txt' in file:
# 		gene = file.split('_')[1]
# 		f = SeqIO.parse(file, 'fasta')
# 	out = '/home/kika/Dropbox/blasto_project/blastocrithidia/genes/cv_subunits/triat/p57_' + gene + '.txt'
# 	for protein in f:
# 		with open(out, 'w') as result:
# 			result.write('>{}_{}\n{}\n'.format(gene, protein.name, protein.seq))

# os.chdir('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/cv_subunits/triat/')
# os.system('cat *.txt > p57_input.txt')