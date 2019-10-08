import requests
import os
import csv
import re

print("UniProt requests version", requests.__version__)
#https://www.ebi.ac.uk/training/online/sites/ebi.ac.uk.training.online/files/UniProt_programmatically_py3.pdf
BASE = "http://www.uniprot.org/"
KB_ENDPOINT = "uniprot/"
TOOL_ENDPOINT = "uploadlists/"
orgnpattern = r"OS=(.*)OX="

queryfile = "upr_query.tsv"
usearchfileid = len([x for x in os.listdir(".") if x.startswith("usearch")]) + 1


def uniprotreviewed(feature, query, outfmt):
	if feature != "":
		query = f'{query} AND reviewed:yes'
	else:
		query = f'{feature}:"{query}" AND reviewed:yes'
	#always reviewed!
	searchparams = {"query": query, "format": outfmt}
	if outfmt == "tab":
		#check webpage for further available columns
		searchparams["columns"] = "organism,id,entry_name,ec,protein_names,sequence" 
	result = requests.get(BASE + KB_ENDPOINT, params=searchparams)

	if result.ok:
		if outfmt == "fasta":
			resultstring = ""
			rawresult = result.text.replace("sp|", "")
			for line in rawresult.split(">")[1:]:
				#print(line)
				try:
					orgn = re.search(orgnpattern, line).group(1)
					orgn = "_".join(orgn.split()[:2])
					acc_entry = line.split()[0].replace("|", "@")
					annot = line.split()[1].split("OS=")[0]
					seq = "".join(line.split("\n")[1:])
					resultstring += f">{orgn}_{acc_entry} {annot}\n{seq}\n"
				except IndexError:
					pass
		elif outfmt == "tab":
			resultstring = ""
			for line in result.text.split("\n"):
				if line.startswith("Organism"):
					continue
				line = line.split("\t")
				#print(line)
				try:
					orgn = "_".join(line[0].split()[:2])
					acc = line[1]
					entry = line[2]
					if line[3] != "":
						ecno = f" EC:{line[3]}"
					else:
						ecno == ""
					annot = line[4].split(" (")[0]
					seq = line[-1]
					resultstring += f">{orgn}_{acc}@{entry} {annot}{ecno}\n{seq}\n"
				except IndexError:
					pass
		return resultstring
	
	else:
		print("\tReviewed accessions error:", result.status_code)
		return ""

def uniprotgeneral(feature, query, outfmt):
	if feature != "":
		query = f'{query}'
	else:
		query = f'{feature}:"{query}"'
	#always reviewed!
	searchparams = {"query": query, "format": outfmt}
	if outfmt == "tab":
		#check webpage for further available columns
		searchparams["columns"] = "organism,id,entry_name,ec,protein_names,sequence" 
	result = requests.get(BASE + KB_ENDPOINT, params=searchparams)

	if result.ok:
		if outfmt == "fasta":
			resultstring = ""
			rawresult = result.text.replace("sp|", "")
			for line in rawresult.split(">")[1:]:
				if query.lower() not in line.split("\n")[0].lower():
					continue
				#print(line)
				try:
					orgn = re.search(orgnpattern, line).group(1)
					orgn = "_".join(orgn.split()[:2])
					acc_entry = line.split()[0].replace("|", "@")
					annot = line.split()[1].split("OS=")[0]
					seq = "".join(line.split("\n")[1:])
					resultstring += f">{orgn}_{acc_entry} {annot}\n{seq}\n"
				except IndexError:
					pass
		elif outfmt == "tab":
			resultstring = ""
			for line in result.text.split("\n"):
				if line.startswith("Organism"):
					continue
				try:
					if query.lower() not in line.split("\t")[4].lower():
						continue
				except IndexError:
					print(line)
				line = line.split("\t")
				#print(line)
				try:
					orgn = "_".join(line[0].split()[:2])
					acc = line[1]
					entry = line[2]
					if line[3] != "":
						ecno = f" EC:{line[3]}"
					else:
						ecno = ""
					annot = line[4].split(" (")[0]
					seq = line[-1]
					resultstring += f">{orgn}_{acc}@{entry} {annot}{ecno}\n{seq}\n"
				except IndexError:
					pass
		#print(resultstring)
		return resultstring
	
	else:
		print("Error:", result.status_code)
		return ""

queries = []
enz2annot = {}
with open(queryfile, 'r') as f:
	reader = csv.reader(f, delimiter='\t', skipinitialspace=False)
	for r in reader:
		if r[0].startswith("#"):
			continue
		try:
			enz2annot[r[0]] = r[1]
			queries.append(r[0])
		except IndexError:
			#i.e. no name for query
			queries.append(r[0])

print(queries)

for q in queries:
	run_usearch = True
	print(f"Fetching data for {q}...")
	if len(q.split(".")) == 4:
		#this is an EC number
		annot = enz2annot.get(q, "ec")
		outfilename = f"{annot}_{q}.fasta"
		result = uniprotreviewed("ec", q, "tab") 
		#formats: list = a list of accessions, gff = seq features only, tab = data-rich tabular format
		if result == "":
			#try a more general search
			result = uniprotgeneral("ec", q, "tab")
			if result == "":
				print(f"\tNo sequences for {q}")
				#do not write anything, turn off usearch flag
				run_usearch = False
			else:
				print(f"\tWarning, reviewed accessions not found for {q}, fetching all accessions")
				seqs = len(result.split(">")) - 1
				print("Sequences retrieved:", seqs)
				with open(outfilename, "w") as out:
					out.write(result)
		else:
			seqs = len(result.split(">")) - 1
			print("\tSequences retrieved:", seqs)
			with open(outfilename, "w") as out:
				out.write(result)
	else:
		annot = q
		outfilename = f"{annot}.fasta"
		result = uniprotreviewed("", q, "tab")
		#formats: list = a list of accessions, gff = seq features only, tab = data-rich tabular format
		if result == "":
			#try a more general search
			result = uniprotgeneral("name", q, "tab")
			if result == "":
				print(f"\tNo sequences for {q}")
				#do not write anything, turn off usearch flag
				run_usearch = False
			else:
				print(f"\tWarning, reviewed accessions not found for {q}, fetching all accessions")
				seqs = len(result.split(">")) - 1
				print("\tSequences retrieved:", seqs)
				with open(outfilename, "w") as out:
					out.write(result)
		else:
			seqs = len(result.split(">")) - 1
			print("\tSequences retrieved:", seqs)
			with open(outfilename, "w") as out:
				out.write(result)
	
	if run_usearch == True:
		clustname = outfilename.replace(".fasta", "") + ".clust.fasta"
		os.system(f"/Users/morpholino/.local/bin/usearch -cluster_fast {outfilename} -id 0.6 -sort length -centroids {clustname} -notrunclabels" + f">> usearch{usearchfileid}.log 2>&1")


print("success!")