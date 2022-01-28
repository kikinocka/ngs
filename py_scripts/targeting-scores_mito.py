#courtesy of github.com/morpholino

#function to read fasta and create a list of sequences
print("Please, enter the prefix (-p) of prediction files to be analyzed...(xxx.txt)")
print("###############################################")

import argparse,os,sys
from Bio import SeqIO
import pandas as pd

#### Functions ####
###################

def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

#### Collect Input ####
#######################

parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-p', '--prefix', help='Prediction files prefix', default='found_proteins5')
parser.add_argument('-f', '--fasta', help='Fasta infile (only for iPSORT)', default='none')
parser.add_argument('-a', '--accessions', help='Accession rename key file', default='none')
parser.add_argument('-d', '--directory', help='Working directory', default='.')

args = parser.parse_args()

prefix = args.prefix
#treefile = args.treefile
accessions = args.accessions
os.chdir(args.directory)

# #### Change to workdir ####
# ###########################

# if os.path.isdir("/Users/morpholino/OwnCloud/"):
# 	home = "/Users/morpholino/OwnCloud/"
# elif os.path.isdir("/Volumes/zoliq data/OwnCloud/"):
# 	home = "/Volumes/zoliq data/OwnCloud/"
# elif os.path.isdir("/mnt/mokosz/home/zoli/localize"):
# 	home = "/mnt/mokosz/home/zoli/"
# else:
# 	print("Please set a homedir")
# datadir = home + "progs/PYTHON/targeting_script/"
# if args.directory == ".":
# 	print("changing to default directory")
# 	defdir = "HamplLab/retortamonas/dataset_transcriptomes_v2/targeting"
# 	wd = home + defdir
# 	os.chdir(wd)
# else:
# 	os.chdir(args.directory)


#ONLY FOR TEST PURPOSES:
#accessions = "leaf_renaming.txt"

print("FILE prefix defined: %s" %(prefix))
if accessions != 'none':
	print("Taxa replacement key defined: {}".format(accessions))
else:
	print("Only predefined codes are used.")

#### Open and parse predictions ####
####################################

preds_d = pd.DataFrame() #predictions dictionary
leavesfrompreds = set()
#preds_d['accession'] = {'hectar':'ND', 'signalp': 'ND', 'asafind': 'ND', 'targetp': 'ND', 'ML2ANIM': 'ND', 'ML2PLANT': 'ND'}

if os.path.exists(prefix + ".ipsort.txt"):
	print("Found iPSORT output, cannot parse score")
	"""ipsort = open(prefix + ".ipsort.txt").read().split('\n')
	try:
		seq_d = {x.seq[:80]: x.name for x in SeqIO.parse(args.fasta, "fasta")}
	except:
		print("Fasta file not found, iPSORT disabled")
	possiblepredsipsort = {'Other': 'CYT', 'Mitochondrial Transit Peptide': 'MT', 'Signal Peptide': 'SEC'}
	storeline = False
	name, pred = None, None
	for line in ipsort:
		if line.strip() == "Input Sequence:":
			storeline = "seq"
			if isinstance(name, str): #store the previous prediction in pandas
				preds_d.at[name, "ipsort"] = pred
			continue #data on the next line
		elif line.strip() == "Prediction:":
			storeline = "pred"
			continue #data on the next line

		#iPSORT does not record seq names! need another dictionary to match seqs with names
		if storeline == "seq":
			seq = line.strip() #this is first 80 aa, followed by "..."
			if seq.endswith("..."):
				seq = seq.replace("...", "")
				#check the seq dictionary to find matching seqname!
			name = seq_d.get(seq, None)
			storeline = False
		elif storeline == "pred":
			pred = line.strip()
			storeline = False
	#dont forget to store the last item
	if isinstance(name, str): #store the previous prediction in pandas
		preds_d.at[name, "ipsort"] = pred"""


if os.path.exists(prefix + ".mitofates_fungi.txt"):
	print("Found MitoFates-fungi output")
	mitofates = open(prefix + ".mitofates_fungi.txt").read().split('\n')
	possiblepredsmitofates = {'No mitochondrial presequence': 'CYT', 'Possessing mitochondrial presequence': 'MT'}
	for item in mitofates:
		#Identifier	Score	Prediction	cleavage site(enzyme)	net charge	TOM20 recognition motif	...
		#[0]		[1]		[2]			[3]						[4]			[5]	
		
		if not item.startswith('Sequence ID') and len(item) != 0:
			item = item.split('\t')
			name = item[0].split(" ")[0]
			pred = float(item[1])
			#pred = possiblepredsmitofates[pred]
			preds_d.at[name, "MitoFates fungi"] = pred

if os.path.exists(prefix + ".mitofates_metazoa.txt"):
	print("Found MitoFates-metazoa output")
	mitofates = open(prefix + ".mitofates_metazoa.txt").read().split('\n')
	possiblepredsmitofates = {'No mitochondrial presequence': 'CYT', 'Possessing mitochondrial presequence': 'MT'}
	for item in mitofates:
		#Identifier	Score	Prediction	cleavage site(enzyme)	net charge	TOM20 recognition motif	...
		#[0]		[1]		[2]			[3]						[4]			[5]	
		
		if not item.startswith('Sequence ID') and len(item) != 0:
			item = item.split('\t')
			name = item[0].split(" ")[0]
			pred = float(item[1])
			#pred = possiblepredsmitofates[pred]
			preds_d.at[name, "MitoFates metazoa"] = pred

if os.path.exists(prefix + ".nommpred_mro.txt"):
	print("Found NommPred-MRO output")
	nommpred_mro = open(prefix + ".nommpred_mro.txt").read().split('\n')
	possiblepredsnommpred = {'Other': 0, 'MRO': 1}
	for item in nommpred_mro:
		#Identifier	Class
		#[0]		[1]
		
		if not item.startswith('Seq_Name') and len(item) != 0:
			item = item.split('\t')
			name = item[0].split(" ")[0]
			pred = item[1]
			pred = possiblepredsnommpred[pred]
			preds_d.at[name, "NommPred MRO"] = pred

if os.path.exists(prefix + ".nommpred_dict.txt"):
	print("Found NommPred-Dicty output")
	nommpred_mro = open(prefix + ".nommpred_dict.txt").read().split('\n')
	possiblepredsnommpred = {'Other': 0, 'Mt': 1}
	for item in nommpred_mro:
		#Identifier	Class
		#[0]		[1]
		
		if not item.startswith('Seq_Name') and len(item) != 0:
			item = item.split('\t')
			name = item[0].split(" ")[0]
			pred = item[1]
			pred = possiblepredsnommpred[pred]
			preds_d.at[name, "NommPred Dicty"] = pred

if os.path.exists(prefix + ".ML2_animalHI.txt"):
	print("Found MultiLoc2-animal output")
	ML2ANIM = open(prefix + ".ML2_animalHI.txt").read().split('\n')
	possiblepredsml2 = {'cytoplasmic': "CYT", "ER": "ER", "extracellular": "EXTRACELLULAR", 
	"Golgi apparatus": "GOLGI", "mitochondrial": "MT", "nuclear": "NC", "lysosomal": "LYSOSOME", 
	"peroxisomal": "PEROXISOME", "plasma membrane": "PLASMA MEMBRANE", "secretory pathway": "SEC", "vacuolar": "VACUOLE"}
	if ML2ANIM[0].startswith("MultiLoc2"):
		ML2ANIM = ML2ANIM[5:]
		for item in ML2ANIM:
			#protein	decreasing localization predictions from: cytoplasmic, ER, extracellular, Golgi apparatus, mitochondrial, nuclear, lysosomal, peroxisomal, plasma membrane
			if len(item) > 0:
				item = item.split('\t')
				name = item[0]
				Loc = possiblepredsml2[item[1].split(':')[0]]
				Loc = float([x for x in item if "mitochondrial" in x][0].split(': ')[1])
				best, secondbest = item[1], item[2]
				for pred in possiblepredsml2:
					best = best.replace(pred, possiblepredsml2[pred])
					secondbest = secondbest.replace(pred, possiblepredsml2[pred])
				pred = ("{}_({} > {})".format(Loc, best, secondbest))
				preds_d.at[name, "ML2 animal"] = Loc
				#preds_d.at[name, "ML2animal_broad"] = pred

if os.path.exists(prefix + ".ML2_animal.txt"):
	print("Found MultiLoc2-animal output")
	ML2ANIM = open(prefix + ".ML2_animal.txt").read().split('\n')
	possiblepredsml2 = {'cytoplasmic': "CYT", "mitochondrial": "MT", "nuclear": "NC", 
	"secretory pathway": "SEC"}
	if ML2ANIM[0].startswith("MultiLoc2"):
		ML2ANIM = ML2ANIM[5:]
		for item in ML2ANIM:
			#protein	decreasing localization predictions from: cytoplasmic, ER, extracellular, Golgi apparatus, mitochondrial, nuclear, lysosomal, peroxisomal, plasma membrane
			if len(item) > 0:
				item = item.split('\t')
				name = item[0]
				Loc = possiblepredsml2[item[1].split(':')[0]]
				Loc = float([x for x in item if "mitochondrial" in x][0].split(': ')[1])
				best, secondbest = item[1], item[2]
				for pred in possiblepredsml2:
					best = best.replace(pred, possiblepredsml2[pred])
					secondbest = secondbest.replace(pred, possiblepredsml2[pred])
				pred = ("{}_({} > {})".format(Loc, best, secondbest))
				preds_d.at[name, "ML2 animal"] = Loc
				#preds_d.at[name, "ML2animal_broad"] = pred

if os.path.exists(prefix + ".ML2_fungalHI.txt"):
	print("Found MultiLoc2-fungal output")
	ML2ANIM = open(prefix + ".ML2_fungalHI.txt").read().split('\n')
	possiblepredsml2 = {'cytoplasmic': "CYT", "ER": "ER", "extracellular": "EXTRACELLULAR", 
	"Golgi apparatus": "GOLGI", "mitochondrial": "MT", "nuclear": "NC", "lysosomal": "LYSOSOME", 
	"peroxisomal": "PEROXISOME", "plasma membrane": "PLASMA MEMBRANE", "secretory pathway": "SEC", "vacuolar": "VACUOLE"}
	if ML2ANIM[0].startswith("MultiLoc2"):
		ML2ANIM = ML2ANIM[5:]
		for item in ML2ANIM:
			#protein	decreasing localization predictions from: cytoplasmic, ER, extracellular, Golgi apparatus, mitochondrial, nuclear, lysosomal, peroxisomal, plasma membrane
			if len(item) > 0:
				item = item.split('\t')
				name = item[0]
				Loc = possiblepredsml2[item[1].split(':')[0]]
				Loc = float([x for x in item if "mitochondrial" in x][0].split(': ')[1])
				best, secondbest = item[1], item[2]
				for pred in possiblepredsml2:
					best = best.replace(pred, possiblepredsml2[pred])
					secondbest = secondbest.replace(pred, possiblepredsml2[pred])
				pred = ("{}_({} > {})".format(Loc, best, secondbest))
				preds_d.at[name, "ML2 fungal"] = Loc
				#preds_d.at[name, "ML2fungal_broad"] = pred

if os.path.exists(prefix + ".ML2_fungal.txt"):
	print("Found MultiLoc2-fungal output")
	ML2ANIM = open(prefix + ".ML2_fungal.txt").read().split('\n')
	possiblepredsml2 = {'cytoplasmic': "CYT", "mitochondrial": "MT", "nuclear": "NC", 
	"secretory pathway": "SEC"}
	if ML2ANIM[0].startswith("MultiLoc2"):
		ML2ANIM = ML2ANIM[5:]
		for item in ML2ANIM:
			#protein	decreasing localization predictions from: cytoplasmic, ER, extracellular, Golgi apparatus, mitochondrial, nuclear, lysosomal, peroxisomal, plasma membrane
			if len(item) > 0:
				item = item.split('\t')
				name = item[0]
				Loc = possiblepredsml2[item[1].split(':')[0]]
				Loc = float([x for x in item if "mitochondrial" in x][0].split(': ')[1])
				best, secondbest = item[1], item[2]
				for pred in possiblepredsml2:
					best = best.replace(pred, possiblepredsml2[pred])
					secondbest = secondbest.replace(pred, possiblepredsml2[pred])
				pred = ("{}_({} > {})".format(Loc, best, secondbest))
				preds_d.at[name, "ML2 fungal"] = Loc
				#preds_d.at[name, "ML2fungal_broad"] = pred

if os.path.exists(prefix + ".predotar.txt"):
	print("Found Predotar output")
	predotar = open(prefix + ".predotar.txt").read().split('\n')
	MT = {'possibly mitochondrial', 'mitochondrial'}
	SEC = {'possibly ER', 'ER'}
	for item in predotar:
		#Identifier	Mito	ER		Elsewhere	Prediction
		#[0]		[1]		[2]		[3]			[4]	

		item = item.split('\t')
		if not item[0].startswith('Sequence') and len(item) == 5:
			name = item[0]#.split(" ")[0]
			pred = float(item[1])
			preds_d.at[name, "Predotar"] = pred

if os.path.exists(prefix + ".signalp.txt"):
	print("Found SignalP output")
	signalp = open(prefix + ".signalp.txt").read().split('\n') #sensitive version 4.1
	for item in signalp:
		# SignalP-3.0 euk predictions  
		# name 	Cmax 	pos ? 	Ymax	pos ? 	Smax 	pos ? 	Smean 	?	D 	? 	name 	!	Cmax	pos ? 	Sprob	?
		#  0	1		2	3	4		5	6	7		8	9	10		11	12	13	14		15	16		17	18	19		20
		# SignalP-4.1 euk predictions  
		# names Cmax	pos 	Ymax	pos 	Smax	pos 	Smean 	D 	?	Dmaxcut 	Networks-used 
		#  0	1		2		3		4		5		6		7		8	9	10			11

		if not item.startswith('#') and len(item) != 0:
			item = item.split()
			name = item[0]
			if len(item) == 21:
				#SIGNALPVERSION 3.0
				pred = item[13]
				pred = pred.replace("N", "OTHER")
				pred = pred.replace("Y", "SIGNAL")
			if len(item) == 12:
				#SIGNALPVERSION 4.x
				pred = item[9]
				pred = pred.replace("N", "OTHER")
				pred = pred.replace("Y", "SIGNAL")
			preds_d.at[name, "signalp"] = pred

if os.path.exists(prefix + ".PTS.txt"):
	print("Found peroxisomal signals output, skipping")
	"""signalp = open(prefix + ".PTS.txt").read().split('\n') #sensitive version 4.1
	for item in signalp:
		if not item.startswith('#') and len(item) != 0:
			item = item.split()
			name = item[0]
			pred = item[1]
			pred = pred.replace("none", "_")
			preds_d.at[name, "PTS"] = pred"""

if os.path.exists(prefix + ".targetp.txt"):
	print("Found TargetP output")
	targetp = open(prefix + ".targetp.txt").read().split('\n') #PLANT + NONPLANT
	possiblepredstargetp = {"M": "MT", "C": "PT", "S": "SIG", "_": "_"}
	for item in targetp:
		#Name       Len     mTP     SP      other   Loc     RC
		#[0]		[1]		[2]		[3]		[4]		[5]		[6]
		#BUT PLANT!
		#Name       Len     cTP     mTP     SP      other   Loc     RC
		#[0]		[1]		[2]		[3]		[4]		[5]		[6]		[7]
		#PLANT incl Cleavage Site Prediction:
		#Name       Len     cTP     mTP     SP      other   Loc     RC 		TPlen
		#[0]		[1]		[2]		[3]		[4]		[5]		[6]		[7]		[8]

		if len(item.split()) > 1 and item.split()[1].isnumeric(): #takes only lines with prediction
			item = item.split()
			name = item[0]
			if len(item) == 7:
				targetpreds_l = [float(item[2]), float(item[3]), float(item[4])]
				targetpreds_d = {float(item[2]): 'mTP', float(item[3]): 'SP', float(item[4]): 'other'}
				Loc = possiblepredstargetp[item[5]]
				pred = ("{}_({}:{} > {}:{})".format(Loc, targetpreds_d[max(targetpreds_l)], max(targetpreds_l), targetpreds_d[second_largest(targetpreds_l)], second_largest(targetpreds_l)))
				pred = float(item[2])
			elif len(item) == 8 or len(item) == 9:
				targetpreds_l = [float(item[2]), float(item[3]), float(item[4]), float(item[5])]
				targetpreds_d = {float(item[2]): 'cTP', float(item[3]): 'mTP', float(item[4]): 'SP', float(item[5]): 'other'}
				Loc = possiblepredstargetp[item[6]]
				pred = ("{}_({}:{} > {}:{})".format(Loc, targetpreds_d[max(targetpreds_l)], max(targetpreds_l), targetpreds_d[second_largest(targetpreds_l)], second_largest(targetpreds_l)))
				pred = float(item[2])
			else:
				pred = "nd"

			preds_d.at[name, 'targetp'] = pred

if os.path.exists(prefix + ".targetp2.txt"):
	print("Found TargetP2 output")
	targetp2 = open(prefix + ".targetp2.txt").read().split('\n') #PLANT + NONPLANT
	possiblepredstargetp = {"mTP": "MT", "cTP": "PT", "luTP": "THYLAKOID", "SP": "SIGNAL", "noTP": "CYT"}
	for item in targetp2:
		#NON-PLANT
		#Name       Pred    noTP    SP      mTP     CS position
		#[0]		[1]		[2]		[3]		[4]		[5]

		#PLANT
		#Name       Pred    noTP    SP      mTP     cTP     luTP    CS position
		#[0]		[1]		[2]		[3]		[4]		[5]		[6]		[7]
		if not item.startswith("#") and len(item) != 0: #takes only lines with prediction
			item = item.split("\t")
			name = item[0]
			if len(item) == 6:
				targetpreds_l = [float(item[2]), float(item[3]), float(item[4])]
				targetpreds_d = {float(item[2]): 'CYT', float(item[3]): 'SP', float(item[4]): 'mTP'}
				Loc = possiblepredstargetp[item[1]]
				pred = ("{}_({}:{} > {}:{})".format(Loc, targetpreds_d[max(targetpreds_l)], max(targetpreds_l), targetpreds_d[second_largest(targetpreds_l)], second_largest(targetpreds_l)))
				pred = float(item[4])
			elif len(item) == 8:
				targetpreds_l = [float(item[2]), float(item[3]), float(item[4]), float(item[5])]
				targetpreds_d = {float(item[2]): 'cTP', float(item[3]): 'mTP', float(item[4]): 'SP', float(item[5]): 'CYT'}
				Loc = possiblepredstargetp[item[6]]
				pred = ("{}_({}:{} > {}:{})".format(Loc, targetpreds_d[max(targetpreds_l)], max(targetpreds_l), targetpreds_d[second_largest(targetpreds_l)], second_largest(targetpreds_l)))
				pred = float(item[4])
			else:
				print(len(item))
				pred, Loc = "nd", "nd"
			#preds_d.at[name, 'TargetP2'] = Loc
			preds_d.at[name, 'TargetP2_broad'] = pred

if os.path.exists(prefix + ".pprowler.txt"):
	print("Found PProwler output")
	pprowler = open(prefix + ".pprowler.txt").read().split('\n')
	possiblepredspprowler = {2: 'CYT', 1: 'MT', 
							3: 'PEROXISOME', 0: 'SEC'}
	for item in pprowler:
		#Identifier	SP	MTP	OTHER	Peroxisome
		#[0]		[1]	[2]	[3]		[4]	
		
		if not item.startswith('Sequence') and len(item.split('\t')) > 4:
			item = item.split('\t')
			name = item[0].split(" ")[0]
			preds = [float(x) for x in item[1:]]
			top = preds.index(max(preds))
			if isinstance(top, int):
				pred = possiblepredspprowler[top]
			else:
				print("Warning, two preds with the same score!")
				#quit()
			pred = float(item[-3])
			preds_d.at[name, "PProwler"] = pred
	

if os.path.exists(prefix + ".cello.txt"):
	print("Found Cello output")
	cello = open(prefix + ".cello.txt").read().split('\n')
	possiblepredscello = {'Cytoplasmic': 'CYT', 'Mitochondrial': 'MT', 'PlasmaMembrane': 'SEC', 
							'InnerMembrane': 'SEC', 'OuterMembrane': 'SEC', 'ER': 'SEC',
							'Nuclear': 'NC', 'Lysosomal': 'LYSOSOME', 'Chloroplast': 'MT',
							'Extracellular': 'SEC', 'Vacuole': 'VACUOLE', 'Peroxisomal': 'PEROXISOME'}
	
	for item in cello:
		#SeqNO.	... (various scores)	#Most-likely-Location	#SeqName
		#[0]							[-2]					[-1]
		
		if not item.startswith('#SeqNO.') and len(item) != 0:
			item = item.replace('\t\t', '\t') #this is due to formatting of short compartment names "Nuclear" and "Lysosomal"
			item = item.split('\t')
			name = item[-1]
			pred = item[-2]
			pred = possiblepredscello[pred]
			pred = float(item[14])
			preds_d.at[name, "Cello"] = pred
	
print("preds_dictionary collected")
preds_d.to_csv(path_or_buf='{}.scores.tsv'.format(prefix), float_format='%0.3f', sep="\t")

print("Done!\n\n")
