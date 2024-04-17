#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

#align de-novo
os.chdir('/Users/kika/ownCloud/blasto_comparative/genes/aaRS/')
files = [x for x in os.listdir() if x.endswith('TrpRS2.fa')]

for file in files:
	print(file)
	#L-INS-i (proteins with one alignable domain)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	log = '{}.mafft.log'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
		mafft, file, out, log), shell=True)

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
	
	# subprocess.call('{} --auto --inputorder {} > {} 2> {}'.format(mafft, file, out, log), shell=True)


# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/trees/metazoa_myxozoa/')
# existing = 'ref_aln/myxozoa_final.aln'
# add = 'V9.fa'
# out = 'myxozoa_V9.mafft.aln'
# log = 'myxozoa_V9.mafft.log'
# # subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder --keeplength {} > {} 2> {}'.format(mafft, add, existing, out, log), 
# 	shell=True)
	

# #merge alignments
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/SUM-K/trees/ARFs/')
# aln1 = '/Users/kika/ownCloud/membrane-trafficking/queries/ARFs/ScrollSaw_output_untrimmed_338seq.updated.aln'
# # aln2 = '1C.aln'
# # aln3 = '2A.aln'
# # aln4 = '2B.aln'
# # aln5 = '2C.aln'
# # aln6 = '2D.aln'
# fasta = 'arfs.fa'
# input = 'arfs.mafft.in'
# table = 'arfs.mafft.table'
# out = 'arfs.mafft.aln'
# log = 'arfs.mafft.log'
# subprocess.call('cat {} {} > {}'.format(aln1, fasta, input), shell=True)
# # subprocess.call('cat {} {} {} {} {} {} > {}'.format(aln1, aln2, aln3, aln4, aln5, aln6, input), shell=True)
# print('Alignments concatenated\n\n')
# subprocess.call('ruby {} {} > {}'.format(maketable, aln1, table), shell=True)
# # subprocess.call('ruby {} {} {} {} {} {} {} > {}'.format(maketable, aln1, aln2, aln3, aln4, aln5, aln6, table), shell=True)
# print('Table prepared\n\n')
# # subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# subprocess.call('{} --thread 7 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
