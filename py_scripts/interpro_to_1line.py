#!/usr/bin/env python3
import os

os.chdir('/Users/kika/Downloads/')
interpro = open('eukarya_metaeuk.interpro.tsv')
# accessions = open('bnon_old-new.acc')
output = 'eukarya_metaeuk.interpro_1line.tsv'
errorout = 'eukarya_metaeuk.interpro_erorrs.txt'

# acc = {}
# for line in accessions:
# 	line = line.strip()
# 	acc[line.split('\t')[0]] = line.split('\t')[1]
# # print(acc)

GO_terms = {}
errors = []
for line in interpro:
	try:
		# print(line.split('\t')[0])
		line = line.strip()
		db = set()
		ipr = set()
		go = set()
		# react = set()
		# metac = set()

		db.add(line.split('\t')[4] + ': ' + line.split('\t')[5])
		ipr.add(line.split('\t')[11] + ': ' + line.split('\t')[12])

		if ipr == set('-'):
			go.add('-')
			# react.add('-')
			# metac.add('-')
		else:
			go.add(line.split('\t')[13].replace('|', '; '))
			# if line.split('\t')[14] == '-':
			# 	react.add('-')
			# 	metac.add('-')
			# else:
			# 	for item in line.split('\t')[14].split('|'):
			# 		if item.startswith('Reactome'):
			# 			react.add(item.split(': ')[1])
			# 		elif item.startswith('MetaCyc'):
			# 			metac.add(item.split(': ')[1])

		# if react == set():
		# 	react.add('-')
		# if metac == set():
		# 	metac.add('-')

		if line.split('\t')[0] not in GO_terms:
			GO_terms[line.split('\t')[0]] = [go, db, ipr] #, react, metac]
		else:
			GO_terms[line.split('\t')[0]][0].update(go)
			GO_terms[line.split('\t')[0]][1].update(db)
			GO_terms[line.split('\t')[0]][2].update(ipr)
			# GO_terms[line.split('\t')[0]][3].update(react)
			# GO_terms[line.split('\t')[0]][4].update(metac)
	except:
		errors.append(line.split('\t')[0])

# for key in acc.keys():
# 	if key in GO_terms:
# 		# print(key)
# 		GO_terms[acc[key]] = GO_terms.pop(key)

# print(GO_terms)

# with open(output, 'w') as result:
# 	result.write('Entry\tGO_IDs\tPFAM_IDs\tIPR_IDs\tReactome_IDs\tMetaCyc_IDs\n')
# 	for key, value in GO_terms.items():
# 		result.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], value[2], value[3], value[4]))

with open(output, 'w') as result:
	result.write('Entry\tGOs\tDB\tIPR\n')
	for key, value in GO_terms.items():
		result.write('{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], value[2]))

with open(errorout, 'w') as errout:
	for item in errors:
		errout.write('{}\n'.format(item))
