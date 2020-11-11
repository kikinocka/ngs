#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/peroxisomes/mastig_lopit/orthofinder/OGs_sc_tran-supp/ends_fasta/')
files = [x for x in os.listdir() if x.endswith('.fa')]

distances = []
with open('ends_fasta.txt', 'w') as result:
	for file in files:
		print(file)
		aln = AlignIO.read(file, format = 'fasta')
		calculator = DistanceCalculator('blosum62')
		gd = calculator.get_distance(aln)
		distances.append(round(gd[0][1], 2))
		result.write('{}\t{}\n'.format(file.split('_')[0], round(gd[0][1], 2)))

# protein_models = ['benner6', 'benner22', 'benner74', 'blosum100', 'blosum30', 'blosum35', 'blosum40', 'blosum45', 'blosum50', 
	# 'blosum55', 'blosum60', 'blosum62', 'blosum65', 'blosum70', 'blosum75', 'blosum80', 'blosum85', 'blosum90', 'blosum95', 'feng', 
	# 'fitch', 'genetic', 'gonnet', 'grant', 'ident', 'johnson', 'levin', 'mclach', 'miyata', 'nwsgappep', 'pam120', 'pam180', 'pam250', 
	# 'pam30', 'pam300', 'pam60', 'pam90', 'rao', 'risler', 'structure']


arr = np.array(distances)
plt.hist(arr, color='#00BE89')
plt.xlabel('distance')
plt.ylabel('frequency')
plt.show()

# n, bins, patches = plt.hist(distances)
# print(n)
# print(bins)
# for i in range(10):
# 	print(patches[i])
