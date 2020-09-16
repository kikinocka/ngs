#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/concatenated/ver2/mafft_before_taxa_trimming/')
alignments = [x for x in os.listdir() if x.endswith('.aln')]

keep = ['EU', 'PharKirb', 'RhypEule', 'EntoSulc', 'RapaViri', 'RhabCost', 'AzumHoya', 'DiplAmbu', 'FlecNera', 'PercCosm', 'TrypBorr', 'Andagodo', 
'EutGymCC', 'Naegleri', 'PetaCant', 'CritBomb', 'Eutrgymn', 'NeobDesi', 'ChasCB1', 'AnisSAL5', 'Bodosalt', 'DiplPapi', 'Trypbruc', 'Tsukglob', 
'NotosM49', 'JenABIC1', 'PeranPtR', 'NeomNP12', 'PerkCCAP', 'SphenAM6', 'KeelM82', 'AnisSMS2', 'Diplo21', 'EuglGrac', 'ReclAmer', 'HetABIC3']

for aln in alignments:
	print(aln)
	dataname = aln.split('.')[0]
	with open('{}.fa'.format(dataname), 'w') as out:
		for seq in SeqIO.parse(aln, 'fasta'):
			if seq.name in keep:
				out.write('>{}\n{}\n'.format(seq.name, str(seq.seq).replace('-', '')))
			else:
				pass
