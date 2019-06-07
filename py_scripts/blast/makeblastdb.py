#!/usr/bin/python3
import subprocess

db = '/home/kika/MEGAsync/Data/EG_RNAseq/EUGR_all.fasta'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
