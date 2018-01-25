#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/blobtools/lhes2/')
fasta = SeqIO.parse('/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/lhes2_PRJNA284294_trinity.fasta', 'fasta')
blob = open('blobDB.table.txt', 'r')
diamond = open('lhes2.diamond_out', 'r')
lygus = open('lygus2.fa', 'w')
blasto = open('bexlh2.fa', 'w')
blasto_strict = open('bexlh2_strict.fa', 'w')
table = open('bexlh2_table.tsv', 'w')
rhiz = open('rhizarian2.fa', 'w')

taxonomy = {}
for line in blob:
	try:
		name = line.split('\t')[0]
		group = line.split('\t')[5]
		taxonomy[name] = group
	except:
		pass

diamond_dict = {}
for line in diamond:
	name = line.split('\t')[0]
	taxid = line.split('\t')[1]
	diamond_dict[name] = taxid

taxlist = [929439, 679716, 435258, 420245, 353153, 347515, 185431, 157538, 71804, 5679, 5661]

for contig in fasta:
	if contig.name in taxonomy.keys():
		if taxonomy[contig.name] == 'Arthropoda':
			lygus.write('>{}\n{}\n'.format(contig.description, contig.seq))
		elif taxonomy[contig.name] == 'Eukaryota-undef':
			blasto.write('>{}\n{}\n'.format(contig.description, contig.seq))
			if contig.name in diamond_dict.keys():
				table.write('{}\t{}\n'.format(contig.name, diamond_dict[contig.name]))
				if int(diamond_dict[contig.name]) in taxlist:
					blasto_strict.write('>{}\n{}\n'.format(contig.description, contig.seq))
		elif taxonomy[contig.name] == 'no-hit':
			rhiz.write('>{}\n{}\n'.format(contig.description, contig.seq))
		else:
			pass

lygus.close()
blasto.close()
blasto_strict.close()
rhiz.close()