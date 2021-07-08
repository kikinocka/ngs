import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def cov_plot(files):
	filenames = [x.replace(".tsv", "") for x in files]
	bedcoverages = []
	medians = []
	colors = ["blue", "orange", "green"]
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
	files = ["R.lib.tsv", "E.nana1.tsv", "E.nana2.tsv"]
	cov_plot(files)

	files = ["R.lib.tsv", "R.vac1.tsv", "R.vac2.tsv"]
	cov_plot(files)

