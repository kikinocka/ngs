#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/data/kinetoplastids/genomes_fasta/Ldonovani_BPK282A1_Genome.fasta'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
