#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/TBCs/tbc-D/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

#add to aligned sequences
os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/')
existing = 'ScrollSaw_output_untrimmed_masked_348seq.updated.aln'
add = 'ver4/euglenozoans.fa'
out = 'ver4/arfs.mafft.aln'
log = 'ver4/arfs.mafft.log'
subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)

# #merge alignments
# os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/Lane26_18S_V9/metamonads/reference_tree')
# aln1 = 'fornicata_eukref.aln'
# aln2 = 'parabasalia_eukref.aln'
# aln3 = 'preaxostyla_eukref.aln'
# fasta = 'barthelonids.fa'
# input = 'metamonads.in'
# table = 'metamonads.table'
# out = 'metamonads.mafft.aln'
# log = 'metamonads.mafft.log'
# subprocess.call('cat {} {} {} {} > {}'.format(aln1, aln2, aln3, fasta, input), shell=True)
# print('Aligments concatenated\n\n')
# subprocess.call('ruby {} {} {} {} > {}'.format(maketable, aln1, aln2, aln3, table), shell=True)
# print('Table prepared\n\n')
# subprocess.call('{} --localpair --thread 7 --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
# print('Alignments merged')
