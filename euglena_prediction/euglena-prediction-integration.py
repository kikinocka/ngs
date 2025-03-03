#!/usr/bin/python3
#Predictions from TMHMM, PredSL and PrediSi are needed!

import subprocess
from Bio import SeqIO

tmhmm = open("tmhmm.txt").readlines()
predisi = open("predisi.txt").readlines()
predsl = open("predsl.txt").readlines()
fasta = SeqIO.parse("pred-input.fasta", "fasta")
table = open('table.xlsx', 'w')

table.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('contig', 'number of TMD', 'SP length (PrediSi)',
	'SP length (PrediSL)', 'TP (MultiLoc2)', 'Protein sequence'))

seq_d = {}
#parsing predictions and sequences into dictionary
for line in predisi:
	line = line.split('\t')
	#FASTA-ID	Score	Cleavage Position	Signal Peptide ?	Chart
	#[0]		[1]		[2]					[3]					[4]
	if "FASTA-ID" not in line[0]:
		seq_d[line[0].split(' ')[0]] = [line[3], line[2]]
for line in predsl:
	line = line.split('\t')
	#sequence id	cTP score	mTP score	SP score	prediction	cleavage site	thylakoid	lTP cl. site
	#[0]			[1]			[2]			[3]			[4]			[5]				[6]			[7]
	if "sequence" not in line[0]:
		seq_d[line[0]].append(line[4])
		seq_d[line[0]].append(line[5])
for line in tmhmm:
	line = line.split('\t')
	#sequence id	len	ExpAA	First60	PredHel	Topology
	#[0]			[1]	[2]		[3]		[4]		[5]
	seq_d[line[0]].append(line[4].split('=')[1])

for sequence in fasta:
	seq_d[sequence.name].append(sequence.description)
	seq_d[sequence.name].append(sequence.seq)

for protein in seq_d.keys():
	#seq_d items:
	#predisi-prediction	predisi-cleavage	predsl-prediction	predsl-cleavage	tmd	seq_header	seq_seq
	#[0]				[1]					[2]					[3]				[4]	[5]			[6]
	if seq_d[protein][0] == "Y" or seq_d[protein][2] == "secreted":
		try:
			SP_si = int(seq_d[protein][1])
			SP_sl = int(seq_d[protein][3])
			if SP_si == SP_sl:
				SP_cleaved = '>{}\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_si:])
				with open('result_cleaved.txt', 'a') as result:
					result.write(SP_cleaved)
			else:
				SP_cleaved_si = '>{}_PrediSi\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_si:])
				SP_cleaved_sl = '>{}_PredSL\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_sl:])
				with open('result_cleaved.txt', 'a') as result:
					result.write(SP_cleaved_si)
					result.write(SP_cleaved_sl)
		except ValueError as VE:
			with open('result_errors.txt', 'a') as errors:
				errors.write('{}\n{}\n\n'.format(seq_d[protein][5], str(VE)))		
	else:
		with open('no_sp.fasta', 'a') as no_sp:
			no_sp.write('>{}\n{}\n'.format(protein, seq_d[protein][6]))

print('SP cleavage done')
print('Running MultiLoc2 on sequences without SP')
subprocess.call('/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=no_sp.fasta -predictor=LowRes -origin=animal -result=full_ML2.txt -output=simple', shell=True)
print('MultiLoc2 prediction on sequences without SP done')

full_ml2_prediction = open('full_ML2.txt').readlines()
#seq_name	#prediction_1: 0.00 #prediction_2: 0.00 #prediction_3: 0.00 #prediction_4: 0.00
#[0]		#[1]				#[2]				#[3]				#[4]
full_ml2_d = {}
for line in full_ml2_prediction:
	line = line.split('\t')
	try:
		full_ml2_d[line[0]] = line[1]
	except:
		pass

for key in full_ml2_d.keys():
	for root_key, value in seq_d.items():
		if key == root_key:
			final_line = '{}\t{}\t-\t-\t{}\t{}\n'.format(key, seq_d[root_key][4], full_ml2_d[key], seq_d[root_key][6])
			table.write(final_line)

print('Running MultiLoc2 on cleaved sequences')
subprocess.call('/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=result_cleaved.txt -predictor=LowRes -origin=plant -result=cleaved_ML2.txt -output=simple', shell=True)
print('MultiLoc2 prediction on cleaved sequences done')

ml2_prediction = open('cleaved_ML2.txt').readlines()
#seq_name	#prediction_1: 0.00 #prediction_2: 0.00 #prediction_3: 0.00 #prediction_4: 0.00 #prediction_5: 0.00
#[0]		#[1]				#[2]				#[3]				#[4]				#[5]
ml2_d = {}
ml2_d_sorted = {}
for line in ml2_prediction:
	line = line.split('\t')
	try:
		ml2_d[line[0]] = (line[1], line[2], line[3], line[4], line[5][:-1])
		for key in ml2_d:
			ml2_d_sorted[key] = sorted(ml2_d[key])
	except:
		pass

for key in ml2_d_sorted.keys():
	# cTP_name = ml2_d_sorted[key][0].split(' ')[0]
	# mTP_name = ml2_d_sorted[key][2].split(' ')[0]
	cTP = ml2_d_sorted[key][0].split(' ')[1]
	mTP = ml2_d_sorted[key][2].split(' ')[1]
	for root_key, value in seq_d.items():
		if key == root_key:
			final_line = '{}\t{}\t{}\t{}\tpt: {} (mt: {})\t{}\n'.format(
				key, seq_d[root_key][4], seq_d[root_key][1], seq_d[root_key][3], cTP, mTP, seq_d[root_key][6])
			table.write(final_line)