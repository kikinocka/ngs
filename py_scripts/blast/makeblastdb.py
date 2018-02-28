#!/usr/bin/python3
import subprocess

db = '/home/kika/programs/blast-2.5.0+/bin/jac_proteins_companion.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
