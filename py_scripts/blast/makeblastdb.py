#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/anaeramoeba/proteomes/Tvag_proteins.fasta'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
