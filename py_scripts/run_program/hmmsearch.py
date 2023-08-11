#!/usr/bin/env python3
import os
import subprocess

# hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

# db = '/Users/kika/ownCloud/blastocrithidia/genome_assembly/p57_polished_translated.fa'
# orgn = 'bnon_gen'

# for file in files:
# 	print(file)
# 	name = file.split('.hmm')[0]
# 	out = orgn + '_' + name + '.hmmsearch.out'
# 	subprocess.call('{} -o {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# # -o
# # --tblout


dbs = [x for x in os.listdir('/mnt/mokosz/home/kika/allDB/renamed/') if x.endswith('.faa')]

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/')
for db in dbs:
	# print(db)
	orgn = db.split('.faa')[0]
	for file in files:
		print(file)
	# 	name = file.split('.hmm')[0]

	# 	if os.path.isdir('{}'.format(name)) == True:
	# 		pass
	# 	else:
	# 		os.mkdir('{}'.format(name))

	# 	subprocess.call('cd {}'.format(name), shell=True)
	# 	out = orgn + '.' + name + '.hmmsearch.tsv'
	# 	subprocess.call('hmmsearch --tblout {} --cpu 10 {} {}'.format(out, file, db), shell=True)
	# 	subprocess.call('cd ..', shell=True)
