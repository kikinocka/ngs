#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/RABs/')
# files = [x for x in os.listdir() if x.endswith('.fa')]
# # files = [x for x in os.listdir() if x.startswith('kineto')]

# for file in files:
# 	print(file)
# 	#L-INS-i (proteins with one alignable domain)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

# 	# #E-INS-i (proteins with several functional domains)
# 	# out = '{}.einsi.aln'.format(file.split('.fa')[0])
# 	# log = '{}.einsi.log'.format(file.split('.fa')[0])
# 	# subprocess.call('{} --thread 7 --genafpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 	# 	mafft, file, out, log), shell=True)

# 	# #tRNAs
# 	# out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	# log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --op 10 --ep 0 --inputorder {} > {} 2> {}'.format(
# 	# 	mafft, file, out, log), shell=True)
	
# 	# subprocess.call('{} --auto --inputorder {} > {} 2> {}'.format(mafft, file, out, log), shell=True)


#add to aligned sequences
os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
existing = 'queries/RABs/rabs.mafft.aln'
add = 'diplonemids_all/mantamonas/RABs/rabs.fa'
out = 'diplonemids_all/mantamonas/RABs/rabs.mafft.aln'
log = 'diplonemids_all/mantamonas/RABs/rabs.mafft.log'
subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder --keeplength {} > {} 2> {}'.format(mafft, add, existing, out, log), 
# 	shell=True)
	

# #merge alignments
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/all_adaptors/ver8/')
# aln1 = '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/all_adaptors/ver5/medium.mafft.aln'
# aln2 = 'diplo_AP5M.mafft.aln'
# # fasta = 'arfs.fa'
# input = 'medium.mafft.in'
# table = 'medium.mafft.table'
# out = 'medium.mafft.aln'
# log = 'medium.mafft.log'
# # subprocess.call('cat {} {} > {}'.format(aln1, fasta, input), shell=True)
# subprocess.call('cat {} {} > {}'.format(aln1, aln2, input), shell=True)
# print('Alignments concatenated\n\n')
# subprocess.call('ruby {} {} > {}'.format(maketable, aln1, table), shell=True)
# # subprocess.call('ruby {} {} {} {} {} {} {} > {}'.format(maketable, aln1, aln2, aln3, aln4, aln5, aln6, table), shell=True)
# print('Table prepared\n\n')
# # subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# subprocess.call('{} --thread 7 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
