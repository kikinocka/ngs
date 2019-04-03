#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/')
files = [x for x in os.listdir() if x.endswith('_replaced.indel')]
alignments = [x for x in os.listdir() if x.endswith('aln')]

for file in files:
	print(file)
	name = file.split('_')[0]
	locations = {}
	for line in open(file):
		if line.startswith('Indel location in alignment:'):
			loc = line.strip().split(': ')[1].split('-')
			if len(loc) == 1:
				loc.append(loc[0])
			if name not in locations:
				locations[name] = [loc]
			else:
				locations[name].append(loc)

for aln in alignments:
	print(aln)
	name = aln.split('.')[0]
	if name in locations.keys():
		location = locations[name]
		for seq in AlignIO.read(aln, 'fasta'):
			sp = seq.name.split('_')[0]
			print(sp)
			c = 0
			positions = []
			with open('ins_non-ins/{}_insertions.fa'.format(sp), 'w') as insertions:
				for item in location:
					c += 1
					start = int(item[0]) - 1
					end = int(item[1])
					pos = [start, end]
					ins = str(seq.seq[start:end]).replace('-', '')
					if ins != '':
						insertions.write('>{}_ins{}\n{}\n'.format(name, c, ins))
						positions.append(pos)
					else:
						pass
			
			with open('ins_non-ins/{}_not_insertions.fa'.format(sp), 'w') as not_ins:
				for i in range(len(positions)):
					while i < len(positions):
						if i == 0:
							start = 0
							end = positions[i][0]
							out = str(seq.seq[start:end]).replace('-', '')
							not_ins.write('>{}_{}\n{}\n'.format(name, i+1, out))
						elif i < len(positions):
							start = int(positions[i-1][1])
							end = int(positions[i][0])
							out = str(seq.seq[start:end]).replace('-', '')
							not_ins.write('>{}_{}\n{}\n'.format(name, i+1, out))
						i += 1
					else:
						break
				start = int(positions[-1][1])
				end = AlignIO.read(aln, 'fasta').get_alignment_length()
				out = str(seq.seq[start:end]).replace('-', '')
				not_ins.write('>{}_{}\n{}\n'.format(name, len(positions)+1, out))
	else:
		print(name)