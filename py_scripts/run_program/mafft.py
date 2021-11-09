#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/archamoebae/trees/hydA/ver4/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/discoba/alns/')
# existing = 'alns/ref_metamonads_eukref.barthelona.anaeramoeba.aln'
# add = 'metamonads_otus_above100.fa'
# out = 'metamonads_V9.mafft.aln'
# log = 'metamonads_V9.mafft.log'
# # subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)

#merge alignments
os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/discoba/alns/')
aln1 = 'Euglenozoa_alignment.aln'
# aln2 = 'Euglenida_alignment.aln'
# aln3 = 'preaxostyla_eukref.aln'
fasta = 'outgroup_nogaps.fa'
input = 'euglenozoa_outgroup.in'
table = 'euglenozoa_outgroup.table'
out = 'euglenozoa_outgroup.mafft.aln'
log = 'euglenozoa_outgroup.mafft.log'
subprocess.call('cat {} {} > {}'.format(aln1, fasta, input), shell=True)
print('Alignments concatenated\n\n')
subprocess.call('ruby {} {} > {}'.format(maketable, aln1, table), shell=True)
print('Table prepared\n\n')
subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
print('Alignments merged')
