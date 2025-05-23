#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/metamonads/MRO_proteins/2again/')
# inacc = open('CAD2219389.trimal_gt-0.8.marked.treefile')
# infasta = SeqIO.parse('CAD2219389.fa', 'fasta')
inacc_files = [x for x in os.listdir() if x.endswith('.treefile')]
inaln_files = [x for x in os.listdir() if x.endswith('.aln')]
infasta_files = [x for x in os.listdir() if x.endswith('.fa')]

# omitted = []
# for line in inacc:
# 	if 'color=#ff0000' in line:
# 		# print(line.split('[')[0].replace('\'', '').replace('\t', '').replace('eval_', 'eval-'))
# 		omitted.append(line.split('[')[0].replace('\'', '').replace('\t', '').replace('eval_', 'eval-'))

# c = 0
# with open('CAD2219389_reduced.fa', 'w') as result:
# 	for seq in infasta:
# 		if seq.description in omitted:
# 			c += 1
# 			print('{} in omitted list'.format(seq.description))
# 			# result.write('>{}\n{}\n'.format(seq.description, str(seq.seq).replace('-','')))
# 		else:
# 			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
# 			# print('{} in omitted list'.format(seq.description))
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

	with open('{}.mro+hmm.final.fa'.format(fname), 'w') as result:
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

