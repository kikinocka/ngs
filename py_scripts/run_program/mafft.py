#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/COPII/ver2/')
# files = [x for x in os.listdir() if x.endswith('sar1.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

#add to aligned sequences
os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/arf1-6/')
existing = 'Arf1,Arl1,Arl5_SS_untrimmed_cleargapcol.aln'
add = 'ver3/arfs_to_add.fa'
out = 'ver3/arf1-6.mafft.aln'
log = 'ver3/arf1-6.mafft.log'
subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)

# #merge alignments
# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/discoba/alns')
# aln1 = 'Diplonemea_Kinetoplastida_alignment.aln'
# aln2 = 'Euglenida_alignment.aln'
# # aln3 = 'preaxostyla_eukref.aln'
# # fasta = 'barthelonids.fa'
# input = 'euglenozoa.in'
# table = 'euglenozoa.table'
# out = 'euglenozoa.mafft.aln'
# log = 'euglenozoa.mafft.log'
# subprocess.call('cat {} {} > {}'.format(aln1, aln2, input), shell=True)
# print('Aligments concatenated\n\n')
# subprocess.call('ruby {} {} {} > {}'.format(maketable, aln1, aln2, table), shell=True)
# print('Table prepared\n\n')
# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
