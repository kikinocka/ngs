#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/workdir/')
# inacc = open('fasttree/q2002972.og_hmm.trimal_gt-0.8.filtered-50.fasttree.treefile')
# infasta = SeqIO.parse('red/q2002972.og_hmm.fa', 'fasta')
inacc_files = [x for x in os.listdir() if x.endswith('.treefile')]
inaln_files = [x for x in os.listdir() if x.endswith('.aln')]
infasta_files = [x for x in os.listdir() if x.endswith('.og_hmm.fa')]

# omitted = []
# for line in inacc:
# 	if 'color=#ff0000' in line:
# 		# print(line.split('[')[0].replace('\'', '').replace('\t', '').replace('eval_', 'eval-'))
# 		omitted.append(line.split('[')[0].replace('\'', '').replace('\t', '').replace('eval_', 'eval-'))

# c = 0
# with open('red/q2002972.og_hmm.final.fa', 'w') as result:
# 	for seq in infasta:
# 		if seq.description in omitted:
# 			c += 1
# 			print('{} in omitted list'.format(seq.description))
# 		else:
# 			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
# print(c)


for inacc in inacc_files:
	omitted = []
	accessions = []
	fname = inacc.split('.')[0]
	print(inacc)
	# print(fname)
	for line in open(inacc):
		if 'color=#ff0000' in line:
			# print(line.split('[')[0].replace('\'', '').replace('\t', ''))
			omitted.append(line.split('[')[0].replace('\'', '').replace('\t', ''))
	# print(len(omitted))

	for inaln in inaln_files:
		if fname in inaln:
			for seq in SeqIO.parse(inaln, 'fasta'):
				if seq.description in omitted:
					pass
				else:
					accessions.append(seq.description.replace('eval_', 'eval-'))
	# print(len(accessions))
	# print(accessions)

	with open('{}.og_hmm.final.fa'.format(fname), 'w') as result:
		for infasta in infasta_files:
			# print(infasta)
			if fname in infasta:
				# print(fname)
				for seq in SeqIO.parse(infasta, 'fasta'):
					if seq.description in accessions:
						# print(seq.description)
						result.write('>{}\n{}\n'.format(seq.description, seq.seq))
					else:
						pass
						# print(seq.description)

