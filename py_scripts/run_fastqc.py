#!/usr/bin/python3
import os
import subprocess

os.chdir('/home/kika/llin/')
files = os.listdir()

fastqc = 'fastqc'
out_dir = '/home/kika/llin/'
threads = 2

for file in files:
	subprocess.call('{} -t {} -o {} {}'.format(fastqc, threads, out_dir, file), shell=True)