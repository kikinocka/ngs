#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Phylloquinone/assembly_MenDHC/input.fasta'
one = 'NODE_38_length_30771_cov_87.5178'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/triat_scaffolds_transc.fasta'
out = '/home/kika/ownCloud/blastocrithidia/genes/aa-tRNA-synthetases/additional/triat_NODE.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 