#!/usr/bin/env python3
import subprocess

db = '/Dcko/MEGAsync/Data/stramenopiles/Proteromonas_l_proteins.fasta'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
