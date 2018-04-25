#!/usr/bin/python3
import re
from Bio import SeqIO
from Bio.Blast import NCBIXML

seq = SeqIO.read('/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y6/y6.txt', 'fasta')
tsv = open('/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y6/y6_modules_best_blast.tsv')
xml = open('/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y6/y6_modules_blast.xml')
gff = open('/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y6/y6_modules.gff', 'w')

class MitoGene:
	def __init__(self, name, start, end):
		self.name = name
		self.start = start
		self.end = end
		self.mod_coordinates = []
		self.blast_records = NCBIXML.parse(xml)
		self.editing = []

	def add_module(self, mstart, mend):
		self.mod_coordinates.append((mstart, mend))

	def add_editing(self, blast_records):
		for self.record in self.blast_records:
			best_hit = self.record.alignments[0].hsps[0]
			sstart = best_hit.sbjct_start
			if ' ' in best_hit.match:
				for i in re.finditer(' ', best_hit.match):
					position = sstart + i.start()
					self.editing.append((position, best_hit.query[i.start()], best_hit.sbjct[i.start()]))
#
mito = MitoGene(str(seq.name).split('_')[1], 1, len(seq.seq))
mito.add_editing(xml)

for line in tsv:
	try:
		sstart = int(line.split('\t')[12])
		send = int(line.split('\t')[13])
		mito.add_module(sstart, send)
	except:
		pass

for i in range(len(mito.mod_coordinates)):
	while i < len(mito.mod_coordinates):
		gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tName={};ID={}-m{}\n'.format(
			mito.name, mito.mod_coordinates[i][0], mito.mod_coordinates[i][1], mito.name, mito.name, i+1))
		for pos in mito.editing:
			if pos[0] in range(mito.mod_coordinates[i][0],mito.mod_coordinates[i][1]):
				if (pos[1] == 'C' and pos[2] == 'T') or (pos[1] == 'A' and pos[2] == 'G'):
					gff.write(
						'{}\tblast\tmisc_difference\t{}\t{}\t.\t.\t.\tName={};ID={}-m{}_{}_{}>{};ref={};alt={}\n'.
						format(mito.name, pos[0], pos[0], mito.name, mito.name, i+1, pos[0], pos[1], pos[2], pos[1], 
						pos[2]))
				else:
					gff.write(
						'{}\tblast\tpolymorphism\t{}\t{}\t.\t.\t.\tName={};ID={}-m{}_{}_{}>{};ref={};alt={}\n'.
						format(mito.name, pos[0], pos[0], mito.name, mito.name, i+1, pos[0], pos[1], pos[2], pos[1], 
						pos[2]))
		if i+1 == len(mito.mod_coordinates):
			pass
		else:
			if mito.mod_coordinates[i][1]+1 < mito.mod_coordinates[i+1][0]:
				gff.write('{}\tblast\tpoly-u\t{}\t{}\t.\t+\t.\tName={};ID={}-m{}-pU{}\n'.format(
					mito.name, mito.mod_coordinates[i][1]+1, mito.mod_coordinates[i+1][0]-1, mito.name, 
					mito.name, i+1, mito.mod_coordinates[i+1][0]-1 - mito.mod_coordinates[i][1]))
		i += 1
	else:
		break

if mito.mod_coordinates[-1][1] < mito.end:
	for i in range(len(seq.seq[mito.mod_coordinates[-1][1]:])):
		if seq.seq[mito.mod_coordinates[-1][1]] == seq.seq[mito.mod_coordinates[-1][1]+i]:
			tstart = mito.mod_coordinates[-1][1]
			tend = mito.mod_coordinates[-1][1]+i+1
		tract = str(seq.seq[tstart:tend])
	if 'T' in tract:
		gff.write('{}\tblast\tpoly-u\t{}\t{}\t.\t+\t.\tName={};ID={}-m{}-pU{}\n'.format(
			mito.name, tstart+1, tend, mito.name, mito.name, len(mito.mod_coordinates), len(tract)))
		if tend < mito.end:
			gff.write('{}\tblast\tpoly-A\t{}\t{}\t.\t+\t.\tName={};ID={}-m{}-pA{}\n'.format(
				mito.name, tend+1, mito.end, mito.name, mito.name, len(mito.mod_coordinates), mito.end-tend))
	elif 'A' in tract:
		gff.write('{}\tblast\tpoly-A\t{}\t{}\t.\t+\t.\tName={};ID={}-m{}-pA{}\n'.format(
			mito.name, tstart+1, tend, mito.name, mito.name, len(mito.mod_coordinates), len(tract)))

gff.close()