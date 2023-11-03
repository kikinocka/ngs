#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/Users/kika/ownCloud/archamoebae/ncbi_submission/')
contamination = open('mab_to_trim.txt').read().split('\n')
contigs = SeqIO.parse('mabd.trinity_forNCBI.l200_trimmed.fa', 'fasta')
contigs_upd = open('mabd.trinity_forNCBI.l200_trimmed2.fa', 'w')

def get_coordinates(contamination):
	to_trim = {}
	for row in contamination:
		# print(row)
		if ',' in row.split('\t')[2]:
			for item in row.split('\t')[2].split(','):
				beginning = int(item.split('..')[0])
				end = int(item.split('..')[1])
				whole = [beginning, end]
				if row.split('\t')[0] not in to_trim:
					to_trim[row.split('\t')[0]] = [whole]
				else:
					to_trim[row.split('\t')[0]].append(whole)
		else:
			beginning = int(row.split('\t')[2].split('..')[0])
			end = int(row.split('\t')[2].split('..')[1])
			whole = [beginning, end]
			to_trim[row.split('\t')[0]] = [whole]
	return to_trim
	# contig name : [[start, end], [start,end]]
	# 				   adaptor1		 adaptor2

to_trim = get_coordinates(contamination)
remove = []
# print(to_trim)

print('Removing to_trim')
genome = OrderedDict()
for contig in contigs:
	if contig.name in remove:
		pass
	else:
		if contig.name in to_trim.keys():
			key = contig.name
			value = to_trim[key]
			if len(value) == 1:
				for i in value:
					if i[0] == 1:
						genome[key] = contig.seq[i[1]:]
					elif i[1] == len(contig.seq):
						genome[key] = contig.seq[:i[0]-1]
					else:
						key = contig.description
						genome[key + '_1'] = contig.seq[:i[0]-1]
						genome[key + '_2'] = contig.seq[i[1]:]
			else:
				if value[0][0] == 1 and value[1][1] == len(contig.seq):
					genome[key] = contig.seq[value[0][1]:value[1][0]-1]
				else:
					print(key)
		else:
			genome[contig.description] = contig.seq

print('Writing contigs to file')
for key, value in genome.items():
	if len(value) > 199:
		contigs_upd.write('>{}\n{}\n'.format(key, value))

contigs_upd.close()
