#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/')
blast = open('stops/check_genuine_stop/Braa_genome.fwd_Bnon.best_blast.tsv')
assembly = SeqIO.parse('genomes/FINAL/Braa_genome_final_corrected2_masked.fa', 'fasta')
# result = 'stops/check_genuine_stop/Braa_genuine_stops.tsv'

genome = {}
for seq in assembly:
	genome[seq.name] = seq.seq

stop_codons = {}
for line in blast:
	try:
		qlen = line.split('\t')[1]
		qend = line.split('\t')[14]
		sseqid = line.split('\t')[3]
		sframe = int(line.split('\t')[6])
		send = int(line.split('\t')[16])
		if qlen == qend:
			if sframe > 0:
				if sseqid in genome:
					codon = genome[sseqid][send:send+3].upper()
			else:
				if sseqid in genome:
					codon = genome[sseqid][send-4:send-1].upper().reverse_complement()
			codon = str(codon)
			if codon not in stop_codons:
				stop_codons[codon] = 1
				# print(sseqid, send, sframe, codon)
			else:
				stop_codons[codon] += 1
				# print(sseqid, send, sframe, codon)
	except ValueError:
		pass

with open(result, 'w') as out:
	for key, value in stop_codons.items():
		out.write('{}\t{}\n'.format(key, value))
