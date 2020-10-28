#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/archamoebae/mastigamoeba_balamuthi/blastdb/Masba_prot_LATEST.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
