#!/bin/sh

#extract proteins
genome='/Users/kika/data/kinetoplastids/Vickermania_ingenoplastis_final_polished.fa'
gff='/Users/kika/data/kinetoplastids/Vickermania_ingenoplastis_final_polished.gff3'
proteins='/Users/kika/data/kinetoplastids/Vickermania_ingenoplastis_CDS.fasta'

gffread $gff -g $genome -x $proteins 
 
 # -w    write a fasta file with spliced exons for each transcript
 # -x    write a fasta file with spliced CDS for each GFF transcript
 # -y    write a protein fasta file with the translation of CDS for each record



# #convert gtf to gff
# cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
# gtf='p57_cufflinks.renamed.gtf'
# gff='p57_cufflinks.renamed.gff'

# gffread $gtf -o $gff
