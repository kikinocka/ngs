#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/angomonas_SNAREs/trees/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)
# 	# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --op 10 --ep 0 --inputorder {} > {} 2> {}'.format(
# 	# 	mafft, file, out, log), shell=True)
# 	# subprocess.call('{} --auto --inputorder {} > {} 2> {}'.format(mafft, file, out, log), shell=True)


#add to aligned sequences
os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/Lane26_18S_V9/metamonads/MLSB/above99/')
existing = 'ver2/metamonads.mafft.aln'
add = 'mlsb_metamonads.no_chimera.above99.fa'
out = 'ver2/metamonads_v9.mafft.aln'
log = 'ver2/metamonads_v9.mafft.log'
subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)


# #merge alignments
# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/above99/metamonads/')
# aln1 = 'ver1/metamonads.mafft.aln'
# aln2 = 'ver2/pimpavicka_dataset.aln'
# # aln3 = 'preaxostyla_eukref.aln'
# # fasta = 'otu.fa'
# input = 'ver2/metamonads.mafft.in'
# table = 'ver2/metamonads.mafft.table'
# out = 'ver2/metamonads.mafft.aln'
# log = 'ver2/metamonads.mafft.log'
# # subprocess.call('cat {} {} > {}'.format(aln1, fasta, input), shell=True)
# subprocess.call('cat {} {} > {}'.format(aln1, aln2, input), shell=True)
# print('Alignments concatenated\n\n')
# # subprocess.call('ruby {} {} > {}'.format(maketable, aln1, table), shell=True)
# subprocess.call('ruby {} {} {} > {}'.format(maketable, aln1, aln2, table), shell=True)
# print('Table prepared\n\n')
# # subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# subprocess.call('{} --thread 7 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
