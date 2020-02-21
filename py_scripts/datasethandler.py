#!/usr/bin/env python3

# Performs fasta header renaming, and calls mafft and trimal to align and trim datasets 
# automatically on all fasta files in the current folder
# Alternatively, set folder with -d

import os
from Bio import SeqIO,AlignIO
import argparse
import re

print("PHYLOHANDLER:\nThis script automatically handles fasta datasets to create alignments, trimmed sets and phylo trees.")
print("usage: python datasethandler-new.py [-i infile.fasta/batch -a pasta -t iqtree -d workdirectory -b bootstrap]\n--------------------------------------------------------------------------")

#########################
####       Fx        ####
#########################

def delbadchars(string):
	badchars = ("|+,:;()' ") #also []/@
	n = []
	for c in string:
		if c in badchars:
			c = "_"
		n.append(c)
	result = "".join(n)
	return result

def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

#########################
#### Read parameters ####
#########################

parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-i', '--infile', help='Fasta/Phylip set to be analyzed', default="batch")
parser.add_argument('-a', '--aligner', help='Aligner', default='run_pasta.py')
parser.add_argument('-t', '--treemaker', help='Program for tree inference', default='none')
parser.add_argument('-b', '--bootstrap', help='Boostrap calculation', action='store_true')
parser.add_argument('-d', '--directory', help='Change working directory', default='.')

args = parser.parse_args()

##################################
#### Create working directory ####
##################################

if os.path.isdir("/Users/morpholino/OwnCloud/"):
	home = "/Users/morpholino/OwnCloud/"
elif os.path.isdir("/Volumes/zoliq data/OwnCloud/"):
	home = "/Volumes/zoliq data/OwnCloud/"
else:
	print("Please set a homedir")
if args.directory == ".":
	print("changing to default directory")
	defdir = "genomes/chromera/trees/argJ/"
	wd = home + defdir
	os.chdir(wd)
else:
	os.chdir(args.directory)
for generation in range(1,15):
	if os.path.isdir("TREE" + str(generation)) == False:
		outdir = "TREE" + str(generation)
		break
if os.path.isdir("temp") == False:
	os.mkdir("./temp")
if os.path.isdir("RESULT") == False:
	os.mkdir("./RESULT")

###############################
#### Open and parse inputs ####
###############################

#this is commented bc lineage parsing is not yet implemented
#LINEAGEFILE = home + "progs/PYTHON/fetch_lineages.tsv"
#with open(LINEAGEFILE, 'r') as f:
#	reader = csv.reader(f, delimiter='\t')
#	tax2lineage = {r[0]: r[1] for r in reader}

allowed = ("fasta", "fas", "fst", "phy", "phylip")
if args.infile == "batch":
	infilelist = [x for x in os.listdir(".") if x.split(".")[-1] in allowed]
	infilelist = [x for x in infilelist if not x.startswith("safe")] #bc these have been created by a previous run
	infilelist = [x for x in infilelist if not x.startswith("trim")] #bc these have been created by a previous run
elif args.infile.split(".")[-1] in allowed:
	infilelist = [args.infile]
else:
	quit("file type not recognized - is it fasta/fas/fst or phy/phylip?")

print("PHYLOHANDLER: Files to be analyzed: " + ", ".join(infilelist))
print("PHYLOHANDLER: Data output to dir: " + outdir)
print("PHYLOHANDLER: (some data in ./temp)")
print("PHYLOHANDLER: Final relevant data will be in ./RESULTS")

#zoltan's homemade database renaming dictionary
taxarepl9 = {"actiCORYd": "Corynebacter diphteriae", "actiMYCOt": "Mycobacterium tuberculosis", 
"actiSTREc": "Streptomyces coelicolor", "alfaAZOSs": "Azospirillum sp. B506", 
"alfaMAGNm": "Magnetospirillum magneticum", "alfaNITRh": "Nitrobacter hamburgensis", 
"alfaRHODs": "Rhodobacter sphaeroides", "alfaRICKc": "Rickettsia conori", 
"amoACANc": "Acanthamoeba castellanii str neff", "amoDICTd": "Dictyostelium discoideum", 
"amoENTAh": "Entamoeba histolytica", "amoFILAn": "Filamoeba nolandi", "amoPOLYp": "Polysphondylium pallidum pn500", 
"amoSEXAN": "Sexangularia sp. CB-2014", "amoSTYGA": "Stygamoeba regulata", "amoVANEL": "Vannella", 
"apiBABEb": "Babesia bovis", "apiCHROv": "Chromera velia", "apiCRYPm": "Cryptosporidium muris", 
"apiEIMEt": "Eimeria tenella", "apiGREGn": "Gregarina niphandrodes", "apiNEOSc": "Neospora caninum", 
"apiPLASb": "Plasmodium berghei",
"apiTHEIe": "Theileria equi", "apiTOXOg": "Toxoplasma gondii", "apiVITbr": "Vitrella brassicaformis", 
"apiVORp": "Voromonas pontica", "archPICRt": "Picrophilus torridus", "archPYROa": "Pyrobaculum aerophilum", 
"archSULFt": "Sulfolobus tokodaii", "archTHERv": "Thermoplasma volcanium", "bcidBACTf": "Bacteroides fragilis", 
"bcidFLAVc": "Flavobacterium columnare", "bcidPORPg": "Porphyromonas gingivalis", 
"bcidPREVr": "Prevotella ruminicola", "betaBURKc": "Burkholderia cenocepacia", "betaCUPRn": "Cupriavidus necator", 
"betaRALSs": "Ralstonia solanacearum", "betaVERMe": "Verminephrobacter eiseniae", 
"chlaAMORC": "Amorphochlora amoebiformis", "chlaBIGna": "Bigelowiella natans", "chlaCHLOR": "Chlorarachnion reptans", 
"chlaLOTam": "Lotharella amoebiformis", "chlaLOTgl": "Lotharella globosa", "chlaLOTgZ": "Lotharella globosa", 
"chlaLOTHs": "Lotharella sp. CCMP622", "chlaLOToc": "Lotharella oceanica", "chlaPARTg": "Partenskyella glossopodia", 
"chryCHATs": "Chattonella subsalsa CCMP2191", "chryDINOB": "Dinobryon sp UTEXLB2267", 
"chryHETak": "Heterosigma akashiwo CCMP3107", "chryOCHRO": "Ochromonas sp. CCMP1393", 
"chryVAUCH": "Vaucheria litorea CCMP2940", "cilCLIMv": "Climacostomum virens", "cilMESOD": "Mesodinium pulex", 
"cilLITOp": "Litonotus pictus",
"cilPARAt": "Paramecium tetraurelia", "cilPLATm": "Platyophrya macrostoma", "cilPROTa": "Protocruzia adherens", 
"cilPSEUp": "Pseudocohnilembus persalinus", "cilSTENc": "Stentor coeruleus", "cilTETRt": "Tetrahymena thermophila", 
"crypCHROO": "Chroomonas cf. mesostigmatica", "crypCRYpa": "Cryptomonas paramecium", 
"crypCRYPp": "Cryptomonas paramecium", "crypGONIp": "Goniomonas pacifica", "crypGUILt": "Guillardia theta", 
"crypGUIth": "Guillardia theta", "crypPALPb": "Palpitomonas bilix", "crypRHODl": "Rhodomonas lens", 
"cyanANABv": "Anabaena variabilis", "cyanCROCw": "Crocosphaera watsonii", "cyanCYANp": "Cyanothece sp. PCC 7425", 
"cyanLYNGp": "Lyngbya sp. PCC 8106", "cyanNODUs": "Nodularia spumigena", "cyanPROCm": "Prochlorococcus marinus", 
"cyanSYNEs": "Synechococcus sp. PCC 7335", "cyanTHERe": "Thermosynechococcus elongatus", 
"dinALEXa": "Alexandrium andersonii CCMP2222", "dinALEXc": "Alexandrium catenella OF101", 
"dinALEXt": "Alexandrium tamarense", "dinAMPHc": "Amphidinium carterae", "dinCERAf": "Ceratium fusus PA161109", 
"dinCRYPc": "Crypthecodinium cohnii WH Provasly-Seligo", "dinCRYPZ": "Crypthecodinium cohnii", 
"dinDURIb": "Durinskia baltica CSIRO CS-38", "dinDURIZ": "Durinskia baltica", "dinDINac": "Dinophysis acuminata",
"dinDYNac": "Dinophysis acuminata",
"dinGLENf": "Glenodinium foliaceum CCAP 1116-3", "dinGYMNc": "Gymnodinium catenatum", 
"dinHETro": "Heterocapsa rotundata SCCAP K-0483", "dinHETtr": "Heterocapsa triquestra CCMP 448", 
"dinKARb": "Karenia brevis SP1", "dinKARL": "Karlodinium veneficum", "dinKARmi": "Karlodinium micrum CCMP2283", 
"dinKARZ": "Karenia brevis", "dinKRYPf": "Kryptoperidinium foliaceum", "dinLINGp": "Lingulodinium polyedra CCMP 1738", 
"dinNOCTs": "Noctiluca scintillans", "dinOXYma": "Oxyrrhis marina", "dinPERKm": "Perkinsus marinus", 
"dinPRORm": "Prorocentrum minimum", "dinPYROb": "Pyrodinium bahamense", "dinSCRIP": "Scrippsiella hangoei", 
"dinSYMBs": "Symbiodinium sp.", "eugANGOd": "Angomonas deanei", "eugBODOs": "Bodo saltans", 
"eugEUGgr": "Euglena gracilis", "eugEUGlo": "Euglena longa", "eugEUTc": "Eutreptiella gymnastica-like CCMP1594", 
"eugEUTn": "Eutreptiella gymnastica NIES-381", "eugEUTgn": "Eutreptiella gymnastica NIES-381", "eugLEISm": "Leishmania major", 
"eugNEOBd": "Neobodo designis", "eugPHYTO": "Phytomonas sp isolate em1", "eugTRYPb": "Trypanosoma brucei", 
"excNAEgr": "Naegleria gruberi", "excPERco": "Percolomonas cosmopolitus ATCC50343", "excADUpa": "Aduncisulcus paluster Carplike_NY0171", 
"excBLATn": "Blattamonas nauphoetae", "excCARPm": "Carpediemonas membranifera", "excDYSNb": "Dysnectes brevis", 
"excERGcy": "Ergobibamus cyprinoides", "excHISTm": "Histomonas meleagridis", "excCHIca": "Chilomastix caulleri", 
"excCHIcu": "Chilomastix cuspidata", "excIOTAs": "Iotanema sp.", "excKIPFb": "Kipferlia bialata", 
"excMONOe": "Monocercomonoides exilis", "excPTRIp": "Paratrimastix pyriformis", "excSPIRs": "Spironucleus salmonicida ATCC50377",
"excTREPs": "Trepomonas sp. PC1", "excTRIMm": "Trimastix marina", "extTTRIf": "Tritrichomonas foetus",
"firmBACIa": "Bacillus anthracis", 
"firmLISTm": "Listeria monocytogenes", "firmSTAPa": "Staphyllococcus aureus", "funASPEf": "Aspergillus fumigatus", 
"funCRYPn": "Cryptococcus neoformans", "funDEBAh": "Debaryomyces hansenii cbs767", "funLACCb": "Laccaria bicolor", 
"funNEURc": "Neurospora crassa", "funPUCCg": "Puccinia graminis", "funSCHIp": "Schizosaccharomyces pombe", 
"gamaSHEWb": "Shewanella baltica", "gamaVIBRc": "Vibrio cholerae", "gamaYERSp": "Yersinia pestis", 
"glauGLOEw": "Gloeochaete wittrockiana", "glauCYApa": "Cyanophora paradoxa", 
"glauCYPTg": "Cyanoptyche gloeocystis SAG4.97", "glauGLOwi": "Gloeochaete wittrockiana SAG46.84", 
"grnBATHp": "Bathycoccus prasinos", "grnCHLAl": "Chlamydomonas leiostraca", "grnHELIs": "Helicosporidium sp.",
"grnDUNAt": "Dunaliella tertiolecta", "grnMICpu": "Micromonas pusilla CCMP1545", "grnMICRZ": "Micromonas pusilla", 
"grnNEPHp": "Nephroselmis pyriformis", "grnOSTRm": "Ostreococcus mediterraneus", "grnPICCL": "Picochlorum sp.", 
"grnPICCY": "Picocystis salinarum", "grnPOLYp": "Polytomella parva", "grnPOLYZ": "Polytomella parva", 
"grnPRASc": "Prasinococcus capsulatus", "grnPYRam": "Pyramimonas amylifera CCMP720", 
"grnPYRpa": "Pyramimonas parkeae CCMP726", "grnPYRpZ": "Pyramimonas parkeae", "grnTETRa": "Tetraselmis astigmatica", 
"grnTETRs": "Tetraselmis striata", "grnVOLVc": "Volvox carteri f. nagariensis", "hapCALCl": "Calcidiscus leptoporus", 
"hapEXANg": "Exanthemachrysis gayraliae", "hapIMANT": "Imantonia sp.", "hapISOCHg": "Isochrysis galbana", 
"hapPHEOC": "Phaeocystis sp.", "hapPLEUc": "Pleurochrysis carterae", "hapPRYMp": "Prymnesium parvum", 
"hapSCYPH": "Scyphosphaera apsteinii", "haptEMILh": "Emiliania huxleyi", "haptEMIZ": "Emiliania huxleyi", 
"haptPLEUc": "Pleurochrysis carterae", "haptPRYMp": "Prymnesium parvum Texoma1", 
"hetPERCO": "Percolomonas cosmopolitus", "kytAMBOt": "Amborella trichopoda", "kytARABt": "Arabidopsis thaliana", 
"kytGLYCm": "Glycine max", "kytHORDv": "Hordeum vulgare", "kytORYZs": "Oryza sativa Japonica", 
"kytPHYSp": "Physcomitrella patens", "kytSELAm": "Selaginella moellendorffii", "kytSOlyc": "Solanum lycopersicum", 
"kytZEAma": "Zea mays", "metANOLc": "Anolis carolinensis", "metCAENe": "Caenorhabditis elegans", 
"metDAPHp": "Daphnia pulex", "metHELOr": "Helobdella robusta", "metLOTTg": "Lottia gigantea", 
"metNEMAv": "Nematostella vectensis", "metSCHIm": "Schistosoma mansoni", "metSTROp": "Strongylocentrotus purpuratus", 
"metTRICa": "Trichoplax adhaerens", "opiACANT": "Acanthoeca", "opiMONbr": "Monosiga brevicollis", 
"opiMONOb": "Monosiga brevicollis", "opiSALPr": "Salpingoeca rosetta", "redCHONc": "Chondrus crispus", 
"redCOMPS": "Compsopogon caeruleus", "redCYANm": "Cyanidioschyzon merolae", "redERYTa": "Erythrolobus australicus", 
"redERYTa": "Erythrolobus australicus", "redERYTm": "Erythrolobus madagascarensis", 
"redERYTm": "Erythrolobus madagascarensis", "redGALDs": "Galdieria sulphuraria", 
"redMADAe": "Madagascaria erythrocladioides", "redMADAe": "Madagascaria erythrocladioides", 
"redPORae": "Porphyridium aerugineum SAG 1380-2", "redPORae": "Porphyridium aerugineum", 
"redPORpu": "Porphyra purpurea", "redRHOma": "Rhodella maculata CCMP736", "redRHOSO": "Rhodosorus marinus", 
"redTIMSP": "Timspurckia oligopyrenoides", "rhiAMMOs": "Ammonia sp.", "rhiAMMOZ": "Ammonia sp.", 
"rhiELPHm": "Elphidium margitaceum", "rhiMINch": "Minchinia chitonis", "rhiPARTg": "Partenskyella glossopodia RCC365", 
"rhiPAULc": "Paulinella chromatophora", "rhiPLASb": "Plasmodiophora brassicae", "rhiROSAL": "Rosalina", 
"rhiSORIT": "Sorites sp.", "strALBUl": "Albugo laibachii", "strAPHAi": "Aphanomyces invadans", 
"strAPLAN": "Aplanochytrium", "strAURAl": "Aurantiochytrium limacinum", "strAURAZ": "Aurantiochytrium limacinum", 
"strAUREN": "Aureococcus anophagefferens", "strAUREE": "Aureococcus anophagefferens", 
"strAUREa": "Aureococcus anophagefferens", "strAUREl": "Aureoumbra lagunensis", 
"strBICOS": "Bicosoecida sp. CB-2014", "strBLASh": "Blastocystis hominis", "strBOLID": "Bolidomonas sp.", 
"strBOLIp": "Bolidomonas pacifica", "strCAFro": "Cafeteria roenbergensis", "strCAFsp": "Cafeteria sp.", 
"strCAFca": "Cafeteria str Caron", "strCHATs": "Chattonella subsalsa", "strCHRRH": "Chrysoreinhardia sp.", 
"strCYLIN": "Cylindrotheca closterium", "strDETON": "Detonula confervacea", "strDICTY": "Dictyocha speculum", 
"strDINOB": "Dinobryon sp.", "strDITYL": "Ditylum brightwellii", "strECTsi": "Ectocarpus siliculosus", 
"strEXTUs": "Extubocellulus spinifer", "strFRAGk": "Fragilariopsis kerguelensis", "strHETak": "Heterosigma akashiwo", 
"strMALLO": "Mallomonas sp.", "strNANNg": "Nannochloropsis gaditana B31", "strNITZs": "Nitzschia sp.", 
"strOCHRO": "Ochromonas sp.", "strODONa": "Odontella aurita", "strPARAb": "Paraphysomonas bandaiensis", 
"strPELAG": "Pelagomonas calceolata", "strPHAtr": "Phaeodactylum tricornutum", "strPHEOM": "Phaeomonas parva", 
"strPHYpa": "Phytophthora parasitica", "strPHYra": "Phytophtora ramorum", "strPINGU": "Pinguiococcus pyrenoidosus", 
"strPTERd": "Pteridomonas danica", "strPYTHu": "Pythium ultimum var. sporangiiferum BR650", 
"strPYTHv": "Pythium vexans", "strRHIZC": "Rhizochromulina marina", "strSAPRd": "Saprolegnia diclina", 
"strSKEco": "Skeletonema costatum", "strSTAUR": "Staurosira sp.", "strSYNCR": "Synchroma pusillum", 
"strTHAps": "Thalassiosira pseudonana", "strTHNEM": "Thalassionema frauenfeldii", 
"strTHNEn": "Thalassionema nitzschioides", "strTHRAU": "Thraustochytrium sp.", "strTHTRX": "Thalassiothrix antarctica", 
"strVAUCl": "Vaucheria litorea"}

#remove bad datasets and bad chars from names
taxonpattern = r'\[(.+)\]'
errors = False
for file in infilelist:
	print("PHYLOHANDLER: Processing file: " + file)
	extension = file.split(".")[-1]
	filename = file.replace("." + extension, "")
	if extension in ("fasta", "fas", "fst"):
		indataset = SeqIO.parse(file, 'fasta')
	elif extension in ("phy", "phylip"):
		indataset = SeqIO.parse(file, 'phylip')
	else:
		continue
	#load fasta
	seq_d = {} #dict[shortname] = [fullname, fullrename, safeseq, taxon]
	seq_set = set()
	with open("error.log", "a") as error:
		for sequence in indataset:
			fullname = sequence.description
			fullrename = delbadchars(fullname) #this could be replaced by md5-based codes
			shortname = fullrename.split(" ")[0]
			taxonmatch = re.search(taxonpattern, fullrename)#.group(1)
			if taxonmatch: 
				taxon = taxonmatch.group(1)
				if sequence.name.startswith(taxon):
					fullrename = fullrename.replace("[{}]".format(taxon), "")
					fullname = fullname.replace("[{}]".format(taxon), "")
			elif fullname.split("_")[0] in taxarepl9:
				taxon = taxarepl9[fullname.split("_")[0]]
			else:
				taxon = ""
			safeseq = str(sequence.seq).replace("*","")
			if fullrename not in seq_d:
				if safeseq not in seq_set:
					seq_d[fullrename] = [fullname, fullrename, safeseq, taxon.replace(" ", "_")]
				else:
					errors = True
					error.write("file:{}\tduplicate sequence, skipping:\n{}\n{}\n".format(file, shortname, safeseq))
			else:
				errors = True
				error.write("file:{0}\tseq ID not unique, skipping:\n{1}\n{2}\n{1}\n{3}\n".format(file, shortname, safeseq, seq_d[shortname][1]))
			#print(">" + shortname + "\n" + seq_d[shortname])
	if errors:
		print("PHYLOHANDLER: Errors occurred during sequence read, please refer to error.log")

	print("PHYLOHANDLER: Done loading sequences, now to writing safe_file...")
	with open("rename-{}.txt".format(filename), "w") as renaming, open("safe-{}.fasta".format(filename), "w") as safefile:
		for key,value in seq_d.items():
			renaming.write("{}\t{}\n".format(value[1], value[0])) #value[1][:50] for shorter names
			safefile.write(">{}\n{}\n".format(value[1], value[2])) #value[1][:50] for shorter names

	if args.aligner == "run_pasta.py":
		command = "{0} -d protein -i safe-{1}.fasta -j {1} -o {2}".format(args.aligner, filename, outdir)
	elif args.aligner == "mafft":
		command = "{0} --maxiterate 1000 --quiet --localpair --thread 4 safe-{1}.fasta > safe-{1}.aln".format(args.aligner, filename)
	if os.path.isfile("safe-{0}.aln".format(filename)):
		print("PHYLOHANDLER: alignment detected, previous data not cleaned?")
	else:
		print("PHYLOHANDLER: issuing aligner\n" + command)
		os.system(command)

	#copy and rename PASTA alignment to current directory and issue trimal
	if args.aligner == "run_pasta.py":
		os.system("cp ./{1}/{0}.marker001.safe-{0}.aln ./safe-{0}.aln".format(filename, outdir))
		command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -gt 0.3".format(filename) #-gappyout / -automated1 / -gt 0.3
		print("PHYLOHANDLER: issuing trimmer:\n{}".format(command))
		os.system(command)
		print("PHYLOHANDLER: trimming finished")
	elif args.aligner == "mafft":
		command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -gt 0.3".format(filename) #-gappyout / -automated1 / -gt 0.3
		print("PHYLOHANDLER: issuing trimmer:\n{}".format(command))
		os.system(command)
		print("PHYLOHANDLER: trimming finished")

	#open trimal-trimmed alignment for dumping any gaps-only sequences
	trimalignmentfile = AlignIO.read("trim-{0}.aln".format(filename), "fasta")
	outfile1, outfile2 = "trimfilt-{0}.fasta".format(filename), "trimfilt-{0}.phy".format(filename)
	#filter out any sequences that are gaps-only after trimming
	filtalignmentfile = [record for record in trimalignmentfile if record.seq.count("-") != len(record.seq) and len(record.seq) != 0]
	#uniqtrimseqs = set()
	with open(outfile1, "w") as result:
		#count number of remaining sequences and their length
		for index, r in enumerate(filtalignmentfile):
			#get rid of the trailing newline character at the end of file:
			if index != len(filtalignmentfile) - 1:
				result.write(">{}\n{}\n".format(r.id, r.seq)) #r.description includes seqlen
			else:
				result.write(">{}\n{}".format(r.id, r.seq))
			#use this loop to add data to modify the rename code
			curlength = "{}_{:.2f}%aligned".format(r.id, 100*(len(str(r.seq).replace("-", ""))/len(r.seq)))
			seq_d[r.id].append(curlength)
			##############
			##############
			##############
		count, length = len(filtalignmentfile), trimalignmentfile.get_alignment_length()

	#convert trimfile to phylip format (phylobayes)
	if os.stat(outfile1).st_size > 0: #check for file size
		ffile = AlignIO.read(outfile1, "fasta")
		AlignIO.write(ffile, outfile2, "phylip-relaxed")
	else:
		print("#####\nWARNING: File {} has zero size\n#####".format(outfile1))

	print("PHYLOHANDLER: Now to writing renaming_file...")
	with open("rename-{}.txt".format(filename), "w") as renaming:
		for key,value in seq_d.items():
			try:
				percentalign = value[4]
			except IndexError:
				percentalign = value[1]
			renaming.write("{0}\t{1}\t{2}\n".format(value[1], value[0], percentalign)) #value[1][:50] for shorter names

	print("PHYLOHANDLER: Automated trimming done.")
	print("Trimming produced a file with {} sequences of {} sites".format(count, length))

	if length < 100:
		print("WARNING: alignment shorter than 100 chars, consider less stringent trimming.")

	if args.treemaker != "none":
		if args.treemaker in ["iqtree-omp", "iqtree"]:
			if os.path.isfile("trimfilt-{}.fasta.treefile".format(filename)):
				if os.stat("trimfilt-{}.fasta.treefile".format(filename)).st_size > 0: #check for file size
					print("PHYLOHANDLER: tree inference finished, previous data not cleaned?")
				else:
					print("PHYLOHANDLER: tree inference finished, but treefile is corrupt. Please check")
			else:
				guidetreecommand = "-m LG+F+G -nt AUTO -ntmax 4 -quiet -s trimfilt-{0}.fasta -pre guide-{0}".format(filename) #GTR20 only for very large datasets
				treecommand = "-m LG+C20+F+G -nt AUTO -ntmax 4 -quiet -s trimfilt-{0}.fasta -ft guide-{0}.treefile -bb".format(filename) #GTR20 only for very large datasets
				if args.bootstrap:
					treecommand += " -bb 1000"
				if is_tool("iqtree"):
					program = "iqtree"
				elif is_tool("iqtree-omp"):
					program = "iqtree-omp"
				else:
					quit("PHYLOHANDLER fatal error, iqtree not found")
				print("PHYLOHANDLER: Issuing software for guide tree inference:\n{} {}".format(program, guidetreecommand))
				os.system("{} {}".format(program, guidetreecommand))
				print("PHYLOHANDLER: Issuing software for tree inference:\n{} {}".format(program, treecommand))
				os.system("{} {}".format(program, treecommand))
		else:
			print("PHYLOHANDLER: ERROR assigning software for tree inference!")

	print("PHYLOHANDLER: tree inference finished, post-processing result files...")
	#rename branches for presentation purposes:
	try:
		with open("trimfilt-{}.fasta.treefile".format(filename)) as intree, open("final-{}.fasta.treefile".format(filename), "w") as outtree:
			tree = intree.read()
			for key in taxarepl9:
				while key in tree:
					tree = tree.replace(key, taxarepl9[key])
			outtree.write(tree)
	except FileNotFoundError:
		quit("PHYLOHANDLER: ERROR! Treefile not found! Quitting.")

	#copy all final files to the RESULTS directory and clean up
	os.rename("trimfilt-{}.fasta.treefile".format(filename), "RESULT/{}_{}-iq.treefile".format(filename, generation))
	os.rename("final-{}.fasta.treefile".format(filename), "RESULT/_{}_{}-iq.treefile".format(filename, generation))
	os.rename("trimfilt-{}.fasta".format(filename), "RESULT/{}_{}-ali.fasta".format(filename, generation))
	os.rename("trimfilt-{}.phy".format(filename), "RESULT/{}_{}-ali.phy".format(filename, generation))
	os.rename("{}".format(file), "RESULT/{}".format(file))
	os.rename("rename-{}.txt".format(filename), "RESULT/{}_{}-renamekey.tsv".format(filename, generation))
	os.system("mv safe* temp")
	os.system("mv trim* temp")
	print("####################################\n")


print("PHYLOHANDLER: All requested analyses finished. Hooray!")
if errors:
	print("PHYLOHANDLER: Errors occurred during sequence read, please refer to error.log")
