f = SeqIO.parse(file, 'fasta')
with open(newfile, 'w') as out, open('errors_fetch.log', 'w') as errorlog:
	for l in f:
		if l.name.startswith('gi|'):
			gid = l.name.split('|')[1]
			handle = Entrez.efetch(db='protein', id=gid, rettype='fasta', retmode='XML')
			record = Entrez.read(handle)
			try:
				accession = record[0]['TSeq_accver']
			except KeyError:
				accession = l.name.replace('gi|{}|'.format(gid), '')
			#print(record)
			annot = ''.join([x for x in record[0]['TSeq_defline'] if x not in badchars])
			#print(annot)
			out.write('>{} {}\n{}\n'.format(accession, annot, l.seq))
			#record['TSeq_taxid'] and record['TSeq_orgname'] also possible
		elif '|' in l.description:
			codepos = l.description.find('|')
			code = l.description[:codepos]
			print(code)
			res = u.retrieve(code, frmt='fasta', database='uniprot')
			reshead = res.split('\n')[0]
			try:
				out.write('{}\n{}\n'.format(reshead, l.seq)) #extract seq header
				#out.write(res) #write fasta as is
			except TypeError:
				print(res)
				errorlog.write('{}\t{}\n'.format(code, 'could not be retrieved'))
				out.write('>{}\n{}\n'.format(l.description, l.seq))
		else:
			description = ''.join(x for x in l.description if x not in badchars)
			out.write('>{}\n{}\n'.format(description, l.seq))
