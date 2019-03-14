#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/EG_prot/yoshida_dataset/')
yoshidaf = open('found_in_yosihda.txt')
tablef = open('our_table.txt')

yoshida = []
for line in yoshidaf:
	yoshida.append(line[:-1])

# table = []
for line in tablef:
	if line[:-1] in yoshida:
		print(line[:-1])

