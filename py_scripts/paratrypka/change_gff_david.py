#!/usr/bin/python

from Bio import SeqIO


class Scaffold(object):

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
        self.gff = []
        self.contaminations = []
        
    def __str__(self):
        return self.name
    
    def read_gff(self, gene):
        self.gff.append(gene)
        
    def get_gff(self):
        return self.gff
        
    def add_contamination(self, contamination):
        self.contaminations.append(contamination)
        
    def get_contaminations(self):
        return self.contaminations


scaffold_dict = {}

for scaffold in SeqIO.parse('para_genome.fa', 'fasta'):
    scaffold_dict[scaffold.name] = Scaffold(scaffold.name, scaffold.seq)
    

for line in open('contaminations.txt'):
    scaffold_name = line.split()[0]
    contaminations = line.split()[2]
    cont_list = [tuple(cont.split('..')) for cont in contaminations.split(',')]
    for contamination in cont_list:
        scaffold_dict[scaffold_name].add_contamination(contamination)
        
for line in open('para.gff'):
    scaffold_name = line.split()[0]
    scaffold_dict[scaffold_name].read_gff(line)
    
def prepare_GFF(scaffold):
    scaff = scaffold_dict[scaffold]
    result_list = []
    multiple_names = False
    new_scaff_dict = {}
    for gene in scaff.get_gff():
        counter = 1
        split_gene = gene.split()
        gene_start = int(split_gene[3])
        gene_end = int(split_gene[4])
        scaff_len = len(scaff.sequence)
        true_start = str(gene_start)
        true_end = str(gene_end)
        for cont in scaff.get_contaminations():
            if int(cont[1]) < gene_start:
                true_start = gene_start - int(cont[1])
                true_end = gene_end - int(cont[1])
                if int(cont[0]) == 1 or int(cont[1]) == scaff_len:
                    pass
                else:
                    counter += 1
                    new_scaff_dict[counter] = int(cont[1])
              
        split_gene[3] = str(true_start)
        split_gene[4] = str(true_end)
        
        
        if counter == 0:
            result_list.append('\t'.join(split_gene))
        else:
            split_gene[0] = split_gene[0] + f'_{counter}'
            result_list.append('\t'.join(split_gene))
            multiple_names = True
        
    for result in result_list:
        if multiple_names == False:
            print(result)
        else:
            split_res = result.split()
            if split_res[0] == scaff.name:
                split_res[0] = scaff.name + '_0'
                print('\t'.join(split_res))
            else:
                print(result)
            
            
for scaffold in scaffold_dict:    
   prepare_GFF(scaffold)



def genome_cutter(scaffold):
    scaff = scaffold_dict[scaffold]
    
    con_seqs = []
    
    result_seq = str(scaff.sequence)
    
    for cont in scaff.get_contaminations():
        con_seqs.append(str(scaff.sequence)[int(cont[0])-1:int(cont[1])-1])
        print(str(scaff.sequence)[int(cont[0])-1:int(cont[1])-1])
        # print(result_seq.count(str(scaff.sequence)[int(cont[0])-1:int(cont[1])-1]))
    
    for seq in con_seqs:
        result_seq = result_seq.replace(seq, '@')
    
    counter = 1
    pre_result = result_seq.split('@')
    result = [i for i in pre_result if len(i)>5]
    for i in result:
        if len(result) > 1:
            print('>{}\n{}\n'.format(scaff.name + f'_{counter}', scaff.sequence))
            counter += 1
        else:
            print('>{}\n{}\n'.format(scaff.name, scaff.sequence))
        


# for scaffold in scaffold_dict:    
#     genome_cutter(scaffold)















