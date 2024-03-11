#!/usr/bin/env python3
import os
import pandas as pd
from matplotlib import pyplot
from upsetplot import plot, generate_counts

os.chdir('/Users/kika/ownCloud/blasto_comparative/orthofinder_Oct02/')
# df = pd.read_csv('upset_data_test.tsv', sep='\t')

data = {
	'OG0000000' : [1, 0, 0, 0, 1],
	'OG0000001' : [1, 0, 0, 0, 1],
	'OG0000002' : [1, 1, 0, 0, 1]
}
# print(df)

df = pd.DataFrame(data)
plot(df)
pyplot.show()


# example = generate_counts()
# print(example)
# plot(example)
# pyplot.show()