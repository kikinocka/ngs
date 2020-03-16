#!/usr/bin/env python3
import subprocess

db = '/Dcko/MEGAsync/Data/EG/eg_deeg.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
