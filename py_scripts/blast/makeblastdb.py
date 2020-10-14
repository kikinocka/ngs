#!/usr/bin/env python3
import subprocess

db = '/Users/kika/data/alveolates/Perkinsus_marinus_GCF_000006405.prot.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
