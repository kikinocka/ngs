#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/paratrypanosoma/')
contamination = open('contamination.txt', 'r')
contigs = SeqIO.parse('Paratrypanosoma_genome_final_PE_MP_Newbler_500bp_up.fa', 'fasta')
contigs_upd = open('paratryp_new.fa', 'w')

def get_coordinates(contamination):
	adaptors = {}
	for row in contamination:
		if ',' in row.split('\t')[2]:
			for item in row.split('\t')[2].split(','):
				beginning = int(item.split('..')[0])
				end = int(item.split('..')[1])
				whole = [beginning, end]
				if row.split('\t')[0] not in adaptors:
					adaptors[row.split('\t')[0]] = [whole]
				else:
					adaptors[row.split('\t')[0]].append(whole)
		else:
			beginning = int(row.split('\t')[2].split('..')[0])
			end = int(row.split('\t')[2].split('..')[1])
			whole = [beginning, end]
			adaptors[row.split('\t')[0]] = [whole]
	return adaptors
	# contig name : [[start, end], [start,end]]
	# 				   adaptor1		 adaptor2

adaptors = get_coordinates(contamination)
remove = ['contig06599', 'scaffold00124']

genome = OrderedDict()
for contig in contigs:
	for key, value in adaptors.items():
		if contig.description == key:
			if len(value) == 1:
				for i in value:
					if i[0] == 1:
						genome[key] = contig.seq[i[1]:]
					elif i[1] == len(contig.seq):
						genome[key] = contig.seq[:i[0]-1]
					else:
						genome[key + '_1'] = contig.seq[:(i[0]-1)]
						genome[key + '_2'] = contig.seq[i[1]:]
			else:
				if value[0][0] == 1 and value[-1][1] == len(contig.seq):
					genome[key] = contig.seq[value[0][1]:value[-1][0]-1]
				else:
					genome[key + '_1'] = contig.seq[:value[0][0]-1]
					c = 1
					while c <= len(value):
						try:
							genome[key + '_' + str(c+1)] = contig.seq[value[c-1][1]:value[c][0]-1]
						except IndexError:
							if value[-1][1] == len(contig.seq):
								pass
							else:
								genome[key + '_' + str(c+1)] = contig.seq[value[-1][1]:]
						c += 1
		elif contig.description in remove:
			pass
		else:
			if contig.description in genome:
				pass
			else:
				genome[contig.description] = contig.seq

for key, value in genome.items():
	if key + '_1' in genome:
		pass
	else:
	   contigs_upd.write('>{}\n{}\n'.format(key, value))

contigs_upd.close()