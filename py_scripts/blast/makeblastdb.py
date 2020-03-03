#!/usr/bin/env python3
import subprocess

db = '/Dcko/ownCloud/membrane-trafficking/Rab_db/RABs_deduplicated.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
