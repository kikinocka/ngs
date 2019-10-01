import requests
import os
import csv
import re

#input je tsvcko s dvomi stlpcami, prvy je to co chces najst, druhy ako sa to vola (skratka); druhy stlpec nemusi byt


print('UniProt requests version', requests.__version__)

BASE = 'http://www.uniprot.org/'
KB_ENDPOINT = 'uniprot/'
TOOL_ENDPOINT = 'uploadlists/'
orgnpattern = r'OS=(.*)OX='

queryfile = 'query.tsv'


def uniprotfetch(feature, query, outfmt):
	if feature != '':
		query = f'{query} AND reviewed:yes'
	else:
		query = f'{feature}:'{query}' AND reviewed:yes'
	#always reviewed!
	searchparams = {'query': query, 'format': outfmt}
	if outfmt == 'tab':
		searchparams['columns'] = 'organism,id,entry_name,ec,protein_names,sequence'
	result = requests.get(BASE + KB_ENDPOINT, params=searchparams)

	if result.ok:
		if outfmt == 'fasta':
			resultstring = ''
			rawresult = result.text.replace('sp|', '')
			for line in rawresult.split('>')[1:]:
				print(line)
				try:
					orgn = re.search(orgnpattern, line).group(1)
					orgn = '_'.join(orgn.split()[:2])
					acc_entry = line.split()[0].replace('|', '@')
					annot = line.split()[1].split('OS=')[0]
					seq = ''.join(line.split('\n')[1:])
					resultstring += f'>{orgn}_{acc_entry} {annot}\n{seq}\n'
				except IndexError:
					pass
		elif outfmt == 'tab':
			resultstring = ''
			for line in result.text.split('\n'):
				if line.startswith('Organism'):
					continue
				line = line.split('\t')
				try:
					orgn = '_'.join(line[0].split()[:2])
					acc = line[1]
					entry = line[2]
					ecno = line[3]
					annot = line[4].split(' (')[0]
					seq = line[-1]
					resultstring += f'>{orgn}_{acc}@{entry} {annot} EC:{ecno}\n{seq}\n'
				except IndexError:
					pass
				print(line)
		return resultstring
	else:
		print('Error:', result.status_code)


queries = []
enz2annot = {}
with open(queryfile, 'r') as f:
	reader = csv.reader(f, delimiter='\t', skipinitialspace=False)
	for r in reader:
		try:
			enz2annot[r[0]] = r[1]
			queries.append(r[0])
		except IndexError:
			#i.e. no name for query
			queries.append(r[0])

print(queries)

for q in queries:
	annot = enz2annot.get(q, 'ec')
	with open(f'{annot}_{q}.fasta', 'w') as outfile:
		result = uniprotfetch('ec', q, 'tab') 
		#list = a list of accessions, gff = seq features only, tab = data-rich tabular format
		print('Sequences retrieved:', len(result.split('>')))
		outfile.write(result)
	os.system(f'/Users/morpholino/.local/bin/usearch -cluster_fast {annot}_{q}.fasta -id 0.6 -sort length -centroids {annot}_{q}.clust.fasta -notrunclabels')


print('success!')
