#!/usr/bin/python3
from Bio import SeqIO

proteins = SeqIO.parse('/home/kika/MEGAsync/blasto_project/blast_searches/triat_transcriptome/triat_aa.fa', 'fasta')
out = open('/home/kika/MEGAsync/blasto_project/blast_searches/triat_transcriptome/triat_aa_SLremoved.fa', 'w')
sl1 = 'RIFCYSFCTLL'
sl2 = 'TNAFFVTVSVLY'
sl3 = 'LTHFLLQFLYFI'

prot_dict = {}
for protein in proteins:
	prot_dict[protein.description] = protein.seq

sl_dict = {}
for key, value in prot_dict.items():
	i = 0
	for letter in sl1:
		if value.startswith(sl1[i:]):
			sl_dict[key] = value[value.find('M'):]
		i += 1

	i = 0
	for letter in sl2:
		if value.startswith(sl2[i:]):
			sl_dict[key] = value[value.find('M'):]
		i += 1

	i = 0
	for letter in sl3:
		if value.startswith(sl3[i:]):
			sl_dict[key] = value[value.find('M'):]
		i += 1

for key, value in prot_dict.items():
	if key in sl_dict:
		out.write('>{}\n{}\n'.format(key, sl_dict[key]))
	else:
		out.write('>{}\n{}\n'.format(key, value))

out.close()