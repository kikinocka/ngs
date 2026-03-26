#!/bin/sh

#extract proteins
genome='/Users/kika/ownCloud/paratrimastix/new_assembly/flye_assembly.pilon.remove_contaminants.260210.fasta'
gff='/Users/kika/ownCloud/paratrimastix/annotation/eukan/eukan_eukaryotes_final.gff3'
proteins='/Users/kika/ownCloud/paratrimastix/annotation/eukan/eukan_euk.prot.fa'

gffread $gff -g $genome -y $proteins 
 
 # -w    write a fasta file with spliced exons for each transcript
 # -x    write a fasta file with spliced CDS for each GFF transcript
 # -y    write a protein fasta file with the translation of CDS for each record



# #convert gtf to gff
# cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
# gtf='p57_cufflinks.renamed.gtf'
# gff='p57_cufflinks.renamed.gff'

# gffread $gtf -o $gff
