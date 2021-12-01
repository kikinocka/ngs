#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

#align de-novo
os.chdir('/Users/kika/ownCloud/archamoebae/trees/Tom60/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	log = '{}.mafft.log'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/')
# existing = 'RAB_db/RABs_backbone.mafft.aln'
# add = 'tvag/exosomal/rabs.fa'
# out = 'tvag/exosomal/tree/rabs.mafft.aln'
# log = 'tvag/exosomal/tree/rabs.mafft.log'
# subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# # subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)


# #merge alignments
# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/ciliates/')
# aln1 = 'alns/ciliophora_eukref.aln'
# aln2 = 'V9_above99.mafft.aln'
# # aln3 = 'preaxostyla_eukref.aln'
# # fasta = 'outgroup_nogaps.fa'
# input = 'ciliates_v9.in'
# table = 'ciliates_v9.table'
# out = 'ciliates_V9_above99.mafft.aln'
# log = 'ciliates_V9_above99.mafft.log'
# subprocess.call('cat {} {} > {}'.format(aln1, aln2, input), shell=True)
# print('Alignments concatenated\n\n')
# subprocess.call('ruby {} {} {} > {}'.format(maketable, aln1, aln2, table), shell=True)
# print('Table prepared\n\n')
# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
