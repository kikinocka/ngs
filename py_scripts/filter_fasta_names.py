infile = open('sequence.fasta')
line = infile.read()
infile.close()

#this is gonna create a very long string with all the file content on it
#we want to search for specific sequence in this string

seqs = line.split('>')
#the first item is empty, remove it with
seqs = seqs[1:]

infile = open('list1')
line = infile.read()
#we don`t need the line string anymore, it was saved as list "seqs"
infile.close()

names = line.split('\n')[:-1]
#in this input file, an extra newline is at the end of file, this will make the script ignore it
for item in seqs:
	sequence =  item.split('\n')
	seqname = sequence[0]
	if seqname is something from names
		aminoacids = ''.join(sequence[1:])
		print seqname"\n"aminoacids
	else:
		pass

