#!/bin/sh

#extract proteins
genome='/Users/kika/ownCloud/kinetoplastids/GP63/chr10/Ld10__Ld10_v01s1.fa'
gff='/Users/kika/ownCloud/kinetoplastids/GP63/chr10/LD10__gp63.gff3'
proteins='/Users/kika/ownCloud/kinetoplastids/GP63/chr10/LD10__proteins.fa'

gffread $gff -g $genome -y $proteins 
 
 # -w    write a fasta file with spliced exons for each transcript
 # -x    write a fasta file with spliced CDS for each GFF transcript
 # -y    write a protein fasta file with the translation of CDS for each record



# #convert gtf to gff
# cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
# gtf='p57_cufflinks.renamed.gtf'
# gff='p57_cufflinks.renamed.gff'

# gffread $gtf -o $gff
