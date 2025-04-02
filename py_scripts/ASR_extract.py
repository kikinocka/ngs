#!/usr/bin/python3
import os
import heapq

os.chdir('/Users/kika/ownCloud/membrane-trafficking/clathrin/ASR_opisthokonta/ver5/asr/')
states = 'CHC_opisthokonta.man_trim.CD.aln.state'
ASR1 = 'CHC_opisthokonta_ASR1.fa'
ASR2 = 'CHC_opisthokonta_ASR2.fa'
node = '46'
primary = ''
secondary = ''
position = ''
aa_dict = {}

with open(states, 'r') as infile, open(ASR1, 'w') as out1, open(ASR2, 'w') as out2:
	for line in infile:
		line = line.strip()
		if line.startswith('Node\tSite'):
			count = 0
			for item in line.split('\t')[3:]:
				aa_dict[count] = item.split('_')[1]
				count += 1
		elif line.startswith('Node{}'.format(node)):
			aa = line.split('\t')[2]
			primary += aa
			probabilities = line.split('\t')[3:]
			largest_two = heapq.nlargest(2, probabilities)
			if float(largest_two[0]) >= 0.8:
				aa = line.split('\t')[2]
			else:
				position = probabilities.index(largest_two[1])
				aa = aa_dict[position]
			secondary += aa
		else:
			pass

	out1.write('>CHC_opisthokonta1__Node{}\n{}\n'.format(node, primary))
	out2.write('>CHC_opisthokonta2__Node{}\n{}\n'.format(node, secondary))
