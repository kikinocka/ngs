from Bio import SeqIO

inFile = SeqIO.parse('input.txt', 'fasta')

with open('Split_fasta.txt', 'a') as result:
    for sequence in inFile:
        name = sequence.name
        seq = sequence.seq
        result.write('{}\t{}\n'.format(name,seq))
