#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema_mt/transcripts/')

genes = ['atp6', 'cob', 'cox1', 'cox2', 'cox3', 'nad1', 'nad4', 'nad5', 'nad7', 'nad8', 'y1', 'y2', 'y3', 'y5', 'y6']

for gene in genes:
	da = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/Da_17_transcripts_translations.fasta', 'fasta')
	dp = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/Dp_17_transcripts_translations.fasta', 'fasta')
	ds = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/Ds_17_transcripts_translations.fasta', 'fasta')
	re = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/Re_17_transcripts_translations.fasta', 'fasta')
	print(gene)
	with open('{}.fa'.format(gene), 'w') as file:
		for contig in da:
			if gene in contig.description:
				print(contig.description)
				file.write('>{}\n{}\n'.format(contig.description, contig.seq))
		for contig in dp:
			if gene in contig.description:
				print(contig.description)
				file.write('>{}\n{}\n'.format(contig.description, contig.seq))
		for contig in ds:
			if gene in contig.description:
				print(contig.description)
				file.write('>{}\n{}\n'.format(contig.description, contig.seq))
		for contig in re:
			if gene in contig.description:
				print(contig.description)
				file.write('>{}\n{}\n'.format(contig.description, contig.seq))
