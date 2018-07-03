#!/usr/bin/python3
import os
from Bio import SeqIO

ogs = open('/media/4TB1/blastocrithidia/orthofinder/Results_Jan03/WorkingDirectory/Orthogroups_2.txt')

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/insertions/')
files = os.listdir()

print('getting names')
names = {}
for og in ogs:
	names[og.split(': ')[0]] = og.split(': ')[1].replace(' ', ', ').replace('\n', '')
print('names obtained')

for file in files:
	if file.endswith('.fa'):
		file_name = file.split('.fa')[0]
		print(file_name)
		with open('{}_renamed.fa'.format(file_name), 'w') as new:
			print('{}_renamed.fa opened'.format(file_name))
			for key, value in names.items():
				print('inspecting {}'.format(key))
				for i in value.split(', '):
					print('searching for {} in insertions'.format(i))
					for ins in SeqIO.parse(file, 'fasta'):
						if ins.name == i:
							print('{} found in names'.format(ins.name))
							new.write('>{} {} {}\n{}\n'.format(
								ins.name, key, ins.description.split('_')[-1], ins.seq))
