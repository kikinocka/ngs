# Performs fasta header renaming, and calls mafft and trimal to align and trim datasets 
# automatically on all fasta files in the current folder
# Alternatively, set folder with -d
# the same script as in progr/PYTHON but server addresses are changed...

import os
from Bio import SeqIO,AlignIO
import argparse
import re
#import multiprocessing


print("PHYLOHANDLER:\nThis script automatically handles fasta datasets to create alignments, trimmed sets and phylo trees.")
print("usage: python datasethandler-new.py [-i infile.fasta/batch -a pasta -t iqtree -d workdirectory -b bootstrap]\n\
       use custom settings for alignment/trimming/tree inference using the following formula: --treeparams='-m TEST'\n\
--------------------------------------------------------------------------")

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

def find_generation(filename):
	versionre = r"_v\d+"
	try:
		version = re.search(versionre, filename).group(0)
		#"_vXX" tag found
		#print("Dataset already versioned:", version)
		generation = ""
	except AttributeError:
		#dataset not versioned
		versions = [x for x in os.listdir("RESULT") if x.startswith(filename)]
		versions = [x for x in versions if x.endswith("treefile")]
		generation = "_v{}".format(len(versions) + 1)
	return generation

#########################
#### Read parameters ####
#########################

parser = argparse.ArgumentParser(description='How to use argparse')
#whereabouts
parser.add_argument('-d', '--directory', help='Change working directory', default='.')
parser.add_argument('-i', '--infile', help='Fasta/Phylip set to be analyzed', default="batch")
#programs used
parser.add_argument('-a', '--aligner', help='Aligner', default='mafft')
parser.add_argument('-t', '--treemaker', help='Program for tree inference', default='iqtree')
parser.add_argument('--maxcores', help='Maximum cores to use for multithreading', default=10)
#seq processing
parser.add_argument('-n', '--no_dedupe', help='Do not filter duplicates', action='store_true')
#aligner params
parser.add_argument('--alignerparams', nargs='*', action="store", help='Custom aligner parameters, check with manual', default='')
#trimal params
parser.add_argument('--trimalparams', nargs='*', action="store", help='Custom TrimAl parameters, check with manual', default='')
#main params for tree inference
parser.add_argument('-b', '--ufbootstrap', help='Ultra-fast boostrap calculation', action='store_true')
parser.add_argument('-B', '--bootstrap', help='Boostrap calculation', action='store_true')
parser.add_argument('--shalrt', help='Calculate SH-aLRT', action='store_true')
parser.add_argument('-g', '--no_guide', help='Do not perform guide tree inference', action='store_true')
parser.add_argument('--treeparams', nargs='*', action="store", help='Custom tree inference parameters, check with manual', default='')
#parser.add_argument('-m', '--testmodel', help='Test best model', action='store_true') #not implemented
#post-processing
parser.add_argument('-s', '--mark_similarity', help='Mark similarity on branches', action='store_true')

args = parser.parse_args()
alignerparams = " ".join(args.alignerparams)
trimalparams = " ".join(args.trimalparams)
treeparams = " ".join(args.treeparams)

print("PHYLOHANDLER: Check custom params settings:")
print("ALIGN:", alignerparams, "|TRIM:", trimalparams, "|TREE:", treeparams)
##################################
#### Create working directory ####
##################################

if os.path.isdir("/Users/morpholino/OwnCloud/"):
	home = "/Users/morpholino/OwnCloud/"
elif os.path.isdir("/storage/brno3-cerit/home/fussyz01/"):
	home = "/storage/brno3-cerit/home/fussyz01/"
	print("PHYLOHANDLER: Home dir exists!")
elif os.path.isdir("/mnt/mokosz/home/zoli/trees/"):
	home = "/mnt/mokosz/home/zoli/trees/"
	print("PHYLOHANDLER: Home dir exists!")
else:
	print("Please set a homedir")
if args.directory == ".": 	#called by a qsub script following copying to scratch
	print("PHYLOHANDLER: changing to default directory")
	wd = "." 				#home + defdir >> commented to calculate on scratch
	os.chdir(wd)
else:
	if args.directory.startswith("/") or args.directory.startswith("~"):
		print("PHYLOHANDLER: changing to specified directory:", args.directory)
		os.chdir(args.directory)
	else:
		wd = home + args.directory
		print("PHYLOHANDLER: changing to specified directory:", wd)
		os.chdir(wd)

#this generation counter must be improved or skipped:
#for generation in range(1,15):
#	if os.path.isdir("TREE" + str(generation)) == False:
#		outdir = "TREE" + str(generation)
#		break
outdir = "pasta"
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

allowed = ("fasta", "fas", "fst", "fa", "faa", "phy", "phylip")
if args.infile == "batch":
	infilelist = [x for x in os.listdir(".") if x.split(".")[-1] in allowed]
	infilelist = [x for x in infilelist if not x.startswith("safe")] #bc these have been created by a previous run
	infilelist = [x for x in infilelist if not x.startswith("trim")] #bc these have been created by a previous run
elif args.infile.split(".")[-1] in allowed:
	infilelist = [args.infile]
else:
	quit("file type not recognized - is it fasta/fas/fst or phy/phylip?")

infilelist.sort() #sort(reverse=True) if you need a parallel run for many datasets - datasethandler-reverse.py
print("PHYLOHANDLER: Files to be analyzed: " + ", ".join(infilelist))
#outdir only needed for pasta
#print("PHYLOHANDLER: Data output to dir: " + outdir)
print("PHYLOHANDLER: Final relevant data will be in ./RESULTS")
print("PHYLOHANDLER: (some data in ./temp)")

#zoltan's homemade database renaming dictionary
taxarepl9 = {"actiCORYd": "Corynebacter diphteriae", "actiMYCOt": "Mycobacterium tuberculosis", 
"actiSTREc": "Streptomyces coelicolor", "alfaAZOSs": "Azospirillum sp. B506", 
"alfaMAGNm": "Magnetospirillum magneticum", "alfaNITRh": "Nitrobacter hamburgensis", 
"alfaRHODs": "Rhodobacter sphaeroides", "alfaRICKc": "Rickettsia conori", 
"amoACANc": "Acanthamoeba castellanii str neff", "amoCAVEf": "Cavenderia fasciculata", 
"amoDICTd": "Dictyostelium discoideum", "amoDICTp": "Dictyostelium purpureum", 
"amoENTAh": "Entamoeba histolytica", "amoFILAn": "Filamoeba nolandi", "amoPLANf": "Planoprotostelium fungivorum",
"amoPOLYp": "Polysphondylium pallidum pn500", "amoSEXAN": "Sexangularia sp. CB-2014", 
"amoSTYGA": "Stygamoeba regulata", "amoTIEGl": "Tieghemostelium lacteum", "amoVANEL": "Vannella", 
"apiBABEb": "Babesia bovis", "apiCHROv": "Chromera velia", "apiCRYPm": "Cryptosporidium muris", 
"apiEIMEt": "Eimeria tenella", "apiGREGn": "Gregarina niphandrodes", "apiNEOSc": "Neospora caninum", 
"apiPLASb": "Plasmodium berghei", "apiPLASg": "Plasmodium gallinaceum",
"apiTHEIe": "Theileria equi", "apiTOXOg": "Toxoplasma gondii", "apiVITbr": "Vitrella brassicaformis", 
"apiVORp": "Voromonas pontica", "apuTHECt": "Thecamonas trahens",
"archPICRt": "Picrophilus torridus", "archPYROa": "Pyrobaculum aerophilum", 
"archSULFt": "Sulfolobus tokodaii", "archTHERv": "Thermoplasma volcanium", "bcidBACTf": "Bacteroides fragilis", 
"bcidFLAVc": "Flavobacterium columnare", "bcidPORPg": "Porphyromonas gingivalis", 
"bcidPREVr": "Prevotella ruminicola", "betaBURKc": "Burkholderia cenocepacia", "betaCUPRn": "Cupriavidus necator", 
"betaRALSs": "Ralstonia solanacearum", "betaVERMe": "Verminephrobacter eiseniae", 
"chlaAMORC": "Amorphochlora amoebiformis", "chlaBIGna": "Bigelowiella natans", "chlaCHLOR": "Chlorarachnion reptans", 
"chlaLOTam": "Lotharella amoebiformis", "chlaLOTgl": "Lotharella globosa", "chlaLOTgZ": "Lotharella globosa", 
"chlaLOTHs": "Lotharella sp. CCMP622", "chlaLOToc": "Lotharella oceanica", "chlaPARTg": "Partenskyella glossopodia", 
"chryCHATs": "Chattonella subsalsa CCMP2191", "chryDINOB": "Dinobryon sp UTEXLB2267", 
"chryHETak": "Heterosigma akashiwo CCMP3107", "chryOCHRO": "Ochromonas sp. CCMP1393", 
"chryVAUCH": "Vaucheria litorea CCMP2940", 
"cilCLIMv": "Climacostomum virens", "cilICHTm": "Ichthyophthirius multifiliis","cilMESOD": "Mesodinium pulex", 
"cilLITOp": "Litonotus pictus","cilOXYTt": "Oxytricha trifallax",
"cilPARAt": "Paramecium tetraurelia", "cilPLATm": "Platyophrya macrostoma", "cilPROTa": "Protocruzia adherens", 
"cilPSEUp": "Pseudocohnilembus persalinus", "cilSTENc": "Stentor coeruleus", "cilTETRt": "Tetrahymena thermophila", 
"crypCHROO": "Chroomonas cf. mesostigmatica", "crypCRYpa": "Cryptomonas paramecium", "crypCRYsp": "Cryptophyceae sp. CCMP2293",
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
"dinSYMBs": "Symbiodinium sp.", "dinSYMBa": "Symbiodinium microadriaticum",
"eugANGOd": "Angomonas deanei", "eugBODOs": "Bodo saltans", 
"eugEUGgr": "Euglena gracilis", "eugEUGlo": "Euglena longa", "eugEUTc": "Eutreptiella gymnastica-like CCMP1594", 
"eugEUTn": "Eutreptiella gymnastica NIES-381", "eugEUTgn": "Eutreptiella gymnastica NIES-381", "eugLEISm": "Leishmania major", 
"eugLEPTp": "Leptomonas pyrrhocoris", "eugLEPTs": "Leptomonas seymouri",
"eugNEOBd": "Neobodo designis", "eugPARco": "Paratrypanosoma confusum", "eugPHYTO": "Phytomonas sp em1", 
"eugTRYPb": "Trypanosoma brucei", 
"excADUpa": "Aduncisulcus paluster Carplike_NY0171", "excBLATn": "Blattamonas nauphoetae", "excCARPm": "Carpediemonas membranifera", 
"excCHIca": "Chilomastix caulleri", "excCHIcu": "Chilomastix cuspidata", "excDYSNb": "Dysnectes brevis", 
"excERGcy": "Ergobibamus cyprinoides", "excGIARi": "Giardia intestinalis P15", "excHISTm": "Histomonas meleagridis", 
"excIOTAs": "Iotanema sp.", "excKIPFb": "Kipferlia bialata", "excMONOe": "Monocercomonoides exilis", "excNAEgr": "Naegleria gruberi", 
"excPERco": "Percolomonas cosmopolitus ATCC50343", "excPTRIp": "Paratrimastix pyriformis", 
"excSPIRs": "Spironucleus salmonicida ATCC50377", "excTREPs": "Trepomonas sp. PC1", "excTRIMm": "Trimastix marina", 
"extTTRIf": "Tritrichomonas foetus",
"firmBACIa": "Bacillus anthracis", "firmLISTm": "Listeria monocytogenes", "firmSTAPa": "Staphyllococcus aureus", 
"funASPEf": "Aspergillus fumigatus", "funCRYPn": "Cryptococcus neoformans", "funDEBAh": "Debaryomyces hansenii cbs767", 
"funLACCb": "Laccaria bicolor", "funNEURc": "Neurospora crassa", "funPUCCg": "Puccinia graminis", 
"funSCHIp": "Schizosaccharomyces pombe", 
"gamaSHEWb": "Shewanella baltica", "gamaVIBRc": "Vibrio cholerae", "gamaYERSp": "Yersinia pestis", 
"glauGLOEw": "Gloeochaete wittrockiana", "glauCYApa": "Cyanophora paradoxa", 
"glauCYPTg": "Cyanoptyche gloeocystis SAG4.97", "glauGLOwi": "Gloeochaete wittrockiana SAG46.84", 
"grnASTEs": "Asterochloris sp.", "grnAUXEp": "Auxenochlorella protothecoides",
"grnBATHp": "Bathycoccus prasinos", "grnCHLAl": "Chlamydomonas leiostraca", "grnCHLAl": "Chlamydomonas reinhardtii",
"grnCHLOs": "Chlorella sp.", "grnCHROz": "Chromochloris zofingiensis",
"grnCOCCs": "Coccomyxa subellipsoidea", "grnDUNAs": "Dunaliella salina", 
"grnDUNAt": "Dunaliella tertiolecta", 
"grnGONIp": "Gonium pectorale", "grnHELIs": "Helicosporidium sp.", 
"grnMICco": "Micromonas commoda", "grnMICpu": "Micromonas pusilla CCMP1545", "grnMICRZ": "Micromonas pusilla", 
"grnMONOn": "Monoraphidium neglectum", "grnNEPHp": "Nephroselmis pyriformis", "grnOSTRl": "Ostreococcus lucimarinus",
"grnOSTRm": "Ostreococcus mediterraneus", "grnOSTRt": "Ostreococcus tauri", "grnPICCL": "Picochlorum sp.", 
"grnPICCY": "Picocystis salinarum", "grnPOLYp": "Polytomella parva", "grnPOLYZ": "Polytomella parva", 
"grnPRASc": "Prasinococcus capsulatus", "grnPYRam": "Pyramimonas amylifera CCMP720", 
"grnPYRpa": "Pyramimonas parkeae CCMP726", "grnPYRpZ": "Pyramimonas parkeae", "grnTETRa": "Tetraselmis astigmatica", 
"grnTETRs": "Tetraselmis striata", "grnVOLVc": "Volvox carteri f. nagariensis", "hapCALCl": "Calcidiscus leptoporus", 
"hapCHRYt": "Chrysochromulina tobin", 
"hapEXANg": "Exanthemachrysis gayraliae", "hapIMANT": "Imantonia sp.", "hapISOCHg": "Isochrysis galbana", 
"hapPAVLs": "Pavlovales sp. CCMP2435", "hapPHAan": "Phaeocystis antarctica", "hapPHAgl": "Phaeocystis globosa",
"hapPHEOC": "Phaeocystis sp.", "hapPLEUc": "Pleurochrysis carterae", "hapPRYMp": "Prymnesium parvum", 
"hapSCYPH": "Scyphosphaera apsteinii", "hapEMILh": "Emiliania huxleyi", "haptEMIZ": "Emiliania huxleyi", 
"haptPLEUc": "Pleurochrysis carterae", "haptPRYMp": "Prymnesium parvum Texoma1", 
"hetPERCO": "Percolomonas cosmopolitus", "kytAMBOt": "Amborella trichopoda", "kytARABt": "Arabidopsis thaliana", 
"grnARABl": "Arabidopsis lyrata", "grnCHARb": "Chara braunii", 
"kytGLYCm": "Glycine max", "kytHORDv": "Hordeum vulgare", "kytORYZs": "Oryza sativa Japonica", 
"kytPHYSp": "Physcomitrella patens", "grnPHYSp": "Physcomitrella patens", "grnPOPtr": "Populus trichocarpa",
"kytSELAm": "Selaginella moellendorffii", "grnSELAm": "Selaginella moellendorffii", "grnSORGb": "Sorghum bicolor",
"kytSOlyc": "Solanum lycopersicum", "kytZEAma": "Zea mays", 
"metANOLc": "Anolis carolinensis", "metCAENe": "Caenorhabditis elegans", 
"metDAPHp": "Daphnia pulex", "metHELOr": "Helobdella robusta", "metLOAlo": "Loa loa",
"metLOTTg": "Lottia gigantea", 
"metNEMAv": "Nematostella vectensis", "metSCHIm": "Schistosoma mansoni", "metSTROp": "Strongylocentrotus purpuratus", 
"metTRICa": "Trichoplax adhaerens", "opiACANT": "Acanthoeca", "opiCAPSo": "Capsaspora owczarzaki",
"opiFONTa": "Fonticula alba",
"opiMONbr": "Monosiga brevicollis", "opiMONOb": "Monosiga brevicollis", 
"opiSALPr": "Salpingoeca rosetta", 
"redAHNFf": "Ahnfeltiopsis flabelliformis", "redBETAp": "Betaphycus philippinensis", 
"redCHONc": "Chondrus crispus", "redCOMPS": "Compsopogon caeruleus", "redCYANm": "Cyanidioschyzon merolae", 
"redERYTa": "Erythrolobus australicus", "redERYTm": "Erythrolobus madagascarensis", 
"redERYTm": "Erythrolobus madagascarensis", "redGALDs": "Galdieria sulphuraria", 
"redGRACv": "Gracilaria vermiculophylla", "redGRATt": "Grateloupia turuturu", "redHETSp": "Heterosiphonia pulchra",
"redMADAe": "Madagascaria erythrocladioides", "redMADAe": "Madagascaria erythrocladioides", 
"redPORae": "Porphyridium aerugineum SAG 1380-2", "redPORIp": "Porphyridium purpureum", 
"redPORum": "Porphyra umbilicalis", "redPORpu": "Porphyra purpurea", "redRHOma": "Rhodella maculata CCMP736", 
"redRHOSO": "Rhodosorus marinus", "redTIMSP": "Timspurckia oligopyrenoides", 
"rhiAMMOs": "Ammonia sp.", "rhiAMMOZ": "Ammonia sp.", 
"rhiELPHm": "Elphidium margitaceum", "rhiMINch": "Minchinia chitonis", "rhiPARTg": "Partenskyella glossopodia RCC365", 
"rhiPAULc": "Paulinella chromatophora", "rhiPLASb": "Plasmodiophora brassicae", "rhiRETIf": "Reticulomyxa filosa",
"rhiROSAL": "Rosalina", "rhiSORIT": "Sorites sp.", 
"strACHLh": "Achlya hypogyna", "strALBUl": "Albugo laibachii", "strAPHAi": "Aphanomyces invadans", 
"strAPLAN": "Aplanochytrium", "strAURAl": "Aurantiochytrium limacinum", "strAURAZ": "Aurantiochytrium limacinum", 
"strAUREN": "Aureococcus anophagefferens", "strAUREE": "Aureococcus anophagefferens", 
"strAUREa": "Aureococcus anophagefferens", "strAUREl": "Aureoumbra lagunensis", 
"strBICOS": "Bicosoecida sp. CB-2014", "strBLASh": "Blastocystis hominis", "strBOLID": "Bolidomonas sp.", 
"strBOLIp": "Bolidomonas pacifica", "strCAFro": "Cafeteria roenbergensis", "strCAFsp": "Cafeteria sp.", 
"strCAFca": "Cafeteria str Caron", "strCHATs": "Chattonella subsalsa", "strCHRRH": "Chrysoreinhardia sp.", 
"strCYCLc": "Cyclotella cryptica",
"strCYLIN": "Cylindrotheca closterium", "strDETON": "Detonula confervacea", "strDICTY": "Dictyocha speculum", 
"strDINOB": "Dinobryon sp.", "strDITYL": "Ditylum brightwellii", "strECTsi": "Ectocarpus siliculosus", 
"strEXTUs": "Extubocellulus spinifer", "strFRAGc": "Fragilariopsis cylindrus", 
"strFRAGk": "Fragilariopsis kerguelensis", "strFISTs": "Fistulifera solaris",
"strHETak": "Heterosigma akashiwo", 
"strHONDf": "Hondaea fermentalgiana", "strHYALa": "Hyaloperonospora arabidopsidis",
"strMALLO": "Mallomonas sp.", "strNANNg": "Nannochloropsis gaditana", "strNANNo": "Nannochloropsis oceanica", 
"strNITZs": "Nitzschia sp.", 
"strOCHRO": "Ochromonas sp.", "strOCHR2": "Ochromonadaceae sp. CCMP2298",
"strODONa": "Odontella aurita", "strPARAb": "Paraphysomonas bandaiensis", 
"strPELAG": "Pelagomonas calceolata", "strPELAs": "Pelagophyceae CCMP2097", "strPHAtr": "Phaeodactylum tricornutum", 
"strPHEOM": "Phaeomonas parva", 
"strPHYin": "Phytophtora infestans", "strPHYca": "Phytophthora capsici", "strPHYci": "Phytophthora cinnamomi",
"strPHYpa": "Phytophthora parasitica", "strPHYra": "Phytophtora ramorum", "strPHYso": "Phytophtora sojae", 
"strPINGU": "Pinguiococcus pyrenoidosus", 
"strPOTOs": "Poterioochromonas sp. DS", "strPSEUm": "Pseudo-nitzschia multistriata", 
"strPSEma": "Pseudo-nitzschia multistriata", "strPSEms": "Pseudo-nitzschia multiseries",
"strPTERd": "Pteridomonas danica", "strPYTHu": "Pythium ultimum var. sporangiiferum BR650", 
"strPYTHv": "Pythium vexans", "strRHIZC": "Rhizochromulina marina", "strSAPRd": "Saprolegnia diclina", 
"strSAPRp": "Saprolegnia parasitica", "strSCHYa": "Schizochytrium aggregatum",
"strSKEco": "Skeletonema costatum", "strSPUMv": "Spumella vulgaris", 
"strSTAUR": "Staurosira sp.", "strSYNCR": "Synchroma pusillum", "strTHAoc": "Thalassiosira oceanica",
"strTHAps": "Thalassiosira pseudonana", "strTHNEM": "Thalassionema frauenfeldii", 
"strTHNEn": "Thalassionema nitzschioides", "strTHRAc": "Thraustotheca clavata", "strTHRAU": "Thraustochytrium sp.", 
"strTHTRX": "Thalassiothrix antarctica", "strVAUCl": "Vaucheria litorea"}

#remove bad datasets and bad chars from names
taxonpattern = r'\[(.+)\]'
errors = False
failedfiles = []
for file in infilelist:
	extension = file.split(".")[-1]
	filename = file.replace("." + extension, "")
	generation = find_generation(filename)
	if generation == "":
		print("PHYLOHANDLER: Processing file: {}".format(file))
	else:
		print("PHYLOHANDLER: Processing file: {}, version {}".format(file, generation.replace("_", "")))
	if extension in ("fasta", "fas", "fst", "fa", "faa"):
		try:
			indataset = [x for x in SeqIO.parse(file, 'fasta')]
		except FileNotFoundError:
			#file is missing, check next file - 
			print("\tFile not found, skipping...")
			continue
	elif extension in ("phy", "phylip"):
		try:
			indataset = [x for x in SeqIO.parse(file, 'phylip')]
		except FileNotFoundError:
			#file is missing, check next file
			print("\tFile not found, skipping...")
			continue
	else:
		continue
	#here remove the infile so that parallel runs cannot access it:
	os.rename("{}".format(file), "RESULT/{}{}.{}".format(filename, generation, extension))
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
				elif args.no_dedupe:
					print("Duplicate found but deduplication turned off!")
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

	if args.aligner == "-":
		#assume aligned!
		os.system("mv safe-{0}.fasta trimfilt-{0}.fasta".format(filename))
	elif os.path.isfile("safe-{0}.aln".format(filename)):
		print("PHYLOHANDLER: Alignment detected, previous data not cleaned?")
	else:
		if args.aligner == "run_pasta.py":
			if args.alignerparams == "":
				command = "{0} -d protein -i safe-{1}.fasta -j {1} -o {2}".format(args.aligner, filename, outdir)
			else:
				command = "{0} {3} -d protein -i safe-{1}.fasta -j {1} -o {2}".format(args.aligner, filename, outdir, alignerparams)
		elif args.aligner == "mafft":
			if args.alignerparams == "":
				command = "{0} --maxiterate 1000 --localpair --thread {2} safe-{1}.fasta > safe-{1}.aln 2>{1}_mafft.log".format(args.aligner, filename, args.maxcores)
			else:
				command = "{0} {3} --thread {2} safe-{1}.fasta > safe-{1}.aln 2>{1}_mafft.log".format(args.aligner, filename, args.maxcores, alignerparams)
		os.system(command)
		print("PHYLOHANDLER: Issuing aligner\n" + command)

	#copy and rename PASTA alignment to current directory and issue trimal
	if args.aligner == "run_pasta.py":
		os.system("cp ./{1}/{0}.marker001.safe-{0}.aln ./safe-{0}.aln".format(filename, outdir))
		if args.trimalparams == "":
			command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -gt 0.3".format(filename) #-gappyout / -automated1 / -gt 0.3
		else:
			command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta {1}".format(filename, trimalparams)
		print("PHYLOHANDLER: Issuing trimmer:\n{}".format(command))
		os.system(command)
	elif args.aligner == "mafft":
		if args.trimalparams == "":
			command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -automated1".format(filename) #-gappyout / -automated1 / -gt 0.3
		else:
			command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta {1}".format(filename, trimalparams)
		print("PHYLOHANDLER: Issuing trimmer:\n{}".format(command))
		os.system(command)
	elif args.aligner == "-":
		#assume aligned!
		pass

	#check alignment length!
	length = AlignIO.read("trim-{0}.aln".format(filename), "fasta").get_alignment_length()
	if length < 20:
		print("PHYLOHANDLER: Retrimming alignment of lenght <20!")
		if args.aligner == "run_pasta.py":
			os.system("cp ./{1}/{0}.marker001.safe-{0}.aln ./safe-{0}.aln".format(filename, outdir))
		command = "trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -gt 0.1".format(filename)
		os.system(command)

	#open trimal-trimmed alignment for dumping any gaps-only sequences
	outfile1, outfile2 = "trimfilt-{0}.fasta".format(filename), "trimfilt-{0}.phy".format(filename)
	if args.aligner != "-":
		with open("error.log", "a") as error:
			try:
				trimalignmentfile = AlignIO.read("trim-{0}.aln".format(filename), "fasta")
				print("PHYLOHANDLER: Trimming finished, loading alignment")
			except FileNotFoundError:
				errors = True
				error.write("file:{}\tcould not find trimmed alignment\n".format(file))
				failedfiles.append(file)
				os.rename("safe-{}.aln".format(filename), "RESULT/nontrimmed{}{}-ali.fasta".format(filename, generation))
				print("PHYLOHANDLER: ERROR! Alignment not found! Quitting.")
				continue

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
				curlength = "{}_{:.2f}%aligned".format(r.id, 100*(len(str(r.seq).replace("-", "").replace("X", ""))/len(r.seq)))
				seq_d[r.id].append(curlength)
				##############
				##############
				##############
			count, length = len(filtalignmentfile), trimalignmentfile.get_alignment_length()
	else:
		count = len(seq_d.keys())
		length = AlignIO.read(outfile1, "fasta").get_alignment_length()

	print("PHYLOHANDLER: Post-trimming performed.")
	print("Trimming produced a file with {} sequences of {} sites".format(count, length))

	#convert trimfile to phylip format (phylobayes)
	if os.stat(outfile1).st_size > 0: #check for file size
		ffile = AlignIO.read(outfile1, "fasta")
		AlignIO.write(ffile, outfile2, "phylip-relaxed")
	else:
		print("#####\nWARNING: File {} has zero size\n#####".format(outfile1))

	print("PHYLOHANDLER: Now to writing rename file...")
	with open("rename-{}.txt".format(filename), "w") as renaming:
		for key,value in seq_d.items():
			try:
				percentalign = value[4]
			except IndexError:
				percentalign = value[1]
			renaming.write("{0}\t{1}\t{2}\n".format(value[1], value[0], percentalign)) #value[1][:50] for shorter names

	if length < 100:
		print("WARNING: Alignment shorter than 100 chars, consider less stringent trimming.")

	if args.treemaker != "none":
		if args.treemaker in ["iqtree-omp", "iqtree"]:
			if os.path.isfile("trimfilt-{}.fasta.treefile".format(filename)):
				if os.stat("trimfilt-{}.fasta.treefile".format(filename)).st_size > 0: #check for file size
					print("PHYLOHANDLER: Tree inference finished, previous data not cleaned?")
				else:
					print("PHYLOHANDLER: Tree inference finished, but treefile is corrupt. Please check")
			else:
				#check if iqtree present
				if is_tool("iqtree"):
					program = "iqtree"
				elif is_tool("iqtree-omp"):
					program = "iqtree-omp"
				elif os.path.isfile("./iqtree"):
					program = "./iqtree"
				else:
					quit("PHYLOHANDLER: FATAL ERROR! iqtree not found")

				#specify iqtree command
				if args.no_guide:
					if args.treeparams == "":
						treecommand = "-m LG+F+G -nt AUTO -ntmax {1} -s trimfilt-{0}.fasta 1>final-{0}_iqtree.log".format(filename, args.maxcores) #GTR20 only for very large datasets
					else:
						treecommand = "-nt AUTO -ntmax {1} -s trimfilt-{0}.fasta 1>final-{0}_iqtree.log {2}".format(filename, args.maxcores, treeparams)
				else:
					if args.treeparams == "":
						guidetreecommand = "-m LG+F+G -nt AUTO -ntmax {1} -s trimfilt-{0}.fasta -pre guide-{0} 1>guide-{0}_iqtree.log".format(filename, args.maxcores) #GTR20 only for very large datasets
						treecommand = "-m LG+C20+F+G -nt AUTO -ntmax {1} -s trimfilt-{0}.fasta -ft guide-{0}.treefile 1>final-{0}_iqtree.log".format(filename, args.maxcores) #GTR20 only for very large datasets
					else:
						guidetreecommand = "-m LG+F+G -nt AUTO -ntmax {1} -s trimfilt-{0}.fasta -pre guide-{0} 1>guide-{0}_iqtree.log {2}".format(filename, args.maxcores, treeparams) #GTR20 only for very large datasets
						treecommand = "-m LG+C20+F+G -nt AUTO -ntmax {1} -s trimfilt-{0}.fasta -ft guide-{0}.treefile 1>final-{0}_iqtree.log {2}".format(filename, args.maxcores, treeparams) #GTR20 only for very large datasets						
				if args.ufbootstrap:
					treecommand += " -bb 1000"
				elif args.bootstrap: #will not calculate bootstrap if UFBoot requested
					treecommand += " -b 1000"
				if args.shalrt:
					treecommand += " -alrt 1000"

				#start inference
				if args.no_guide:
					pass
				elif not os.path.isfile("guide-{0}.treefile".format(filename)):
					print("PHYLOHANDLER: Issuing software for guide tree inference:\n{} {}".format(program, guidetreecommand))
					os.system("{} {}".format(program, guidetreecommand))
				else:
					print("PHYLOHANDLER: Guide tree found, continuing...")
				print("PHYLOHANDLER: Issuing software for final tree inference:\n{} {}".format(program, treecommand))
				os.system("{} {}".format(program, treecommand))
		else:
			errors = True
			error.write("file:{}\tcould not find assign software for tree inference\n".format(file))
			print("PHYLOHANDLER: ERROR assigning software for tree inference!")
	bestmodel = "LG+F+G" #find using 'grep "Best-fit model:" final-{0}_iqtree.log'.format(filename)
	print("PHYLOHANDLER:", bestmodel)
	print("PHYLOHANDLER: Tree inference finished, post-processing result files...")
	#rename branches for presentation purposes:
	try:
		with open("trimfilt-{}.fasta.treefile".format(filename)) as intree,\
		open("final-{}.fasta.treefile".format(filename), "w") as outtree,\
		open("error.log", "a") as error:
			try:
				tree = intree.read()
				if args.mark_similarity:
					for key,value in seq_d.items():
						try:
							percentalign = value[4]
						except IndexError:
							percentalign = value[1]
						tree = tree.replace(key, percentalign)
				for key in taxarepl9:
					while key in tree:
						tree = tree.replace(key, taxarepl9[key])
				outtree.write(tree)
			except FileNotFoundError:
				errors = True
				error.write("file:{}\tcould not load treefile\n".format(file))
				failedfiles.append(file)
				print("PHYLOHANDLER: ERROR! Treefile not loaded! Skipping to next.")
		#copy all final files to the RESULTS directory and clean up
		if args.treemaker != "none":
			try:
				os.rename("trimfilt-{}.fasta.treefile".format(filename), "RESULT/{}_{}-iq.treefile".format(filename, generation))
				os.rename("final-{}.fasta.treefile".format(filename), "RESULT/_{}_{}-iq.treefile".format(filename, generation))
			except FileNotFoundError:
				#tree file failure
				errors = True
				error.write("file:{}\tcould not move treefiles\n".format(file))
				failedfiles.append(file)
				print("PHYLOHANDLER: ERROR! Treefile could not be moved found! Skipping to next.")
	except FileNotFoundError:
		#could not open tree file, but other files can be cleaned
		errors = True
		error.write("file:{}\tcould not find treefile\n".format(file))
		failedfiles.append(file)
		print("PHYLOHANDLER: ERROR! Treefile not found! Skipping to next.")

	#save the alignment files
	os.rename("trimfilt-{}.fasta".format(filename), "RESULT/{}{}-ali.fasta".format(filename, generation))
	os.rename("trimfilt-{}.phy".format(filename), "RESULT/{}{}-ali.phy".format(filename, generation))
	#os.rename("{}".format(file), "RESULT/{}{}.{}".format(filename, generation, extension))
	os.rename("rename-{}.txt".format(filename), "RESULT/{}{}-renamekey.tsv".format(filename, generation))
	os.system("mv *{}* temp".format(filename))
	#os.system("mv trim* temp")
	#os.system("mv guide* temp")
	print("#############\n")

if failedfiles == []:
	print("PHYLOHANDLER: All requested analyses finished. Hooray!")
else:
	print("PHYLOHANDLER: Requested analyses failed for: {}".format((", ").join(failedfiles)))

if errors:
	print("PHYLOHANDLER: Errors occurred during processing, please refer to error.log")
