#!/usr/bin/python3
import os
from Bio import SeqIO

fasta = SeqIO.parse('/home/kika/MEGAsync/blasto_project/reference_tryps_proteoms/TriTrypDB-35_TbruceiTREU927_AnnotatedProteins_2.fasta', 'fasta')
out = open('/home/kika/MEGAsync/blasto_project/reference_tryps_proteoms/TriTrypDB-35_TbruceiTREU927_AnnotatedProteins_3.fasta', 'w')

for contig in fasta:
	contig.seq = str(contig.seq).replace('-', '')
	out.write('>{}\n{}\n'.format(contig.description, contig.seq))
out.close