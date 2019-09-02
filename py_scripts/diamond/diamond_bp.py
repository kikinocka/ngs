#!/usr/bin/env python3
import subprocess

query = '/home/kika/MEGAsync/diplonema/octopine_superfamily/DP_ocdh.fa'
out = '/home/kika/MEGAsync/diplonema/octopine_superfamily/MMETSP_dp_ocdh.dmnd.out'
db = '/home/kika/programs/blast-2.5.0+/bin/CAM_P_0001000.pep.fa.dmnd'
threads = 4
target = 100

subprocess.call('diamond blastp -q {} -d {} -o {} -p {} --max-target-seqs {} --sensitive'.format(
	query, db, out, threads, target), shell=True)
# -f 6 --evalue 1e-5
