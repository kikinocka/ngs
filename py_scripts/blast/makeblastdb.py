#!/usr/bin/python3
import subprocess

db = '/home/kika/programs/blast-2.5.0+/bin/CAM_P_0001000.pep.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
