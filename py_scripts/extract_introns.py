import gffutils
import pyfaidx
import sys
import fileinput
db = gffutils.create_db(sys.argv[1], ':memory:', merge_strategy='create_unique')
introns_exon = db.create_introns('exon')
with open('introns.gff3', 'w') as f:
	for intron in introns_exon:
		f.write(str(intron)+ '\n')
f.close()

for line in fileinput.input('introns.gff3', inplace=True):
	line2=line.strip()
	print line2.replace(",", "_")

fasta = pyfaidx.Fasta(sys.argv[2])
db2 = gffutils.create_db('introns.gff3', ':memory:')
original_stdout = sys.stdout
with open('introns.fasta', 'w') as f:
	sys.stdout = f
	for introns in db2.features_of_type('intron', order_by='start'):
		print ('>' + str(introns.id)+ '\n' + introns.sequence(fasta))
	sys.stdout = original_stdout