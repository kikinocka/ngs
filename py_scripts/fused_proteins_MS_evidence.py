#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/fused_proteins/')
ms_bed = open('MS_peptides.bed')
fused_gff = open('p57_fused.gff')
hits_gff = open('p57_prepared_hits.gff')

class Fused_protein:
	def __init__(self, name, contig, start, end):
		self.name = name
		self.contig = contig
		self.start = start
		self.end = end
		self.hit_coordinates = []

	def set_hit(self, hit_start, hit_end):
		self.hit_coordinates.append((hit_start, hit_end))

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
			fused[key].set_hit(hit_start, hit_end)

for key, value in fused.items():
	print(key)
	print(value.contig)
	print(value.start)
	print(value.end)
	print(value.hit_coordinates)

# def hits_positions(hits_gff):
# 	hits_pos = OrderedDict()
# 	for line in hits_gff:
# 		contig = line.split('\t')[0]
# 		start = int(line.split('\t')[3])
# 		end = int(line.split('\t')[4])
# 		hitid = line.split('\t')[8].split(';')[0].split('ID=')[1]
# 		hits_pos[hitid] = [start, end, contig]
# 	return hits_pos

# def ms_positions(ms_bed):
# 	ms_pos = OrderedDict()
# 	for line in ms_bed:
# 		contig = line.split('\t')[0]
# 		start = int(line.split('\t')[1])
# 		end = int(line.split('\t')[2])
# 		trinity = line.split('\t')[3]
# 		ms_pos[trinity] = [start, end, contig]
# 	return ms_pos

# ms_pos = ms_positions(ms_bed)
# fused_pos = fused_positions(fused_gff)
# hits_pos = hits_positions(hits_gff)

# # for km, vm in ms_pos.items():
# # 	for kf, vf in fused_pos.items():
# # 		if vm[2] == vf[2]:
# # 			if vf[0] <= vm[0] <= vf[1]:
# # 				print(vm[2], km)

# for kh, vh in hits_pos.items():
# 	for kf, vf in fused_pos.items():
# 		if vh[2] == vf[2]:
# 			if vf[0] <= vh[0] <= vf[1]:
# 				print(kf, vh[2], vf[0], vh[0], vh[1], vf[1])

