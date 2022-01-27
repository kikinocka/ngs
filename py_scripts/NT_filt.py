#!/usr/bin/env python3

#courtesy of github.com/morpholino

import os,re,time,argparse
from Bio import SeqIO,Entrez
from ete3 import NCBITaxa
#http://etetoolkit.org/docs/2.3/tutorial/tutorial_ncbitaxonomy.html
ncbi = NCBITaxa()
Entrez.email = 'kika.zahonova@gmail.com'
#update at times:
#ncbi.update_taxonomy_database()

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
			errorfile.write(f"error retrieving taxid for {accession}\n")
			
	try:
		name2taxid = ncbi.get_name_translator([orgn])
		taxid = name2taxid[orgn][0]
	except:
		print(f"problem with {accession}:{orgn}, please try updating taxa.sqlite")
		taxid = 1
		keeptmpblastfile = True
		with open("errors.log", "a") as errorfile:
			errorfile.write(f"error retrieving taxid for {accession}:{orgn}\n")

	print("Organism retrieved:", orgn, taxid)

	return taxid

def force_taxid_nucl(accession):
	#lower data traffic with rettype=docsum, sufficient for taxid retrieval
	if "|" in accession:
		accession = accession.split("|")[3]
		#print(accession)
	try:
		nucl = Entrez.efetch(db='nucleotide', id=accession, rettype='docsum', retmode='xml')
		record = Entrez.read(nucl)[0]
		taxid = int(record["TaxId"])
		#name2taxid = ncbi.get_name_translator([orgn])
	except:
		print("Could not process", accession)
		keeptmpblastfile = True
		with open("manual.accession2taxid", "at") as out:
			out.write("{}\t".format(accession))
		return 1
	print("Organism retrieved:", taxid)

	return taxid

def force_taxid_gbnuc(accession):
	if "|" in accession:
		accession = accession.split("|")[3]
		#print(accession)
	try:
		nucl = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
		nucl_record = SeqIO.read(nucl, 'genbank')
		orgn = nucl_record.annotations['organism']
		name2taxid = ncbi.get_name_translator([orgn])
		taxid = name2taxid[orgn][0]
	except:
		print("Could not process", accession)
		keeptmpblastfile = True
		with open("manual.accession2taxid", "at") as out:
			out.write("{}\t".format(accession))
	print("Organism retrieved:", orgn, taxid)

	return taxid

def parse_sseqid(sseqid):
	#if sseqid.startswith("gi|"):
	if "|" in sseqid:
		accession = sseqid.split("|")[1]
	else:
		accession = sseqid
	return accession

def del_pX(nodename):
	partpattern = r'p\d+'
	try:
		partID = re.search(partpattern, nodename).group()
		nodename = nodename.replace(partID, "")
		#this also works
		#for hit in re.findall(partpattern, nodename):
		#	nodename = nodename.replace(hit, "")
	except:
		pass
		#print(f"No pattern in {nodename}")
	return nodename

def counter(c, freq):
	c += 1
	if c % freq == 0:
		print(c)
	return c

#previously fetched from NCBI
lookups = {1267768: [2, 1224, 28211, 204455, 31989, 1855413, 1267768], 
		  1379903: [2, 1224, 28211, 204455, 31989, 93682, 1379903], 
		  93064: [2, 1224, 28211, 204457, 41297, 13687, 93064], 
		  1514140: [2759, 2698737, 33634, 2696291, 2836, 589449, 33837, 232508, 210587, 1529381, 1514140], 
		  2494563: [28883, 10699, 196894, 2494563], 
		  1333996: [2, 1224, 28211, 356, 41294, 1649510, 1333996], 
		  301: [2, 1224, 1236, 72274, 135621, 286, 136841, 1232139, 301], 
		  2605946: [2, 1224, 28211, 204455, 31989, 58840, 2605946], 
		  2703868: [2759, 2608109, 2830, 2608131, 73020, 418951, 412163, 2703868], 
		  2741499: [2, 1224, 1236, 91347, 1903411, 613, 2741499], 
		  1470209: [2759, 2611352, 33682, 5653, 2704647, 2704949, 5654, 1470208, 1470209], 
		  41899: [2, 1224, 28216, 80840, 119060, 32008, 41899], 
		  303: [2, 1224, 1236, 72274, 135621, 286, 136845, 303], 
		  2015173: [2759, 33154, 33208, 6072, 33213, 33317, 1206794, 88770, 6656, 197563, 197562, 6960, 50557, 85512, 7496, 33340, 33392, 7399, 7400, 7434, 2153479, 36668, 213859, 2015172, 2015173], 
		  2213200: [2, 1783272, 201174, 1760, 85007, 85025, 1817, 2213200], 
		  2716812: [2, 1783272, 201174, 1760, 85013, 74712, 1854, 2716812], 
		  264483: [2759, 33154, 4751, 451864, 5204, 5302, 155616, 90883, 1851551, 107449, 264483], 
		  1577725: [2759, 2698737, 33634, 2696291, 2836, 33836, 33846, 33847, 29202, 1577724, 1577725], 
		  1417228: [2, 1224, 28216, 80840, 119060, 1822464, 261302, 1417228], 
		  2052683: [2759, 2698737, 33634, 4762, 121069, 4782, 1448052, 2052682, 2052683], 
		  1855912: [2, 57723, 1813735, 2211325, 2004797, 1855912], 
		  2510791: [2759, 2763, 2806, 2045261, 31468, 31469, 2510790, 2510791], 
		  1404864: [2, 1224, 28211, 356, 41294, 374, 1404864], 
		  2587401: [2759, 33154, 4751, 451864, 4890, 716545, 147538, 716546, 715989, 147550, 222544, 5139, 35718, 2609799, 2587401], 
		  418699: [2, 1224, 28216, 206389, 2008794, 12960, 418699], 
		  2511165: [2759, 2698737, 33634, 2696291, 5747, 425074, 425072, 2511164, 2511165], 
		  97495: [2759, 2608109, 2830, 2608131, 73020, 418951, 412163, 2703868], 
		  2081491: [2759, 2608109, 2830, 73026, 418969, 70451, 2081491]}

############################
###   PARSE PARAMETERS   ###
############################

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("starting {}".format(current_time))
#to parse arguments listed in the command after the script
parser = argparse.ArgumentParser(description='How to use argparse')
#dmnd blast input absolutely requires -outfmt 6 qseqid bitscore sseqid qcovhsp pident qlen length !
parser.add_argument('-i', '--infile', help='BLASTN outfile(s) to be taxified', required=True)
parser.add_argument('-d', '--work_dir', help='Working directory with the files', default=".")
#parser.add_argument('-a', '--skip_accession_pairing', help='Do not perform parsing prot.accession2taxid', action='store_true')
#input fasta names can be inferred from blast input
parser.add_argument('-nt', '--fasta_nt', help='Nucleotide fasta for parsing', default="")
parser.add_argument('-q', '--qcov_threshold', help='query coverage threshold', default=50)
parser.add_argument('-p', '--pident_threshold', help='percent identity threshold', default=75)
parser.add_argument('-g', '--good_groups', nargs='+', help='List of good taxonomic groups', default=["Amoebozoa"])
parser.add_argument('-t', '--test_mode', help='Testing mode to allow checking tmp files', action="store_true")

args = parser.parse_args()

filetype = "blast"
transcriptome = "trinity"
if args.infile == "batch":
	files = [x for x in os.listdir(".") if x.endswith(filetype)]
else:
	files = args.infile.split(",")
print("to analyze:", ", ".join(files))

if args.work_dir != ".":
	os.chdir(args.work_dir)

qthr = float(args.qcov_threshold)
pthr = float(args.pident_threshold)

goodgroups = set()
goodgroupsrep = ""

for orgn in args.good_groups:
	if ncbi.get_name_translator([orgn]):
		goodgroups.add(orgn)
	else:
		print("Unrecognized taxon: {}".format(orgn))
		continue
	if not goodgroupsrep:
		goodgroupsrep = orgn

##############
###  MAIN  ###
##############
#quit("Use only for files for which fastas are present in folder")

taxids = {}
try:
	with open("subset.accession2taxid") as taxidfile:
		print("reading accession2taxid...")
		for l in taxidfile:
			l = l.strip().split("\t")#.decode('utf8')
			taxids[l[0]] = l[1]
except:
	print("accession2taxid file not found, skipping")

for i,filepath in enumerate(files):
	path, file = os.path.split(filepath)
	print("\n\n======\nAnalyzing", file)
	# find nucleotide fasta for processing
	if args.fasta_nt == "":
		ntfasta = file.replace(filetype, "fasta")
		if not os.path.exists(ntfasta):
			print("Nucleotide fasta missing/unspecified, nt fasta output muted")
			writent = False
	else:
		ntfasta = args.fasta_nt
		writent = True

	dataset = file.split(".")[0]
	if os.path.isdir("./tmp".format(dataset)) == False:
		os.system("mkdir tmp".format(dataset))
		print("tmp directory created")
	if os.path.isdir("./contaminants".format(dataset)) == False:
		os.system("mkdir contaminants".format(dataset))
		print("contaminant directory created")
	if os.path.isdir("./{}_NT".format(dataset)) == False:
		os.system("mkdir {}_NT".format(dataset))
		print("target directory created")
	statfile = dataset + "_report.txt"
	filt = "tmp/{}_filt.txt".format(dataset)
	check = "tmp/{}_check.txt".format(dataset)
	#use tmpblast file to retrieve taxids if the script crashes on NCBI requests
	#cut -f 3,6 tmp/<blastresult>.tmp >> subset.accession2taxid
	tmpblast =  "tmp/{}.tmp".format(file)
	keeptmpblastfile = False
	cont_bact = list()
	cont_fungal = list()
	cont_animal = list()
	cont_plant = list()
	#cont_parabasalia = list()
	cont_other = list()
	species = set()
	goodscafs = {}
	outscafs = {}
	scaf_d = {}
	ranks = {}
	#replacement = {"319938": "288004", "1317118": "1379903", "427920": "1983720"}
	distribution = {goodgroupsrep: 0}
	c = 0 #we need a process monitor
	with open(file) as infile, \
	open(tmpblast, "w") as outfile,\
	open(check, "w") as checkfile,\
	open(filt, "w") as filtfile:
		table = infile.read().split("\n")
		#print("{}".format(len(table)))
		print("To be analyzed: {}".format(len(table)))
		for line in table:
			c += 1
			if c % 10000 == 0:
				print(c)
			if len(line.split("\t")) != 1:
				line = line.split("\t")
				
				#First create a dictionary item
				if len(line) == 6:
					#this is a blastn output, so additional columns can be used for filtering
					score, qcovs, pident = float(line[2]), float(line[4]), float(line[5])
				else:
					print("Not enough columns")
					continue
				try:
					query = line[0]
					query_scaf = del_pX(query)
					if query_scaf not in goodscafs:
						goodscafs[query_scaf] = 0
						outscafs[query_scaf] = 0
					#hitid = line[3]
				except IndexError:
					#this should not happen, but testing what other errors might happen
					continue

				if query not in scaf_d.keys():
					scaf_d[query] = {"score": score, "qcovs": qcovs, "pident": pident, "taxid": 0, "rank": [""]}
				elif score > scaf_d[query]["score"]:
					#keep the best scoring hit
					scaf_d[query] = {"score": score, "qcovs": qcovs, "pident": pident, "taxid": 0, "rank": [""]}
				else:
					continue

				#Second get taxid and lineage ranks
				if qcovs < 20: #ignore queries not sufficiently covered
					continue
				accession = parse_sseqid(line[3])
				taxid = line[1]
				if accession in taxids:
					taxid = taxids[accession]
					lineage = ncbi.get_lineage(taxid)[2:]
				elif taxid in ["N/A", "0"]:
					taxid = force_taxid_nucl(accession)
					lineage = ncbi.get_lineage(taxid)[2:]
				elif taxid in lookups:
					lineage = lookups[taxid]
				else:
					try:
						if ";" in taxid:
							print("Multiple taxids:", taxid)
							taxid = taxid.split(";")[0]
							#for x in taxid.split(";"):
							#	print(ncbi.get_lineage(x)[2:])
						lineage = ncbi.get_lineage(taxid)[2:]
					except ValueError:
						print(f"Invalid taxid, force checking: {line} {accession}")
						taxid = force_taxid_nucl(accession)
						lineage = ncbi.get_lineage(taxid)[2:]
						lookups[taxid] = lineage
				names = ncbi.get_taxid_translator(lineage)
				rank = [names[taxid] for taxid in lineage]

				outfile.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(line[0], line[2], line[3], line[4], line[5], taxid))
				
				scaf_d[query]["taxid"] = taxid
				scaf_d[query]["rank"] = rank
				
				#Third, prepare ranks to print and store distribution data
				if query_scaf not in ranks:
					ranks[query_scaf] = set()
				if taxid not in species:
					species.add(taxid)
					#orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					#print("{}\t{}".format(orgn, "_".join(rank)))
				if any(x in rank for x in goodgroups):
					#print(rank)
					orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					scaf_d[query]["rank"] = [goodgroupsrep]
					ranks[query_scaf].add(orgn)
					group = goodgroupsrep
					distribution[goodgroupsrep] += 1
				elif "Metazoa" in rank:
					#Metazoan ranking is too detailed
					try:
						#print(rank[7])
						group = "Opisthokonta_Metazoa_" + rank[7]
						if group not in distribution:
							distribution[group] = 1
						else:
							distribution[group] += 1
					except IndexError:
						if not "Trichoplax" in rank:
							print("out of range:" + "_".join(rank))
					ranks[query_scaf].add(group)
				else:
					#print(rank)
					group = "_".join(rank[1:3])
					#print(group)
					if group == "":
						#no subgroups defined
						try:
							group = rank[0]
						except IndexError:
							group = "N/A"
					if group not in distribution:
						distribution[group] = 1
					else:
						distribution[group] += 1
					ranks[query_scaf].add(group)
				
				#Write ranks to a report
				try:
					checkfile.write(f"{query}\t{rank[1]}\n")
				except IndexError:
					#this is most likely an unranked bacterium
					#print("\tweird rank", rank)
					checkfile.write(f"{query}\t{rank}\n")

				#Write ranks of the filtered files
				if query in goodscafs:
					filtfile.write(f"{query}\t{rank}\n")

		#ANY FILTER CAN BE APPLIED			
		for query in scaf_d:
			query_scaf = del_pX(query)
			item = scaf_d[query]
			qcovs, pident, rank = item["qcovs"], item["pident"], item["rank"]
			if qcovs > qthr and pident > pthr: #Sebastian's thresholds:
				#Usually 80% identity and at least 50% coverage of the transcript by the hits. 
				#LGT's don't have such a high identity towards any bacteria usually. 
				#these are high-similarity hits, so sort the sequences as contaminants to subsets:
				if "Bacteria" in rank:
					cont_bact.append(query_scaf)
					outscafs[query_scaf] += 1
				elif "Fungi" in rank:
					cont_fungal.append(query_scaf)
					outscafs[query_scaf] += 1
				elif "Metazoa" in rank:
					cont_animal.append(query_scaf)
					outscafs[query_scaf] += 1
				elif "Streptophyta" in rank:
					cont_plant.append(query_scaf)
					outscafs[query_scaf] += 1
				#elif "Parabasalia" in rank:
				#	cont_parabasalia.append(query_scaf)
				#	outscafs[query_scaf] += 1
				elif goodgroupsrep in rank:
					goodscafs[query_scaf] += 1
				else:
					#modify this if organism of interest is in NT
					#if seqID has been added to goodscafs, this will be ignored
					cont_other.append(query_scaf)
					outscafs[query_scaf] += 1
					#print(rank)
			elif any(x in rank for x in goodgroups):
				goodscafs[query_scaf] += 1
			else:
				#this has no good hit in nt:
				goodscafs[query_scaf] += 1
				if "Bacteria" in rank:
					#cont_bact.append(query_scaf)
					outscafs[query_scaf] += 1
	seqlen = 0
	
	if writent == True:
		in_nucl = SeqIO.parse(ntfasta, "fasta")
		out_nucl = open("{0}_NT/{0}.{1}.NTfilt.fasta".format(dataset, transcriptome), "w")
		out_bact = open("contaminants/{0}_bact.fasta".format(dataset), "w")
		out_fungal = open("contaminants/{0}_fungal.fasta".format(dataset), "w")
		out_animal = open("contaminants/{0}_animal.fasta".format(dataset), "w")
		out_plant = open("contaminants/{0}_plant.fasta".format(dataset), "w")
		#out_para = open("contaminants/{0}_para.fasta".format(dataset), "w")
		out_other = open("contaminants/{0}_other.fasta".format(dataset), "w") #assuming this organism is not in nr
		for seq in in_nucl:
			if goodscafs.get(seq.name, 0) > outscafs.get(seq.name, 0):
				out_nucl.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
				seqlen += len(seq.seq)			
				#out_para.write("{}:\t{}\t{}\n".format(seq.name, goodscafs.get(seq.name, 0), outscafs.get(seq.name, 0)))
			#there might be a lot of low-coverage hits, but most are from bacteria
			elif cont_bact.count(seq.name) > goodscafs.get(seq.name, 0):
				out_bact.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			#note that the following are only high-similarity, high-coverage hits
			elif cont_fungal.count(seq.name) > goodscafs.get(seq.name, 0):
				out_fungal.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			elif cont_animal.count(seq.name) > goodscafs.get(seq.name, 0):
				out_animal.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			elif cont_plant.count(seq.name) > goodscafs.get(seq.name, 0):
				out_plant.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			#elif cont_parabasalia.count(seq.name) > goodscafs.get(seq.name, 0):
			#	out_para.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			elif cont_other.count(seq.name) > goodscafs.get(seq.name, 0):
				out_other.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
			else:
				#no nr blast hit:
				out_nucl.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
				seqlen += len(seq.seq)
				#out_para.write("{}:\t{}\t{}\n".format(seq.name, goodscafs.get(seq.name, 0), outscafs.get(seq.name, 0)))
		print("{} bases extracted".format(seqlen))
		out_nucl.close()
		out_bact.close()
		out_fungal.close()
		out_animal.close()
		out_plant.close()
		#out_para.close()
		out_other.close()
	
	print("{} different species as hits".format(len(species)))
	with open(statfile, "w") as result:
		if seqlen != 0:
			result.write("{} bases extracted\n".format(seqlen))
		groups = list(distribution.keys())
		groups.sort()

		g = goodgroupsrep
		print("{}\tsequences of {}".format(distribution[g], g))
		result.write("{}\tsequences of {}\n".format(distribution[g], g))
		groups.remove(goodgroupsrep)

		for g in groups:
			print("{}\tsequences of {}".format(distribution[g], g))
			result.write("{}\tsequences of {}\n".format(distribution[g], g))
	if not args.test_mode:
		os.system("mv {} {}_NT/".format(file, dataset))
		for tmpfile in [filt, check]:
			os.system("rm {}".format(tmpfile))
	if keeptmpblastfile == False:
		os.system("rm {}".format(tmpblast))
	print("now, run quast to analyze contaminants:")
	print("quast {0}_NT/*fasta -o ~/quast/{0}_NT --threads 4".format(dataset))

print("NCBI taxid lookups", lookups)
print("finished sorting")
