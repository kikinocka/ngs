#!/usr/bin/python3
from Bio import Entrez, Medline
import csv

impacts = {}
with open('JournalHomeGrid_2019.csv', 'r') as f:
	reader = csv.reader(f, delimiter=',')
	impacts = {r[1].upper(): r[3] for r in reader}

pubs = 0
#refresh sometimes...
MAX_COUNT = 50
TERM = 'Záhonová Kristína'

Entrez.email = 'kika.zahonova@gmail.com' # put your mail here
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(h)
ids = result['IdList']
h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
records = Medline.parse(h)

print("looking up papers at NCBI...")
with open("references_NCBI_automatic.tsv", "w") as result:
	for paper in records:
		pubs += 1
		print(paper['TI'])
		title = paper['TI']
		try:
			journalfull = paper['JT']
			journalshort = paper['TA']
			impactfactor = "[IF2019={}]".format(impacts[journalfull.upper()])
		except KeyError:
			print("!! unsuccessful paper import bc not in journal: ", title)
			impactfactor = ""
		try:
			authors = ", ".join(paper['AU'])
		except KeyError:
			print("!! unsuccessful paper import bc of authors: ", title)
			authors = "Zahonova K and whoknows"
		try:
			year = paper['DP']
			if " " in year:
				year = year.split()[0]
			volume = paper['VI']
			pages = paper['PG']
			#doi = paper['AID'][0]
		except KeyError:
			volume = "in press"
			pages = ""
			year = ""
			print("!! unsuccessful paper import bc unpublished: ", title)

		result.write("{}\t{}\t{}\t{} {}:{}\t{}\n".format(authors, year, title, journalshort, volume, pages, impactfactor))
print("Imported from NCBI: {} articles.".format(pubs))
	
