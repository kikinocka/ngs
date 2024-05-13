#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_fasta/')
# inacc = open('arfs.mb+raxml_renamed.tre')
# infasta = SeqIO.parse('arfs.mafft.aln', 'fasta')
inacc_files = [x for x in os.listdir() if x.endswith('.treefile')]
infasta_files = [x for x in os.listdir() if x.endswith('.og_hmm.fa')]
inaln_files = [x for x in os.listdir() if x.endswith('.aln')]

# omitted = []
# for line in inacc:
# 	if 'color=' in line:
# 		# print(line.split('[')[0].replace('\'', '').replace('\t', ''))
# 		omitted.append(line.split('[')[0].replace('\'', '').replace('\t', ''))

# c = 0
# with open('arfs_reduced.mafft.aln', 'w') as result:
# 	for seq in infasta:
# 		if seq.description in omitted:
# 			c += 1
# 			print('{} in omitted list'.format(seq.description))
# 		else:
# 			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
# print(c)


omitted = []
accessions = []
for inacc in inacc_files:
	fname = inacc.split('.')[0]
	print(inacc)
	# print(fname)
	for line in open(inacc):
		if 'color=#ff0000' in line:
			# print(line.split('[')[0].replace('\'', '').replace('\t', ''))
			omitted.append(line.split('[')[0].replace('\'', '').replace('\t', ''))
	# print(omitted)

	for inaln in inaln_files:
		if fname in inaln:
			for seq in SeqIO.parse(inaln, 'fasta'):
				if seq.description in omitted:
					pass
				else:
					accessions.append(seq.description)
	# print(accessions)

	with open('{}.og_hmm.final.fa'.format(fname), 'w') as result:
		for infasta in infasta_files:
			# print(infasta)
			if fname in infasta:
				# print(fname)
				for seq in SeqIO.parse(infasta, 'fasta'):
					if seq.description in accessions:
						result.write('>{}\n{}\n'.format(seq.description, seq.seq))
					else:
						# print(seq.description)
						pass

