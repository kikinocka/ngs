#!/usr/bin/python3
from Bio import SeqIO
from collections import OrderedDict

proteins = SeqIO.parse('/home/kika/MEGAsync/blasto_project/blast_searches/bexlh1/bexlh1_aa.fa', 'fasta')
out = open('/home/kika/MEGAsync/blasto_project/blast_searches/bexlh1/bexlh1_aa_SLremoved.fa', 'w')
sl1 = 'RIFCYSFCTLL'
sl2 = 'TNAFFVTVSVLY'
sl3 = 'LTHFLLQFLYFI'

prot_dict = OrderedDict()
for protein in proteins:
	i = 0
	for letter in sl1:
		if protein.seq.startswith(sl1[i:]):
			prot_dict[protein.description] = protein.seq[protein.seq.find('M'):]
		i += 1

	i = 0
	for letter in sl2:
		if protein.seq.startswith(sl2[i:]):
			prot_dict[protein.description] = protein.seq[protein.seq.find('M'):]
		i += 1

	i = 0
	for letter in sl3:
		if protein.seq.startswith(sl3[i:]):
			prot_dict[protein.description] = protein.seq[protein.seq.find('M'):]
		i += 1

proteins = SeqIO.parse('/home/kika/MEGAsync/blasto_project/blast_searches/bexlh1/bexlh1_aa.fa', 'fasta')
for protein in proteins:
	if protein.description in prot_dict:
		out.write('>{}\n{}\n'.format(protein.description, prot_dict[protein.description]))
	else:
		out.write('>{}\n{}\n'.format(protein.description, protein.seq))

out.close()