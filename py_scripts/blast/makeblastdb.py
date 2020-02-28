#!/usr/bin/python3
import subprocess

db = '/Dcko/MEGAsync/Data/dpapilatum/dpap_predicted_proteins.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
