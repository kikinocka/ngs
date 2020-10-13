#!/usr/bin/env python3
import subprocess

db = '/Users/kika/data/eukprot/EP00004_Rigifila_ramosa.fasta'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
