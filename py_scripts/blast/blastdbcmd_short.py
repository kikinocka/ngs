#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Phylloquinone/assembly_MenDHC/input.fasta'
one = 'TRINITY_DN9897_c0_g1_i1'
positions = '43693-47247'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/pelo_trinity.fa'
out = '/home/kika/ownCloud/pelomyxa/mito_proteins/pelo_TRINITY_DN9897_c0_g1_i1'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 