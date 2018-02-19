#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/fused_proteins/')
fused_gff = open('p57_fused.gff')
hits_gff = open('p57_prepared_hits.gff')
ms_bed = open('MS_peptides.bed')

class Fused_protein:
	def __init__(self, name, contig, start, end):
		self.name = name
		self.contig = contig
		self.start = start
		self.end = end
		self.hit_coordinates = []
		self.ms_coordinates = []

	def set_hit(self, hit_start, hit_end):
		self.hit_coordinates.append((hit_start, hit_end))

	def set_ms(self, ms_start, ms_end):
		self.ms_coordinates.append((ms_start, ms_end))

fused = {}
for line in fused_gff:
	try:
		contig = line.split('\t')[0]
		start = int(line.split('\t')[3])
		end = int(line.split('\t')[4])
		protid = line.split('\t')[8].split(';')[0].split('ID=')[1]
		fused[protid] = Fused_protein(protid, contig, start, end)
	except:
		pass

for line in hits_gff:
	for key, value in fused.items():
		contig = line.split('\t')[0]
		hit_start = int(line.split('\t')[3])
		hit_end = int(line.split('\t')[4])
		if contig == value.contig:
			if hit_start >= value.start and hit_end <= value.end:
				value.set_hit(hit_start, hit_end)

for line in ms_bed:
	for key, value in fused.items():
		contig = line.split('\t')[0]
		ms_start = int(line.split('\t')[1])
		ms_end = int(line.split('\t')[2])
		if contig == value.contig:
			if ms_start >= value.start and ms_end <= value.end:
				value.set_ms(ms_start, ms_end)

for key, value in fused.items():
	# print(key)
	# print(value.contig)
	# print(value.start)
	# print(value.end)
	# print(value.hit_coordinates)
	# print(value.ms_coordinates)
	for hit_pos in value.hit_coordinates:
		for ms_pos in value.ms_coordinates:
			if ms_pos[1] >= hit_pos[1]:
				print(value.contig, key, ms_pos[1], hit_pos[1])