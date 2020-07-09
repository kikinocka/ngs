#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/data/kinetoplastids/genomes_fasta/Herpetomonas_muscarum_genome.fna'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
