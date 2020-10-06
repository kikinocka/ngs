#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/data/stramenopiles/platysulcus_tardus.fa'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
