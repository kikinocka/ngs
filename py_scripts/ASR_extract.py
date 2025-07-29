#!/usr/bin/python3
import os
import heapq

os.chdir('/Users/kika/ownCloud/membrane-trafficking/ARFs-ASR/Carpedi_Arf6_removed/ASR/')
states = 'combinedArfsRoot__Carpedi_Arf6_removed.phy.state'
ASR1 = 'Arf1-6_ASR1.fa'
ASR2 = 'Arf1-6_ASR2.fa'
probabilities1 = 'Arf1-6_ASR1_prob.tsv'
probabilities2 = 'Arf1-6_ASR2_prob.tsv'
node = '2'
primary = ''
secondary = ''
prob1 = []
prob2 = []
position = ''
aa_dict = {}

with open(states, 'r') as infile, open(ASR1, 'w') as out1, open(ASR2, 'w') as out2, open(probabilities1, 'w') as outp1, open(probabilities2, 'w') as outp2:
	for line in infile:
		line = line.strip()
		if line.startswith('Node\tSite'):
			count = 0
			for item in line.split('\t')[3:]:
				aa_dict[count] = item.split('_')[1]
				count += 1
		elif line.startswith('Node{}\t'.format(node)):
			aa = line.split('\t')[2]
			primary += aa
			probabilities = line.split('\t')[3:]
			largest_two = heapq.nlargest(2, probabilities)
			prob1.append(float(largest_two[0]))
			if float(largest_two[0]) >= 0.8:
				aa = line.split('\t')[2]
				p2 = float(largest_two[0])
			else:
				position = probabilities.index(largest_two[1])
				aa = aa_dict[position]
				p2 = float(largest_two[1])
			secondary += aa
			prob2.append(p2)
		else:
			pass

	out1.write('>{}__Node{}\n{}\n'.format(ASR1.split('.')[0], node, primary))
	out2.write('>{}__Node{}\n{}\n'.format(ASR2.split('.')[0], node, secondary))
	for item in prob1:
		outp1.write('{}\n'.format(item))
	for item in prob2:
		outp2.write('{}\n'.format(item))
