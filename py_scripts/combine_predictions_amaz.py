#!/usr/bin/python3
#Check spliting in all three functions!
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/Chlamydomonas/od_toma/')
multiloc = open('putative_pt_genes_aa_complete5_multiloc.txt')
targetp = open('putative_pt_genes_aa_complete5_targetp.tsv')
predsl = open('putative_pt_genes_aa_complete5_predsl.txt')
predictions = open('putative_pt_genes_aa_complete5_predictions.tsv', 'w')

def split_multiloc(multiloc):
	ml_dict = OrderedDict()
	for line in multiloc:
		try:
			line = line.replace('chloroplast', 'pt').replace('mitochondrial', 'mit').replace('cytoplasmic', 'cyt').replace('secretory pathway', 'sp').replace('nuclear', 'nuc')
			name = line.split('\t')[0].split('_m')[0]
			first = line.split('\t')[1]
			second = line.split('\t')[2]
			third = line.split('\t')[3]
			fourth = line.split('\t')[4]
			if 'pt' in first:
				ml_dict[name] = first
			elif 'pt' in second:
				ml_dict[name] = '{} ({})'.format(first, second)
			elif 'pt' in third:
				ml_dict[name] = '{} ({})'.format(first, third)
			elif 'pt' in fourth:
				ml_dict[name] = '{} ({})'.format(first, fourth)
			else:
				ml_dict[name] = first
		except:
			pass
	return ml_dict

def split_targetp(targetp):
	tp_dict = {}
	for line in targetp:
		try:
			name = line.split('\t')[0]
			cp = line.split('\t')[2]
			loc = line.split('\t')[6]
			tp = line.split('\t')[8][:-1]
			if loc == 'C':
				tp_dict[name] = 'pt (TP: {})'.format(tp)
			elif loc == 'M':
				tp_dict[name] = 'mit (pt: {})'.format(cp)
			elif loc == 'S':
				tp_dict[name] = 'sp (pt: {})'.format(cp)
			else:
				tp_dict[name] = '- (pt: {})'.format(cp)
		except:
			pass
	return tp_dict

def split_predsl(predsl):
	ps_dict = {}
	for line in predsl:
		name = line.split('\t')[0].split('_m')[0]
		cp = line.split('\t')[1]
		loc = line.split('\t')[4]
		tp = line.split('\t')[5]
		if loc == 'chloroplast':
			ps_dict[name] = 'pt (TP: {})'.format(tp)
		elif loc == 'mitochondrion':
			ps_dict[name] = 'mit (pt: {})'.format(cp)
		elif loc == 'secreted':
			ps_dict[name] = '- (pt: {})'.format(cp)
		elif loc == 'other':
			ps_dict[name] = '- (pt: {})'.format(cp)
	return ps_dict

ml_dict = split_multiloc(multiloc)
tp_dict = split_targetp(targetp)
ps_dict = split_predsl(predsl)

# predictions.write('Name\tMultiLoc2\tTargetP\n')
predictions.write('Name\tMultiLoc2\tTargetP\tPredSL\n')

for key, value in ml_dict.items():
	if key in tp_dict.keys():
		# predictions.write('{}\t{}\t{}\n'.format(key, value, tp_dict[key]))
		if key in ps_dict.keys():
			predictions.write('{}\t{}\t{}\t{}\n'.format(key, value, tp_dict[key], ps_dict[key]))
		else:
			print(key + ' not in ps')
	else:
		print(key + ' not in tp')