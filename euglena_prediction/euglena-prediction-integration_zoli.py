import os
from Bio import SeqIO

print('This script integrates data from several predictor algorithms to create a set of putative euglenid plastid proteins')
print('Required files are: "predisi.txt", "predsl.txt", "tmhmm.txt", and "pred-input.fasta"')
print('Please analyse your dataset with these predictors prior to using this script.\n=================================================')
print('ERASE OLD result_cleaved.txt AND pred-ML2-out.txt WHEN STARTING WITH A NEW DATASET.\n=================================================\n')
#getting input files ready - comment section if dependencies are missing
os.system('source ~/.bash_profile')
#PrediSi is written in JAVA
#PredSL is in perl, but requires JAVA and hmmer
try:
	os.system('tmhmm -short pred-input.fasta > tmhmm.txt')
except:
	print("tmhmm dependency!")

#open input files
predisi = open("predisi.txt").readlines()
predsl = open("predsl.txt").readlines()
tmhmm = open("tmhmm.txt").readlines()
fasta = SeqIO.parse("pred-input.fasta", "fasta")



seq_d = {}
print("parsing PrediSi and PredSL predictions and sequences into data dictionary")
for line in predisi:
	line = line.split("\t")
	#FASTA-ID	Score	Cleavage Position	Signal Peptide ?	Chart
	#[0]		[1]		[2]					[3]					[4]
	if "FASTA-ID" not in line[0]:
		if len(line[0].split()) > 1:
			line[0] = line[0].split()[0]
		seq_d[line[0]] = [line[3], line[2]]
nonredundant = []
for line in predsl:
	line = line.split()
	#sequence id	cTP score	mTP score	SP score	prediction	cleavage site	thylakoid	lTP cl. site
	#[0]			[1]			[2]			[3]			[4]			[5]				[6]			[7]
	if line[0] not in nonredundant:
		nonredundant.append(line[0])
		if "sequence" not in line[0]:
			seq_d[line[0]].append(line[4])
			seq_d[line[0]].append(line[5])



nonredundant = []
for line in tmhmm:
	line = line.split()
	#queryID	length	expAA 	First60	PredHel	Topology
	#[0]		[1]		[2]		[3]		[4]		[5]
	numhel = line[4].split('=')[1]
	if line[0] not in nonredundant:
		nonredundant.append(line[0])	
		seq_d[line[0]].append(numhel)
nonredundant = []
for sequence in fasta:
	if sequence.name not in nonredundant:
		nonredundant.append(sequence.name)
		seq_d[sequence.name].append(sequence.description)
		seq_d[sequence.name].append(sequence.seq)

print("filtering proteins with signal peptide")
for protein in seq_d.keys():
	#seq_d items:
	#predisi-prediction	predisi-cleavage	predsl-prediction	predsl-cleavage	TMHMM 	seq_header	seq_seq
	#[0]				[1]					[2]					[3]				[4]		[5]			[6]
	if seq_d[protein][0] == "Y" or seq_d[protein][2] == "secreted":
		try:
			SP_si = int(seq_d[protein][1])
			SP_sl = int(seq_d[protein][3])
			if SP_si == SP_sl:
				SP_cleaved = '>{}\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_si:])
				with open('result_cleaved.txt', 'a') as result:
					result.write(SP_cleaved)
			else:
				SP_cleaved_si = '>{}@PrediSi\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_si:])
				SP_cleaved_sl = '>{}@PredSL\n{}\n'.format(seq_d[protein][5], seq_d[protein][6][SP_sl:])
				with open('result_cleaved.txt', 'a') as result:
					result.write(SP_cleaved_si)
					result.write(SP_cleaved_sl)
		except ValueError as VE:
			with open('result_errors.txt', 'a') as errors:
				errors.write('SP cleavage error: {}\n{}\n\n'.format(seq_d[protein][5], str(VE)))

print("cleaved proteins written to result_cleaved.txt... now running MultiLoc2 plant")
if os.path.isfile("pred-ML2-cleave.txt") == False:
	os.system('python /home/manager/MultiLoc2/src/multiloc2_prediction.py -fasta=result_cleaved.txt -predictor=LowRes -origin=plant -result=pred-ML2-cleave.txt -output=simple')
	os.system('python /home/manager/MultiLoc2/src/multiloc2_prediction.py -fasta=pred-input.fasta -predictor=LowRes -origin=animal -result=pred-ML2-full.txt -output=simple')


print("MultiLoc2 finished, now adding predictions to data dictionary")
ML2 = open("pred-ML2-full.txt").read()
ML2F = ML2.split('\n')

nonredundant = []
for line in ML2F:
	if len(line.split('\t')) != 1:
		line = line.split('\t')
		preds = line[1:]
		#['cytoplasmic: ', 'mitochondrial: ', 'nuclear: ', 'secretory pathway: ']
		if line[0] not in nonredundant:
			nonredundant.append(line[0])
			try:
				highest = preds[0]
				second = preds[1]
				seq_d[line[0]].append(highest)
				if float(preds[1].split()[-1]) > 0.2:
					seq_d[line[0]].append(second)
				else:
					seq_d[line[0]].append(" ")
			except:
				print("exception occurred")

ML2 = open("pred-ML2-cleave.txt").read()
ML2C = ML2.split('\n')

finalplastidprots = []
nonredundant = []
for line in ML2C:
	if len(line.split('\t')) != 1:
		line = line.split('\t')
		preds = sorted(line[1:])
		#['chloroplast: ', 'cytoplasmic: ', 'mitochondrial: ', 'nuclear: ', 'secretory pathway: ']
		if "@PredSL" in line[0] or "@PrediSi" in line[0]:
			print("alternative cleavage for: ", line[0])
			line[0] = line[0].split("@")[0]
		if line[0] not in nonredundant:
			nonredundant.append(line[0])
			try:
				cTP = preds[0].split()[1]
				mTP = preds[2].split()[1]
				#print(cTP, mTP)
				seq_d[line[0]].append(cTP)
				seq_d[line[0]].append(mTP)
				#seq_d items from here on:
				#predisi-prediction	predisi-cleavage	predsl-prediction	predsl-cleavage	TMHMM 	seq_header	seq_seq	fullML2-1	fullML2-2	cleaveML2cp	cleaveML2mt
				#[0]				[1]					[2]					[3]				[4]		[5]			[6]		[7]			[8]			[9]			[10]
				if float(cTP) > 0.15 or float(mTP) > 0.15:
					finalplastidprots.append(line[0])
			except ValueError as VE:
				with open('result_errors.txt', 'a') as errors:
					errors.write('ML2 processing error: {}\n{}\n\n'.format(line, str(VE)))
print("proceeding to writing putative plastid proteins to .fasta and all predictions to .tsv")
with open('pred-plastid-proteins.fasta', 'w') as out:
	for pos in finalplastidprots:
		out.write('>{}\n{}\n\n'.format(seq_d[pos][5], seq_d[pos][6]))
#print(seq_d)
print("now to writing predictions")
with open('predictions-all.tsv', 'w') as out:
	out.write("EC\tContig\tlen(aa)\tTMHMM\tPrediSi\tPredSL\tMultiLoc highest\tMultiLoc (after SP cleavage)\n")
	for seq in seq_d.keys():
		#print(seq_d[seq])
		try:
			EC = seq_d[seq][5].split()[1][:-1]
		except IndexError:
			print("sequence description not found: " + seq)
			EC = "unknown"
		length = len(seq_d[seq][6])
		TMHMM = seq_d[seq][4]
		if len(seq_d[seq]) == 11 :
			out.write('{}\t{}\t{}\t{}\t{}\t{}\t{} {}\tpt: {} (mt: {})\n'.format(EC, seq, length, TMHMM, seq_d[seq][1], seq_d[seq][3], seq_d[seq][7], seq_d[seq][8], seq_d[seq][9], seq_d[seq][10]))
		elif len(seq_d[seq]) == 7 :
			with open('ML2_errors.txt', 'a') as MLerrors:
				MLerrors.write('ML2 processing error: {}\n{}\n\n'.format(seq, seq_d[seq]))
		else:
			print(seq)
			out.write('{}\t{}\t{}\t{}\t{}\t{}\t{} {}\t-\n'.format(EC, seq, length, TMHMM, seq_d[seq][1], seq_d[seq][3], seq_d[seq][7], seq_d[seq][8]))

print("file writing done")
