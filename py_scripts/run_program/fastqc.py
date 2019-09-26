#!/usr/bin/python3
import os
import subprocess

os.chdir('/home/kika/llin/')
files = os.listdir()

out_dir = '/home/kika/llin/'
threads = 2

for file in files:
	subprocess.call('fastqc -t {} -o {} {}'.format(fastqc, threads, out_dir, file), shell=True)