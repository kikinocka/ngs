#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/stops_replaced/')
files = sorted(os.listdir())

done = []
for file in files:
	if file.endswith('.aln'):
		name = file.split('.')[0]
		done.append(name)
print(done)

files = reversed(files)
for file in files:
	if file.endswith('_replaced2.fa'):
		name = file.split('_')[0]
		if name in done:
			print('Alignment for {} already done.'.format(name))
		else:
			print('\n------------------------------------')
			print(name)
			d = 'protein'
			os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, name))
			print('------------------------------------\n')
