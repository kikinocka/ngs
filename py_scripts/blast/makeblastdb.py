#!/usr/bin/python3
import subprocess

db = '/home/kika/programs/blast-2.5.0+/bin/pelo_predicted_proteins.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
