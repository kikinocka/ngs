#!/bin/bash

awk_path='/home/sebastian/extract/'
evm_path='/opt/evm/EVM_r2012-06-25/EvmUtils/'
data_dir='/home/kika/pelomyxa_schiedti/pasa-evm/'
genome='/home/kika/pelomyxa_schiedti/genome_assembly/pelomyxa_final_genome.fa'
evm=$data_dir'evm2/evm.all.gff3'
sorted=$data_dir'sorted.gff3'
deduplicated=$data_dir'sorted_deduplicated.gff3'
no_partials='sorted_deduplicated_no_partials.gff3'
dedupl_fasta=$data_dir'sorted_deduplicated.fa'
one_line='sorted_deduplicated_one_line.fa'
incomplete='sorted_deduplicated_incomplete.fa'
missing='missing_list.txt'

# #sort the gff
# gff3_sort -g $evm -i -og $sorted
# echo '***Sorting gff done***'

# #remove duplicates since for unknown reason EVM makes some
# awk -f$awk_path'remove_duplicates_gff' $sorted > $deduplicated
# echo '***Deduplicating gff done***'

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

# #replace to match the ID in gene
# sed -i 's/\.model\./\.TU\./' $missing
# echo '***Matching IDs done***'

# #remove partials
# awk -f$awk_path'remove_partial_gff3' $missing $deduplicated > $no_partials
# echo '***Removing partials done***'

#remove multiple lines of ### if exists
grep -vE '###' $no_partials > removed
mv removed sorted_deduplicated_no_partials.gff3
echo '***Removing non-unique lines done***'

# awk -f awk_name sorted_deduplicated_no_partials.gff3 > renamed.gff3
# # removes the Name=
# sed -E -i 's/Name=.*$//' renamed.gff3 
# # replaces the source of the prediction with PASA instead of dot
# sed -E 's/(scaffold[0-9]+-[0-9]+	)\.(	)/\1PASA\2/' renamed.gff3 > renamed2.gff3 
# # corrects the parent issue in the gff file with mRNA
# cat renamed2.gff3 | awk -f$awk_path'fix_mRNA' > Blattamonas_prediction_final.gff3 
# $evm_path'gff3_file_to_proteins.pl' Blattamonas_prediction_final.gff3 ../renaming/Blattamonas_nauphoetae_genome_final.fasta > initial_proteins.fasta
# grep ">" initial_proteins.fasta | sed -E 's/>(BlNa[0-9]+)(.*) [EVM|PASA].*$/\1\2/' | sed 's/\.1//' | sort --version-sort > list_genes.txt
# # simplifies the shit names which EVM adds to the proteins
# cat initial_proteins.fasta | sed -E 's/(>BlNa[0-9]+)(.*) [EVM|PASA].*$/\1\2/' | sed 's/\.1//' > simple_name.fas
# ~/gffread/gffread/gffread Blattamonas_prediction_final.gff3 -g ../renaming/Blattamonas_nauphoetae_genome_final.fasta -y simple_name.fas
# grep ">" simple_name.fas | sed 's/>//' | sed 's/\.1//'| sort --version-sort > list_genes.txt
# sed -i 's/\.1//' simple_name.fas
# # the final set of proteins sorted in the correct order
# perl ./sort.pl > Blattamonas_predicted_proteins.fasta