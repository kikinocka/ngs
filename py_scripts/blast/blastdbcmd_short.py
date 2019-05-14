#!/usr/bin/env python3
import subprocess

file = '/home/kika/ownCloud/pelomyxa/mito_proteins/import/in'
one = 'TRINITY_GG_4203_c0_g1_i1'
positions = '43693-47247'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/p57_RNA_Trinity.fasta'
out = '/home/kika/ownCloud/blastocrithidia/genes/termination_factors/p57_eRF3_trinity_nt.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 