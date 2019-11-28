#!/usr/bin/env python3
import os

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins_transdecoder/')
predictions = open('pelo_transdecoder.predictions.tsv')

with open('pelo_transdecoder.mit_predictions.tsv', 'w') as mito:
	for line in predictions:
		if 'mit' in line:
			mito.write(line)
		else:
			print(line)
