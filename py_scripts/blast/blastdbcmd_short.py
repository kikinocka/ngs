#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/ownCloud/blasto_comparative/tRNAs/BLAST/')
files = [x for x in os.listdir() if x.endswith('.acc')]
db = '/Users/kika/ownCloud/blasto_comparative/tRNAs/BLAST/braa_tRNA-UAA.fa'

for file in files: 
	print(file)
	fname = file.split('.')[0]
	with open('{}.fa'.format(fname), 'w') as out:
		subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)



# one = 'NODE_561_length_10236_cov_106.963874'
# positions = '43693-47247'
# strand = 'plus'

# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)
# -range={} 
# positions, 