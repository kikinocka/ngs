import os
import csv
import urllib
from Bio import Entrez,SeqIO


Entrez.email = "zoltan.fussy@google.com" 

#this script was designed to extract accessions from a table... 
#see homedir/genomes/chromera/plastid proteome/ribosomals_list.txt
#but can work with other tsv-type or fasta data

def getseq(accession):
	try:
		handle = Entrez.efetch(db="protein", id=accession, rettype="fasta", retmode="XML")
		record = Entrez.read(handle)
		try:
			sequence = record[0]['TSeq_sequence']
		except KeyError:
			sequence = "-"
	except:
		print("error retrieving", accession)
		sequence = "-"
	return sequence

#######################
## change to workdir ##
#######################

if os.path.isdir("/Users/morpholino/OwnCloud/"):
	home = "/Users/morpholino/OwnCloud/"
elif os.path.isdir("/Volumes/zoliq data/OwnCloud/"):
	home = "/Volumes/zoliq data/OwnCloud/"
else:
	print("Please set a homedir")

defdir = "genomes/euglena longa/fetch/"
wd = home + defdir
os.chdir(wd)

############
### MAIN ###	
############

#pick what sort of files you need to parse:
filetype =  ["fasta", "renamefile", "tsv", "errorfile-missing", "list"][2]

badchars = ("|@+,:;()'")
allowed = ("fasta", "fas", "fst", "phy", "phylip")

if filetype == "renamefile":
	files = [x for x in os.listdir(".") if x.startswith("rename")]
	for file in files:
		newfile = "new_" + file
		print("Processing file " + file)
		with open(file) as f, open(newfile, "w") as out:
			for l in f:
				if l.startswith("gi_"):
					gid = l.split("_")[1]
					handle = Entrez.efetch(db="protein", id=gid, rettype="fasta", retmode="XML")
					record = Entrez.read(handle)
					try:
						accession = record[0]['TSeq_accver']
					except KeyError:
						accession = l.split("\t")[0].replace("gi_{}_".format(gid), "")
					#print(record)
					annot = "".join([x for x in record[0]['TSeq_defline'] if x not in badchars])
					#print(annot)
					out.write("{}\t{}_{}\n".format(l.split("\t")[0], accession, annot))
					#record['TSeq_taxid'] and record['TSeq_orgname'] also possible
				else:
					out.write(l)

elif filetype == "fasta":
	files = [x for x in os.listdir(".") if x.endswith("fasta")]
	files = [x for x in files if not x.startswith("new_")]
	#test purposes only: files = ["STT3_pfam02516.fasta"]
	for file in files:
		newfile = "new_" + file
		print("Processing file " + file)
		f = SeqIO.parse(file, "fasta")
		with open(newfile, "w") as out, open("errors_fetch.log", "w") as errorlog:
			for l in f:
				if l.name.startswith("gi|"):
					gid = l.name.split("|")[1]
					handle = Entrez.efetch(db="protein", id=gid, rettype="fasta", retmode="XML")
					record = Entrez.read(handle)
					try:
						accession = record[0]['TSeq_accver']
					except KeyError:
						accession = l.name.replace("gi|{}|".format(gid), "")
					#print(record)
					annot = "".join([x for x in record[0]['TSeq_defline'] if x not in badchars])
					#print(annot)
					out.write(">{} {}\n{}\n".format(accession, annot, l.seq))
					#record['TSeq_taxid'] and record['TSeq_orgname'] also possible
				elif "|" in l.description:
					codepos = l.description.find('|')
					code = l.description[:codepos]
					print(code)
					res = u.retrieve(code, frmt='fasta', database='uniprot')
					reshead = res.split("\n")[0]
					try:
						out.write("{}\n{}\n".format(reshead, l.seq)) #extract seq header
						#out.write(res) #write fasta as is
					except TypeError:
						print(res)
						errorlog.write("{}\t{}\n".format(code, "could not be retrieved"))
						out.write(">{}\n{}\n".format(l.description, l.seq))
				else:
					description = "".join(x for x in l.description if x not in badchars)
					out.write(">{}\n{}\n".format(description, l.seq))

#this part is to retrieve accessions written in a table where the firs columns is the taxon and second is the accession
elif filetype == "tsv":
	files = [x for x in os.listdir(".") if x.endswith("tsv")]
	#test purposes only: files = ["fetchlist.tsv"]
	#assumes seq description in the first column and origin=species in the first row
	for file in files:
		missing = file.replace(".tsv", "") + "-missing.txt"
		newfile = file.replace(".tsv", "") + "-get.fasta"
		print("Processing file " + file)
		f = csv.reader(open(file), delimiter="\t", skipinitialspace=False)
		with open(newfile, "w") as out, open(missing, "w") as error:
			for c,l in enumerate(f):
				if c == 0:
					species = l.copy()
					continue
				else:
					name = l[0]
					accessions = l[1:]
					print("processing table, line {}: {}".format(c, l))
				for i,a in enumerate(accessions):
					tag = "{}_{}".format(name, species[i+1])
					if "@" in a:
						borders = a.split("@")[0].split("-")
						queries = [a.split("@")[1]]
						print("sequence splitting not finished")
					elif "&" in a:
						queries = a.split("&")
						for q in queries:
							seq = getseq(q)
							if seq != "-":
								out.write(">{}_{}\n{}\n".format(q, tag, seq))
								print("getseq function on joined accessions... success!")
							else:
								error.write("{}\t{}\n".format(q, tag))
								print("getseq function on joined accessions... failed. Added to missing list.")
					elif a in ["", "-"]:
						pass
					else:
						seq = getseq(a)
						if seq != "-":
							out.write(">{}_{}\n{}\n".format(a, tag, seq))
							print("getseq function on single accession... success!")
						else:
							error.write("{}\t{}\n".format(a, tag))
							print("getseq function on single accession... failed. Added to missing list.")

#this part is to search for missed sequences in local datasets, need a bit adjustment (set local files etc.):
elif filetype == "errorfile-missing":
	files = [x for x in os.listdir(".") if x.endswith("-missing.txt")]
	for file in files:
		missingdict = {}
		missing = file.replace("missing", "missing2")
		newfile = file.replace(".txt", "") + "-err_get.fasta"
		with open(file) as f:
			for l in f:
				data = l.strip().split("\t")
				if len(data) == 2:
					missingdict[data[0]] = data[1]
		with open(missing, "w") as error, open(newfile, "w") as result:
			infasta1 = SeqIO.parse(home + "genomes/sources/euks/PlasmoDB-40_Pfalciparum3D7_AnnotatedProteins.fasta", "fasta")
			for seq in infasta1:
				name = seq.name.split(".")[0]
				if name in missingdict:
					tag = missingdict[name]
					result.write(">{}_{} {}\n{}\n".format(name, tag, seq.description, seq.seq))
					del missingdict[name]

			infasta2 = SeqIO.parse(home + "genomes/sources/euks/ToxoDB-40_TgondiiME49_AnnotatedProteins.fasta", "fasta")
			for seq in infasta2:
				name = seq.name.split("-")[0]
				if name in missingdict:
					tag = missingdict[name]
					result.write(">{}_{} {}\n{}\n".format(name, tag, seq.description, seq.seq))
					del missingdict[name]
					altname = name.replace("TGME49_2", "TGME49_0").replace("TGME49_3", "TGME49_1")
					try:
						del missingdict[altname]
					except KeyError:
						print(altname, "not in dict")
			
			infasta3 = SeqIO.parse(home + "genomes/sources/euks/cyanidioschyzon_aa.fasta", "fasta")
			for seq in infasta3:
				name = seq.name.split(".")[0]
				if name in missingdict:
					tag = missingdict[name]
					result.write(">{}_{} {}\n{}\n".format(name, tag, seq.description, seq.seq))
					del missingdict[name]
			
			for left in missingdict:
				error.write("{}\t{}\n".format(left, missingdict[left]))

#this part is for a list of accession numbers
elif filetype == "list":
	files = [x for x in os.listdir(".") if x.endswith(".txt")]
	files = [x for x in files if not x.endswith("-missing.txt")]
	#test purposes only: files = ["fetchlist.txt"]
	for file in files:
		missing = file.replace(".txt", "") + "-missing.txt"
		newfile = file.replace(".txt", "") + "-get.fasta"
		print("Processing file " + file)
		f = open(file)
		with open(newfile, "w") as out, open(missing, "w") as error:
			for l in f:
				gid = l.strip()
				print(gid)
				try:
					handle = Entrez.efetch(db="protein", id=gid, rettype="fasta", retmode="XML")
					record = Entrez.read(handle)
				except urllib.error.HTTPError:
					error.write("{}\n".format(gid))
					print("skipped!")
					continue
				try:
					accession = record[0]['TSeq_accver']
					annot = "".join([x for x in record[0]['TSeq_defline'] if x not in badchars])
					sequence = record[0]['TSeq_sequence']
					out.write(">{}\t{}\n{}\n".format(accession, annot, sequence))
				except KeyError:
					error.write("{}\n".format(gid))
					#accession = l.split("\t")[0].replace("gi_{}_".format(gid), "")
				#print(record)
				#print(annot)


"""
#Swissprot works in a similar way:
>>> from Bio import ExPASy,SwissProt

>>> handle = ExPASy.get_sprot_raw(hitid)
>>> record = SwissProt.read(handle)
>>> dir(record)
['__doc__', '__init__', '__module__', 'accessions', 'annotation_update',
'comments', 'created', 'cross_references', 'data_class', 'description',
'entry_name', 'features', 'gene_name', 'host_organism', 'keywords',
'molecule_type', 'organelle', 'organism', 'organism_classification',
'references', 'seqinfo', 'sequence', 'sequence_length',
'sequence_update', 'taxonomy_id']

#Uniprot uses a different library:
from bioservices import UniProt
u = UniProt(verbose=False)
res = u.retrieve("V4LCC8", frmt='xml', database='uniprot') #or fasta/gff frmt
res = u.retrieve("V4LCC8", frmt='txt', database='uniprot')
print(res)
"""