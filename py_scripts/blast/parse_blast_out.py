#!/usr/bin/env python3
import os
from Bio import SeqIO

# os.chdir('/Users/kika/ownCloud/anaeramoeba/RABs/')
# btable = open('Tvag_rev.RABdb.best_blast.tsv')
# out = 'Tvag_rev.acc'
# rabs = ['Rab', 'IFT', 'Ran', 'RAN', 'RTW', 'Ypt']

# with open(out, 'w') as result:
# 	for line in btable:
# 		qseqid = line.split('\t')[0]
# 		sseqid = line.split('\t')[2]
# 		if any(x in sseqid for x in rabs):
# 			# print(qseqid, sseqid)
# 			result.write('{}\n'.format(qseqid))
# 		else:
# 			print(qseqid, sseqid)

os.chdir('/Users/kika/Downloads/')
blast = open('Tbruc_CDS.pep.best_blast.tsv')
genome = SeqIO.parse('TriTrypDB-68_TbruceiTREU927_AnnotatedCDSs.fasta', 'fasta')

contig_dir = {}
for line in blast:
	if line.startswith('qseqid'):
		pass
	else:
		peptide = line.strip().split('\t')[0]
		if line.strip().split('\t')[2] == '***no hit found***':
			pass
		else:
			contig = line.strip().split('\t')[3]
			frame = int(line.strip().split('\t')[6])
			mismatch = int(line.strip().split('\t')[11])
			start = int(line.strip().split('\t')[15])
			end = int(line.strip().split('\t')[16])
			aln_len = int(float(line.strip().split('\t')[17]))
			# if mismatch == 0:
			# 	if aln_len == 1:
			# 		contig_dir[peptide] = (contig, start, end, frame)
			contig_dir[peptide] = (contig, start, end, frame)

with open('peptides-CDS_seqs.fa', 'w') as out:
	for seq in genome:
		for key, value in contig_dir.items():
			if value[0] in seq.name:
				# print(key, value)
				header = value[0] + ':' + str(value[1]) + '-' + str(value[2]) + '__' + key
				if value[3] in (1,2,3):
					sequence = seq.seq[value[1]-1:value[2]]
					out.write('>{}\n{}\n'.format(header, sequence))
				else:
					sequence = seq.seq[value[2]-1:value[1]].reverse_complement()
					out.write('>{}\n{}\n'.format(header, sequence))
