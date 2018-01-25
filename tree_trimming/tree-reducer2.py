import os
import argparse
from Bio import SeqIO

print("This script removes unwanted branches from a dataset based on an input nexus tree.")
print("Mark the branches to be removed in the input tree by a colour (using FigTree). Please use basic colours or format found in your nex file. ")
print("Phylip not yet supported... ")
print("usage: python tree-reducer.py -i eno.fasta -t testtree.nex -c all\n--------------------------------------------------------------------------")
#WIN:black = #-16777216, #000000; green = #-16737997, #009933

parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-i', '--infile', help='Fasta/Phylip set to be trimmed', required=True)
parser.add_argument('-t', '--tree', help='Treefile for trimming', required=True)
parser.add_argument('-c', '--colour', help='Branch colour filter', default='all')

args = parser.parse_args()

indataset = SeqIO.parse(args.infile, 'fasta')
intree = open(args.tree).read()
filtercolour = args.colour

basecolours = {'blue': '0000ff', 'brown': '996633', 'cyan': '00ffff', 'green': '00ff00', 'magenta': 'ff00ff', 'orange': 'ff8000', 'purple': '800080', 'red': 'ff0000' , 'yellow': 'ffff00'}
black = ['-16777216', '000000']
if filtercolour in basecolours:
	filtercolour = basecolours[filtercolour]
elif filtercolour == 'all':
	print("any colour accepted")
else:
	print("unknown filter, setting to 'user-defined'. taxa with unrecognized colour codes will be retained")

#load fasta
seq_d = {}
for sequence in indataset:
	shortname = sequence.description
	seq_d[shortname] = sequence.seq


print("done loading sequences")
#load taxa from tree
alltaxa = []
lines = intree.split('\n')[4:]
for line in lines:
	if line != ';':
		line = line.replace("'", "")
		line = line.replace("\t", "")
		alltaxa.append(line)
	else:
		break

#determine taxa to be skipped
skip = []
for taxon in alltaxa:
	if '&!color=#' in taxon:
		newcolour = taxon.split('[&!color=#')[1].replace("]", "")
		#print(taxon)
		if newcolour in black:
			print("black detected for %s, keeping this taxon" % (taxon))
		elif filtercolour == 'all':
			skip.append(taxon.split('[&!color=#')[0])
		elif newcolour == filtercolour:
			skip.append(taxon.split('[&!color=#')[0])
		else:
			print("unknown colour detected for %s, keeping this taxon" % (taxon))
		newtaxon = taxon.split('[&!color=#')[0]
		alltaxa = [newtaxon if x==taxon else x for x in alltaxa]

print("done loading taxa, omitted taxa listed in omitted-%s" % (args.infile))
#write omitted taxa
with open('omitted-' + args.infile, 'w') as f:
	for taxon in skip:
		f.write(">%s\n%s\n" % (taxon, seq_d[taxon]))

print("writing filtered dataset...")
#write results
with open('filtered-' + args.infile, 'w') as out:
	for taxon in alltaxa:
		if taxon not in skip:
			out.write(">%s\n%s\n" % (taxon, seq_d[taxon]))
