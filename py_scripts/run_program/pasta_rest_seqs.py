#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/known_secondary_structures/PASTA/')
files = sorted(os.listdir())

done = []
for file in files:
	if file.endswith('.aln'):
		name = file.split('.')[0]
		done.append(name)
print(done)

files = reversed(files)
for file in files:
	if file.endswith('.fa'):
		name = file.split('_')[0]
		if name in done:
			print('Alignment for {} already done.'.format(name))
		else:
			print('\n------------------------------------')
			print(name)
			d = 'protein'
			os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, name))
			print('------------------------------------\n')
