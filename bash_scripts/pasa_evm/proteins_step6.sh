#!/bin/bash

awk_path='/home/sebastian/extract/'
evm_path='/opt/evm/EVM_r2012-06-25/EvmUtils/'
gffread='/home/sebastian/gffread/gffread/gffread'
genome='/home/kika/pelomyxa_schiedti/genome_assembly/pelomyxa_final_genome.fa'
data_dir='/home/kika/pelomyxa_schiedti/pasa-evm/'
deduplicated=$data_dir'sorted_deduplicated.gff3'
final=$data_dir'pelomyxa_prediction_final.gff3'
dedupl_fasta=$data_dir'sorted_deduplicated.fa'
one_line=$data_dir'sorted_deduplicated_one_line.fa'
incomplete=$data_dir'sorted_deduplicated_incomplete.fa'
missing=$data_dir'missing_list.txt'
initial=$data_dir'initial_proteins.fa'
genes=$data_dir'genes_list.txt'
simple=$data_dir'simple_names.fa'
predicted_prot=$data_dir'pelomyxa_predicted_proteins.fa'

# #extract sequences from genome
# $evm_path'gff3_file_to_proteins.pl' $deduplicated $genome > $dedupl_fasta
# echo '***Extracting sequences from genome done***'

# #makes one line fasta
# awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' $dedupl_fasta > $one_line
# echo '***Generating one line fasta done***'

# #get the proteins which are missing a start codon
# awk -f$awk_path'protein_complete' $one_line > $incomplete
# echo '***Search for proteins without start codon done***'

# #get the genes which don't have start codon
# grep ">" $incomplete | awk '{print $1}' | sed 's/>//' | sort | uniq > $missing
# echo '***List of genes without start codon done***'

#replace to match the ID in gene
sed -i 's/\.model\./\.TU\./' $missing
echo '***Matching IDs done***'

#CONTINUE IN GFF RENAMING

# #get initial proteins
# $evm_path'gff3_file_to_proteins.pl' $final $genome > $initial
# echo '***Getting initial proteins done***'

# #get gene list
# grep ">" $initial | sed -E 's/>(Pelo[0-9]+)(.*) [PASA].*$/\1\2/' | sed 's/\.1//' | sort --version-sort > $genes
# echo '***Getting gene list done***'

# #simplifies the shit names which EVM adds to the proteins
# cat $initial | sed -E 's/(>Pelo[0-9]+)(.*) [PASA].*$/\1\2/' | sed 's/\.1//' > $simple
# echo '***Changing header done***'
# $gffread $final -g $genome -y $simple
# echo '***gffread done***'
# grep ">" $simple | sed 's/>//' | sed 's/\.1//'| sort --version-sort > $genes
# echo '***First sorting done***'
# sed -i 's/\.1//' $simple
# echo '***Simplifying names done***'

# #the final set of proteins sorted in the correct order
# perl ./sort.pl > $predicted_prot
# echo '***Final set of proteins done***'
