#!/usr/bin/python

#courtesy of github.com/morpholino

#use p2 or uncomment the decode attribute on l.66
import argparse, gzip, time, os
from Bio import Entrez,SeqIO
from ete3 import NCBITaxa
ncbi = NCBITaxa()
#update at times:
#ncbi.update_taxonomy_database()

Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = "ed51bca6c73792ecc692af11ff762b72a008"

def force_taxid_prot(accession):
	print("Requesting", accession)
	if "|" in accession:
		#this is a bit of a problem
		if len(accession.split("|")) == 4:
			#this happened with old-style headers, now NCBI does not use GI
			accession = accession.split("|")[3]
		else:
			#there should be just one item in accession.split("|") that is not an empty string
			#also, it is supposedly never the first item in such headers
			accession  = [x for x in accession.split("|")[1:] if x not in [""]][0]
		#print(accession)
		
	#Efetch will still fail if a pir| accession is passed!
	try:
		prot = Entrez.efetch(db='protein', id=accession, rettype='gb', retmode='text')
		prot_record = SeqIO.read(prot, 'genbank')
		orgn = prot_record.annotations['organism']
	except:
		print("Could not process", accession)
		taxid = 1
		keeptmpblastfile = True
		with open("errors.log", "a") as errorfile:
			errorfile.write("error retrieving taxid for {}\n".format(accession))
			
	try:
		name2taxid = ncbi.get_name_translator([orgn])
		taxid = name2taxid[orgn][0]
	except:
		print("problem with {}:{}, please try updating taxa.sqlite".format(accession, orgn))
		taxid = 1
		keeptmpblastfile = True
		with open("errors.log", "a") as errorfile:
			errorfile.write("error retrieving taxid for {}:{}\n".format(accession, orgn))

	print("Organism retrieved:", orgn, taxid)

	return taxid

#########################
###  READ PARAMETERS  ###
#########################

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("starting {}".format(current_time))
#to parse arguments listed in the command after the script
parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-i', '--infile', help='Diamond outfile to be taxified', required=True)
parser.add_argument('-b', '--blast_type', help='BLAST type (suffix)', default="blastp")
parser.add_argument('-s', '--sseqid_index', help='Zero-based index of the sseqid column in BLAST output', default=2)
parser.add_argument('-w', '--write_taxified', help='Write taxified dmnd.out', action='store_true')

args = parser.parse_args()
sidx = int(args.sseqid_index)

infile = args.infile
path,_ = os.path.split(infile)
if path == "":
	path = "."
subsetfile = "{}/subset.accession2taxid".format(path)

########################
###       MAIN       ###
########################

accessionlist = set()
with open(infile) as dmndin:
	c = 0
	for l in dmndin:
		l = l.strip().split("\t")
		#the input format expected by default:
		#qseqid bitscore sseqid qcovhsp pident qlen length
		if "|" in l[sidx]:
			#this is a bit of a problem
			if len(l[sidx].split("|")) == 4:
				#this happened with old-style headers, now NCBI does not use GI
				accession = l[sidx].split("|")[3]
			else:
				#there should be just one item in accession.split("|") that is not an empty string
				#also, it is supposedly never the first item in such headers
				accession  = [x for x in l[sidx].split("|")[1:] if x not in [""]][0]
			accessionlist.add(accession)
		else:
			accessionlist.add(l[sidx])
		c += 1
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
print("parsing blast output finished")
print("{} unique records found".format(c))

taxids = {}
#renew after NR update:
#os.system("wget -O prot.accession2taxid.FULL.gz ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/prot.accession2taxid.FULL.gz")
with gzip.open("/mnt/mokosz/home/zoli/DMND/prot.accession2taxid.FULL.gz", mode='rb') as taxidfile, open(subsetfile, "w") as subset:
#CAUTION! file named prot.accession2taxid.gz has four columns and lacks some of the accessions!
#with open("subset.accession2taxid") as taxidfile, open("subset", "w") as subset:
	print("filtering accession2taxid... (will take ~70 minutes!)")
	c = 0
	for l in taxidfile:
		#c += 1
		#if c % 10000000 == 0:
		#	print("{}M".format(c/1000000))
		l = l.strip().split("\t")#.decode('utf8')
		try:
			if l[0] in accessionlist:
				subset.write("{}\n".format("\t".join(l)))
				taxids[l[0]] = l[1]
				accessionlist.remove(l[0])
		except IndexError:
			print(l, "not enough columns")
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
print("writing accession2taxid subset finished")
if len(accessionlist) > 0:
	print("Records remained in accession list, writing...")
	with open(path + "/records.list", "w") as records:
		records.write("\n".join(accessionlist))

if args.write_taxified == True:	
	print("Taxified output requested, writing...")
	with open(infile) as dmndin, open(infile.replace("out", args.blast_type), "w") as result:
		for l in dmndin:
			l = l.strip().split("\t")
			#the input format expected:
			#qseqid bitscore sseqid qcovhsp pident qlen length
			#[0]    [1]      [2]    [3]     [4]    [5]  [6]
			#default input is:
			#qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore
			#the output format is:
			#query taxid  bitscore hitID qcovs pident
			sseqid = l[sidx]
			if sseqid in taxids:
				taxid = taxids[sseqid]
			elif len(sseqid.split("|")) not in (1,4):
				sseqid  = [x for x in sseqid.split("|")[1:] if x not in [""]][0]
				taxid = taxids.get(sseqid, 1)
			elif sseqid == "*":
				taxid = 1
			else:
				taxid = force_taxid_prot(sseqid)
			qcov = l[3] #or alternatively float(l[-1])/float(l[-2])*100
			result.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(l[0], taxid, l[1], sseqid, qcov, l[4]))
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print(current_time)
	print("writing blast output finished, success!")
