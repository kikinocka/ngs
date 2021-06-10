#!/usr/bin/env python3

#courtesy of github.com/morpholino

import os,re,time,argparse
from Bio import SeqIO,Entrez
from ete3 import NCBITaxa
#http://etetoolkit.org/docs/2.3/tutorial/tutorial_ncbitaxonomy.html
ncbi = NCBITaxa()
Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = "ed51bca6c73792ecc692af11ff762b72a008"
#update at times:
#ncbi.update_taxonomy_database()


def assembly_methods(blastline):
	# Infer the assembler and protein predictor from blast input or faa file
	seqname = blastline.split()[0].replace(">", "")
	assembler, predictor = "NA", "NA"
	if "::" in seqname:
		predictor = "transdecoder"

	if seqname.startswith("TRINITY"):
		assembler = "trinity"
		if seqname.split("_")[-2].startswith("i"):
			predictor = "prodigal"
	elif seqname.startswith("NODE"):
		assembler = "spades"
		if seqname.split("_")[-3] == "cov":
			predictor = "prodigal"
	
	return assembler, predictor


def get_scaffold(predictor, seqname):
	if predictor == "transdecoder":
		return seqname.split("::")[1]
	elif predictor == "prodigal":
		return "_".join(seqname.split("_")[:-1])
	return seqname


def parse_faa(assembler, predictor, fasta_aa):
	# scaflen requires assembly is made by SPAdes!
	# For Trinity assemblies, this scaffold lengths are inferred from nt assembly.
	faa_file = SeqIO.parse(fasta_aa, "fasta")
	faa_d = {}

	if assembler == "spades":
		if predictor == "transdecoder":
			coordsregex = r":(\d+)-(\d+)\("
			for seq in faa_file:
				header = seq.description
				coords = (float(re.search(coordsregex, header).group(1)), 
						  float(re.search(coordsregex, header).group(2)))
				coords = (min(coords), max(coords))
				scaflen = float(header.split("_")[3])
				#print(coords, scaflen)
				genelen = coords[1] - coords[0] + 1
				faa_d[seq.name] = {"coords": coords, "gene_len": genelen, "scaf_len": scaflen}
		elif predictor == "prodigal":
			for seq in faa_file:
				header = seq.description
				coords = (float(header.split("#")[1]), 
						  float(header.split("#")[2]))
				scaflen = float(header.split("_")[3])
				#print(coords, scaflen)
				genelen = coords[1] - coords[0] + 1
				faa_d[seq.name] = {"coords": coords, "gene_len": genelen, "scaf_len": scaflen}
	elif assembler == "trinity":
		if predictor == "transdecoder":
			coordsregex = r":(\d+)-(\d+)\("
			for seq in faa_file:
				header = seq.description
				coords = (float(re.search(coordsregex, header).group(1)), 
						  float(re.search(coordsregex, header).group(2)))
				coords = (min(coords), max(coords))
				scaflen = scaffolds_d.get(header.split("::")[1], {"length": 1})["length"]
				#print(coords, scaflen)
				genelen = coords[1] - coords[0] + 1
				faa_d[seq.name] = {"coords": coords, "gene_len": genelen, "scaf_len": scaflen}
		elif predictor == "prodigal":
			for seq in faa_file:
				header = seq.description
				coords = (float(header.split("#")[1]), 
						  float(header.split("#")[2]))
				scaflen = scaffolds_d.get("_".join(header.split("_")[:5]), {"length": 1})["length"]
				#print(coords, scaflen)
				genelen = coords[1] - coords[0] + 1
				faa_d[seq.name] = {"coords": coords, "gene_len": genelen, "scaf_len": scaflen}
	else:
		print("unrecognized assembler")

	return faa_d


def parse_fna(fasta_nt):
	# Works with any assembly, requires Bio.SeqIO
	fna_d = {}

	for seq in SeqIO.parse(fasta_nt, "fasta"):
		fna_d[seq.name] = {"length": float(len(seq.seq)), "genes": []}

	return fna_d


def force_taxid_prot(accession):
	print("Requesting", accession)
	if "|" in accession:
		# This is a bit of a problem
		if len(accession.split("|")) == 4:
			# This happened with old-style headers, now NCBI does not use GI
			accession = accession.split("|")[3]
		else:
			# There should be just one item in accession.split("|") that is not an empty string
			# Also, it is supposedly never the first item in such headers
			accession  = [x for x in accession.split("|")[1:] if x not in [""]][0]
		#print(accession)
		
	# Efetch will still fail if a pir| accession is passed!
	try:
		prot = Entrez.efetch(db='protein', id=accession, rettype='gb', retmode='text')
		prot_record = SeqIO.read(prot, 'genbank')
		orgn = prot_record.annotations['organism']
	except:
		print("Could not process", accession)
		keeptmpblastfile = True
		with open("errors.log", "a") as errorfile:
			errorfile.write(f"error retrieving taxid for {accession}\n")
		return 1
			
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
		return 1
	print("Organism retrieved:", orgn, taxid)

	return taxid


############################
###   PARSE PARAMETERS   ###
############################

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("starting {}".format(current_time))

parser = argparse.ArgumentParser(description='How to use argparse')
#dmnd blast input absolutely requires -outfmt 6 qseqid bitscore sseqid qcovhsp pident qlen length !
parser.add_argument('-i', '--infile', help='Diamond outfile(s) to be taxified', required=True)
parser.add_argument('-d', '--work_dir', help='Working directory with the files', default=".")
#parser.add_argument('-a', '--skip_accession_pairing', help='Do not perform parsing prot.accession2taxid', action='store_true')
#input fasta names can be inferred from blast input
parser.add_argument('-nt', '--fasta_nt', help='Nucleotide fasta for parsing', default="")
parser.add_argument('-aa', '--fasta_aa', help='Amino acid fasta for parsing', default="")
parser.add_argument('-q', '--qcov_threshold', help='Query coverage threshold', default=50)
parser.add_argument('-p', '--pident_threshold', help='Percent identity threshold', default=75)
parser.add_argument('-s', '--scaffold_coverage_threshold', help='percent coverage of scaffold to consider as contamination', default=65)
parser.add_argument('-g', '--good_groups', nargs='+', help='List of "good" taxonomic groups', default=["Amoebozoa"])
parser.add_argument('-t', '--test_mode', help='Testing mode to allow checking tmp files', action="store_true")
parser.add_argument('--genomic', help='Genome analysis mode, requires protein fasta as generated by TransDecoder or Prodigal', action="store_true")

args = parser.parse_args()

# cd to wdir first
if args.work_dir != ".":
	os.chdir(args.work_dir)

filetype = "dmnd.out"

if args.infile == "batch": 
	files = [x for x in os.listdir(".") if x.endswith(filetype)]
else:
	files = args.infile.split(",")
print("to analyze:", ", ".join(files))

qthr = float(args.qcov_threshold)
pthr = float(args.pident_threshold)
sthr = float(args.scaffold_coverage_threshold)/100

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
	# Find nucleotide fasta in wdir for processing
	if args.fasta_nt == "":
		ntfasta = file.replace(filetype, "fasta")
		if os.path.exists(ntfasta):
			writent = True
		else:
			print("Nucleotide fasta missing/unspecified, skipping")
			writent = False
			continue # modification to allow proteome sorting might be added
	else:
		ntfasta = args.fasta_nt
		writent = True
	
	# Find amino acid fasta in wdir for processing
	if args.fasta_aa == "":
		aafasta = file.replace(filetype, "faa")
		if os.path.exists(aafasta):
			writeaa = True
		else:
			print("Amino acid fasta missing/unspecified, aa fasta output muted")
			writeaa = False
			if writent == False:
				print("None of the input fastas provided, skipping!")
				continue
	else:
		aafasta = args.fasta_aa
		writeaa = True

	# Check fasta requirements for genomic analysis	
	if args.genomic and writent == False:
		print("Scaffold fasta required for genomic mode, skipping!")
		continue
	if args.genomic and writeaa == False:
		print("Protein fasta required for genomic mode, skipping!")
		continue

	# Start processing files
	with open(filepath) as f:
		assembler, predictor = assembly_methods(f.readline())
	print("Assembly probably {}, protein prediction by {}".format(assembler, predictor))

	if writeaa:
		faa_d = parse_faa(assembler, predictor, aafasta)
	else:
		faa_d = {}

	dataset = file.split(".")[0]
	if os.path.isdir("./tmp") == False:
		os.system("mkdir tmp")
		print("tmp directory created")
	if os.path.isdir("./contaminants") == False:
		os.system("mkdir contaminants")
		print("contaminant directory created")
	if os.path.isdir("./{}_NR".format(dataset)) == False:
		os.system("mkdir {}_NR".format(dataset))
		print("target directory created")
	statfile = dataset + "_report.txt"
	filt = "tmp/{}_filt.txt".format(dataset)
	check = "tmp/{}_check.txt".format(dataset)
	# Use tmpblast file to retrieve taxids if the script crashes on NCBI requests
	# cut -f 3,6 tmp/<blastresult>.tmp >> subset.accession2taxid
	# Warning, this file has an atypical column order!
	tmpblast =  "tmp/{}.tmp".format(dataset)
	keeptmpblastfile = False

	# Various contaminant lists:
	cont_bact = list()
	cont_mix = set()
	cont_fungal = list()
	cont_animal = list()
	cont_plant = list()
	#cont_parabasalia = list()
	cont_other = list()

	# All hit species list
	species = set()

	# Dictionaries for comparisons
	# Initiate scaffold dictionaries or update scaffolds_d with new gene model
	global scaffolds_d
	scaffolds_d = parse_fna(ntfasta)
	
	goodscafs = {scaf: 0 for scaf in scaffolds_d}
	outscafs = {scaf: 0 for scaf in scaffolds_d}
	queries_d = {}
	ranks = {}
	distribution = {goodgroupsrep: 0}
	c = 0 # We need a process monitor

	with open(filepath) as infile, \
	open(tmpblast, "w") as outblastfile, \
	open(check, "w") as checkfile, \
	open(filt, "w") as filtfile:
		lines = sum(1 for line in open(filepath))
		print("To be processed: {}".format(lines))
		for line in infile:
			c += 1
			if c % 10000 == 0:
				print(c)
			if len(line.split("\t")) != 1:
				line = line.split("\t")
				
				# Parse query details
				if len(line) > 7:
					# This is a diamond blastp output, so additional columns can be used for filtering
					score, qcovs, pident = float(line[1]), float(line[3]), float(line[4])
				else:
					print("Not enough columns")
					continue
				try:
					query = line[0]
					query_scaf = get_scaffold(predictor, query)
				except IndexError:
					# Assuming protein ID is the same as the contig's!
					print("Could not get scaffold ID for {}!".format(query))
					query_scaf = query

				gene_len = faa_d[query]["gene_len"] if query in faa_d else 1

				# Keep a best scoring hit or skip to next result
				if query not in queries_d.keys():
					queries_d[query] = {"score": score, "qcovs": qcovs, "pident": pident, "taxid": 0, "rank": [""], "gene_len": gene_len, "scaffold": query_scaf}
				elif score > queries_d[query]["score"]:
					queries_d[query] = {"score": score, "qcovs": qcovs, "pident": pident, "taxid": 0, "rank": [""], "gene_len": gene_len, "scaffold": query_scaf}
				else:
					continue

				# Get taxid and lineage ranks
				if qcovs < 20: # Ignore queries not sufficiently covered
					continue
				
				targetAC = line[2]
				if targetAC in taxids:
					taxid = taxids[targetAC]
				else:
					taxid = force_taxid_prot(targetAC)
				try:
					lineage = ncbi.get_lineage(taxid)[2:]
					names = ncbi.get_taxid_translator(lineage)
					rank = [names[taxid] for taxid in lineage]
				except ValueError:
					print(f"problem with {targetAC}:{taxid}, please try updating taxa.sqlite")
					keeptmpblastfile = True
					with open("errors.log", "a") as errorfile:
						errorfile.write(f"error retrieving taxid for {targetAC}:{orgn}\n")
					continue

				outblastfile.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(line[0], line[1], line[2], line[3], line[4], taxid))
				
				queries_d[query]["taxid"] = taxid
				queries_d[query]["rank"] = rank
				
				# Prepare ranks to print and store distribution data
				if query_scaf not in ranks:
					ranks[query_scaf] = set()
				if taxid not in species:
					species.add(taxid)
					#orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					#print("{}\t{}".format(orgn, "_".join(rank)))
				if any(x in rank for x in goodgroups):
					#print(rank)
					orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					queries_d[query]["rank"] = [goodgroupsrep]
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

		#update scaffolds_d with query data
		for query in queries_d:
			scaffold = queries_d[query]["scaffold"]
			scaffolds_d[scaffold]["genes"].append(query)

		#ANY FILTER CAN BE APPLIED
		for scaffold in scaffolds_d:
			filtfile.write(">>>{}<<<\n".format(scaffold))
			breakhere = False
			scaflen = scaffolds_d[scaffold]["length"]
			queries = scaffolds_d[scaffold]["genes"]
			#based on values in queries_d, sort scaffolds into 
			#contaminants from bacteria, fungi, animals, plants, or mixed:
			#if total_frac[contaminants] > threshold, dump into category
			#put into header which contaminant groups were recovered
			taxon2contlist = {
							 "Bacteria": cont_bact,
							 "Fungi": cont_fungal,
							 "Metazoa": cont_animal,
							 "Streptophyta": cont_plant,
							 #"Parabasalia": cont_parabasalia,
							 }
			high = [x for x in queries if (queries_d[x]["qcovs"] > qthr and queries_d[x]["pident"] > pthr)]
			#highranks = [queries_d[x]["rank"] for x in high] #rank is a list of taxonomic groups, will not work

			# If the majority of proteins have a good taxonomic hit:
			filtfile.write("High confidence:\n")
			for taxon in goodgroups:
				subset = [x for x in high if taxon in queries_d[x]["rank"]]
				scaf_coverage = sum(queries_d[x]["gene_len"] for x in subset) / scaflen
				filtfile.write("{} {}\n".format(taxon, scaf_coverage))
				if scaf_coverage > sthr:
					filtfile.write("{}=>Good h.c.\n".format(scaffold))
					goodscafs[scaffold] += 1
					breakhere = True
					break
			if breakhere:
				filtfile.write("\n")
				continue

			# If the majority of proteins have a bad taxonomic hit:
			for taxon in taxon2contlist:
				subset = [x for x in high if taxon in queries_d[x]["rank"]]
				scaf_coverage = sum(queries_d[x]["gene_len"] for x in subset) / scaflen
				filtfile.write("{} {}\n".format(taxon, scaf_coverage))
				if scaf_coverage > sthr:
					taxon2contlist[taxon].append(scaffold)
					filtfile.write("{}=>Bad h.c.\n".format(scaffold))
					outscafs[scaffold] += 1
					breakhere = True
					break
			if breakhere:
				filtfile.write("\n")
				continue

			# If the majority of proteins have taxonomic hits not listed above, but not in good groups:
			high_nontarget = [x for x in high if not any(y in queries_d[x]["rank"] for y in goodgroups)]
			scaf_coverage = sum(queries_d[x]["gene_len"] for x in high_nontarget) / scaflen
			filtfile.write("any bad {}\n".format(scaf_coverage))
			if scaf_coverage > sthr:
				filtfile.write("{}=>Bad h.c. mix\n".format(scaffold))
				cont_mix.add(scaffold)
				outscafs[scaffold] += 1
				filtfile.write("\n")
				continue

			# If the majority of proteins have a good taxonomic hit with low confidence:
			filtfile.write("Low confidence:\n")
			for taxon in goodgroups:
				subset = [x for x in queries if taxon in queries_d[x]["rank"]]
				scaf_coverage = sum(queries_d[x]["gene_len"] for x in subset) / scaflen
				filtfile.write("{} {}\n".format(taxon, scaf_coverage))
				if scaf_coverage > sthr:
					filtfile.write("{}=>Good l.c.\n".format(scaffold))
					goodscafs[scaffold] += 1
					breakhere = True
					break
			if breakhere:
				filtfile.write("\n")
				continue

			# If the majority of proteins have a bad taxonomic hit with low confidence:
			for taxon in taxon2contlist:
				subset = [x for x in queries if taxon in queries_d[x]["rank"]]
				scaf_coverage = sum(queries_d[x]["gene_len"] for x in subset) / scaflen
				filtfile.write("{} {}\n".format(taxon, scaf_coverage))
				if scaf_coverage > sthr:
					taxon2contlist[taxon].append(scaffold)
					filtfile.write("{}=>Bad l.c.\n".format(scaffold))
					outscafs[scaffold] += 1
					breakhere = True
					break
			if breakhere:
				filtfile.write("\n")
				continue

			# All the rest goes to goodscafs:
			filtfile.write("{}=>Good (rest)\n".format(scaffold))
			goodscafs[scaffold] += 1
			filtfile.write("\n")
		#this is purely based on counts of how many times a bad or good hit was found for each query scaf
		# for query in queries_d:
		# 	try:
		# 		query_scaf = get_scaffold(predictor, query)
		# 	except IndexError:
		# 		#assuming protein ID is the same as the contig's!
		# 		query_scaf = query
		# 	besthit = queries_d[query]
		# 	qcovs, pident, rank, gene_len = besthit["qcovs"], besthit["pident"], besthit["rank"], besthit["gene_len"]
		# 	if qcovs > qthr and pident > pthr:
		# 		# Usually 75% identity and 50% query coverage means high-probability hits.
		# 		# LGT's usually don't have such a high identity towards any bacteria. 
		# 		# Sort the sequences as contaminants or good hits to subsets:
		# 		if "Bacteria" in rank:
		# 			cont_bact.append(query_scaf)
		# 			outscafs[query_scaf] += 1
		# 		elif "Fungi" in rank:
		# 			cont_fungal.append(query_scaf)
		# 			outscafs[query_scaf] += 1
		# 		elif "Metazoa" in rank:
		# 			cont_animal.append(query_scaf)
		# 			outscafs[query_scaf] += 1
		# 		elif "Streptophyta" in rank:
		# 			cont_plant.append(query_scaf)
		# 			outscafs[query_scaf] += 1
		# 		#elif "Parabasalia" in rank:
		# 		#	cont_parabasalia.append(query_scaf)
		# 		#	outscafs[query_scaf] += 1
		# 		elif goodgroupsrep in rank:
		# 			goodscafs[query_scaf] += 1
		# 		else:
		# 			#modify this if organism of interest is in NT
		# 			#if seqID has been added to goodscafs, this will be ignored
		# 			cont_other.append(query_scaf)
		# 			outscafs[query_scaf] += 1
		# 			#print(rank)
		# 	elif outscafs[query_scaf] > 0: # another protein had a contaminant signature
		# 		cont_mix.add(query_scaf)
		# 	elif any(x in rank for x in goodgroups):
		# 		goodscafs[query_scaf] += 1
		# 	else:
		# 		#this has no good hit in nt:
		# 		goodscafs[query_scaf] += 1
		# 		if "Bacteria" in rank:
		# 			#cont_bact.append(query_scaf)
		# 			outscafs[query_scaf] += 1

	#now to extract sequence data as requested
	seqlen = 0
	if writent == True:
		in_nucl = SeqIO.parse(ntfasta, "fasta")
		out_nucl = open("{0}_NR/{0}.{1}.NRfilt.fasta".format(dataset, assembler), "w")
		out_bact = open("contaminants/{0}_bact.fasta".format(dataset), "w")
		out_mix = open("contaminants/{0}_contmix.fasta".format(dataset), "w")
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
			elif seq.name in cont_mix:
				out_mix.write(">{} {}\n{}\n".format(seq.name, ranks.get(seq.name, ""), seq.seq))
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
		print("{} bases extracted".format(seqlen))
		out_nucl.close()
		out_bact.close()
		out_mix.close()
		out_fungal.close()
		out_animal.close()
		out_plant.close()
		#out_para.close()
		out_other.close()

	if writeaa == True:
		in_prot = SeqIO.parse(aafasta, "fasta")
		out_prot = open("{0}_NR/{0}.{1}.NRfilt.faa".format(dataset, assembler), "w")
		for seq in in_prot:
			try:
				query_scaf = get_scaffold(predictor, seq.name)
			except IndexError:
				print("could not parse protID to contig", seq.name)
				query_scaf = seq.name
			if goodscafs.get(query_scaf, 0) > outscafs.get(query_scaf, 0):
				out_prot.write(">{} {}\n{}\n".format(seq.name, ranks.get(query_scaf, ""), seq.seq))
			#there might be a lot of low-coverage hits, but most are from bacteria
			elif cont_bact.count(query_scaf) > goodscafs.get(query_scaf, 0):
				pass
			#note that the following are only high-similarity, high-coverage hits
			elif cont_fungal.count(query_scaf) > goodscafs.get(query_scaf, 0):
				pass
			elif cont_animal.count(query_scaf) > goodscafs.get(query_scaf, 0):
				pass
			elif cont_plant.count(query_scaf) > goodscafs.get(query_scaf, 0):
				pass
			#elif cont_parabasalia.count(query_scaf) > goodscafs.get(query_scaf, 0):
			#	out_para.write(">{} {}\n{}\n".format(query_scaf, ranks.get(query_scaf, ""), seq.seq))
			elif cont_other.count(query_scaf) > goodscafs.get(query_scaf, 0):
				pass
			else:
				#no nr blast hit:
				out_prot.write(">{} {}\n{}\n".format(seq.name, ranks.get(query_scaf, ""), seq.seq))
		out_prot.close()
	
	print("{} different species as hits. Please, check for any unwanted clades.".format(len(species)))
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
		os.system("mv {} {}_NR/".format(file, dataset))
		for tmpfile in [filt, check]:
			os.system("rm {}".format(tmpfile))
	if keeptmpblastfile == False:
		os.system("rm {}".format(tmpblast))
	print("now, run quast to analyze contaminants:")
	print("quast {0}_NR/*fasta -o ~/quast/{0}_NR --threads 4".format(dataset))

current_time = time.strftime("%H:%M:%S", t)
print("finished sorting {}".format(current_time))

