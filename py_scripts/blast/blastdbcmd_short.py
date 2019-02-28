#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Phylloquinone/assembly_MenDHC/input.fasta'
one = 'NODE_36_length_42357_cov_125.809'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'
out = '/home/kika/ownCloud/blastocrithidia/genes/aa-tRNA-synthetases/additional/jac_NODE.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 