#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'
maketable = '/Users/kika/miniconda3/bin/makemergetable.rb'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/archamoebae/trees/LPLA/ver3/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --op 10 --ep 0 --inputorder {} > {} 2> {}'.format(
# 	# 	mafft, file, out, log), shell=True)
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
# existing = 'BLASTs/tca17_cdd.aln'
# add = 'BLASTs/tca17.fa'
# out = 'BLASTs/tca17_eug-cdd.mafft.aln'
# log = 'BLASTs/tca17_eug-cdd.mafft.log'
# # subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)


#merge alignments
os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/above99_decontaminated/stramenopiles/')
aln1 = 'STR_5480seqs_230711_core_blast_min700bp.No_Chimera.align_V5.lineage.aln'
aln2 = 'v9.mafft.aln'
# aln3 = 'preaxostyla_eukref.aln'
# fasta = 'otu.fa'
input = 'placement/stramenopiles_v9.in'
table = 'placement/stramenopiles_v9.table'
out = 'placement/stramenopiles_v9.mafft.aln'
log = 'placement/stramenopiles_v9.mafft.log'
# subprocess.call('cat {} {} > {}'.format(aln1, fasta, input), shell=True)
subprocess.call('cat {} {} > {}'.format(aln1, aln2, input), shell=True)
print('Alignments concatenated\n\n')
# subprocess.call('ruby {} {} > {}'.format(maketable, aln1, table), shell=True)
subprocess.call('ruby {} {} {} > {}'.format(maketable, aln1, aln2, table), shell=True)
print('Table prepared\n\n')
# subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
subprocess.call('{} --thread 7 --merge {} {} > {} 2> {}'.format(mafft, table, input, out, log), shell=True)
print('Alignments merged')
