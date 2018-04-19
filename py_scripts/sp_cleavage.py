#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Calvin_cycle/RuBisCO_assembly_proteins/')
#input file in table: contig_name, TMD_number, SP_cleavage, prot_seq
inFile = open('el_prots.txt')

for protein in inFile:
#   splitting rows based on particular cells in the table
    split_line = protein.split('\t')
    contig = split_line[0]
    # TMD = split_line[1]
    SP = split_line[1]
    seq = split_line[2]
# cleavege of SP in proteins containig SP, based on its length
    try:
        SP = int(SP)
        with open('el_SP_cleaved.txt', 'a') as result:
            result.write('>{}\n{}'.format(contig,seq[SP:]))
# contig with protein, which doesn't contain SP, written in error file
    except ValueError as VE:
        with open('el_errors.txt', 'a') as ValueErrors:
            ValueErrors.write('{}\t{}\n'.format(contig,str(VE)))
