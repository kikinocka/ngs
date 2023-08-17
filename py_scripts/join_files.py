#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/hmmsearch/')

for subdir in os.walk():
	print(os.path.join(subdir))
# files = [x for x in os.listdir() if x.endswith('.hmmsearch.tsv')]


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