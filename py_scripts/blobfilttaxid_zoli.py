from ete3 import NCBITaxa
#http://etetoolkit.org/docs/2.3/tutorial/tutorial_ncbitaxonomy.html
ncbi = NCBITaxa()
from Bio import SeqIO

goodones = {"Panarthropoda"}
species = set()
goodscafs = {}
distribution = {"Panarthropoda": 0}
c = 0 #we need a process monitor
with open("besthits_NR.taxified.out") as infile, \
open("besthits_UP.taxified.out") as infile2, \
open("highertaxa.txt", "w") as outfile:
	table = infile.read().split("\n")
	#print("{}".format(len(table)))
	table += infile2.read().split("\n")
	print("To be analyzed: {}".format(len(table)))
	for line in table:
		c += 1
		if c % 1000 == 0:
			print(c)
		if len(line.split("\t")) != 1:
			line = line.split("\t")
			if line[1] != "N/A":
				taxid = line[1]
				lineage = ncbi.get_lineage(taxid)[2:]
				names = ncbi.get_taxid_translator(lineage)
				rank = [names[taxid] for taxid in lineage]
				# if "Eukaryota" in rank:
				# 	rank.remove("Eukaryota")
				if taxid not in species:
					species.add(taxid)
					#orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					#print("{}\t{}".format(orgn, "_".join(rank)))
				if "Panarthropoda" in rank:
					orgn = ncbi.get_taxid_translator([taxid])[int(taxid)]
					outfile.write("{}\t{}\t{}\n".format(line[0], orgn, "_".join(rank)))
					goodscafs[line[0]] = orgn
					distribution["Panarthropoda"] += 1
				elif "Metazoa" in rank:
					try:
						#print(rank[7])
						group = "Opisthokonta_Metazoa_" + rank[7]
						if group not in distribution:
							distribution[group] = 1
						else:
							distribution[group] += 1
					except IndexError:
						print("out of range:" + "_".join(rank))
				else:
					group = "_".join(rank[1:3])
					#print(group)
					if group not in distribution:
						distribution[group] = 1
					else:
						distribution[group] += 1
				#print(taxid, rank)
seqlen = 0

infasta = SeqIO.parse("Trinity_all_trimmed_stages-AA-X.fasta", "fasta")
outfile = open("kliste_blobfiltfasta.fasta", "w")
for seq in infasta:
	if seq.name in goodscafs.keys():
		outfile.write(">{}\t{}\n{}\n".format(seq.name,goodscafs[seq.name],seq.seq))
		seqlen += len(seq.seq)
print("{} bases extracted".format(seqlen))
outfile.close()

print("{} different species as hits".format(len(species)))
for key in distribution:
	print("{}\tsequences of {}".format(distribution[key], key))

print("finished sorting")