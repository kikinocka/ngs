import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def process_output(files):
	"""Converts the output of ... to tsv files for cov_plot

	Input		List of output files

	Returns		List of tsv file names
				Writes tsv tables

	"""
	files = files.split(",")
	outfiles = [x.split("_")[0]+".tsv" for x in files]
	for i, file in enumerate(files):
		outfile = outfiles[i]
		writedata = False
		with open(file) as f, open(outfile, "wt") as result:
			for l in f:
				if l == ">>>>>>> Coverage per contig\n":
					print("Writing {}=>{} started".format(file, outfile))
					writedata = True
					continue
				#this is the last block in the file, so no need to turn writedata off
				if writedata:
					if len(l.strip()) > 1:
						result.write(l)
	print("Files processed:", ", ".join(outfiles))
	return outfiles


def cov_plot(files):
	"""Processes the output of ... and makes a coverage plot

	Input		List of tsv files

	Returns		Saves plots as files

	"""
	filenames = [x.replace(".tsv", "") for x in files]
	bedcoverages = []
	medians = []
	colors = ["blue", "orange", "green", "red"]
	for file in files:
		print(file)
		bed = pd.read_csv(file, sep="\t", names=["NaN", "contig", "len", "mapped", "coverage", "std"])
		bed = bed.drop("NaN", axis=1)
		average_cov = np.average(bed.coverage)
		median_cov = np.median(bed.coverage)
		print(average_cov, median_cov)
		bedcoverages.append(bed.coverage) #add to a list of datasets
		medians.append(median_cov)

	fig = plt.figure(figsize=(15,5)) #define dimensions first!
	plt.hist(bedcoverages, range=(0, 20), alpha = 0.75, bins=20, edgecolor='black', label=filenames)
	#alpha >> transparency
	plt.legend() #need label names to show a legend properly

	plt.title("Per-contig coverage: {}".format(file[:-5]))
	for i,m in enumerate(medians):
		plt.axvline(m, color=colors[i], linestyle='solid', linewidth=2, label="Median") #add vertical line
	#dotted and dashed lines ale alternatives
	plt.xlabel("Coverage")
	plt.ylabel("Count")

	plt.savefig(file[:-5] + ".png")
	#plt.show()


if __name__ == '__main__':
	# # files = process_output("r.lib_BamQC.txt,r.vac1_qualimap.txt,r.vac2_qualimap.txt")
	# files = ["R.lib.tsv", "E.nana1.tsv", "E.nana2.tsv", "E.nana_reseq1.tsv"]
	# cov_plot(files)

	# files = process_output("r.lib_BamQC.txt,E.nana1_BamQC.txt,E.nana2_BamQC.txt")
	files = ["R.lib.tsv", "R.vac1.tsv", "R.vac2.tsv", "R.vac_reseq1.tsv"]
	cov_plot(files)

