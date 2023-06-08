#!/bin/sh

# #extract proteins
# genome='/Users/kika/ownCloud/blastocrithidia/ncbi_submission/LWC14.fsa'
# gff='/Users/kika/ownCloud/blastocrithidia/genes/tRNAs/FINAL/tRNAs.gff'
# proteins='/Users/kika/ownCloud/blastocrithidia/genes/tRNAs/FINAL/tRNAs.fa'

# gffread $gff -g $genome -w $proteins 
 
#  # -w    write a fasta file with spliced exons for each transcript
#  # -x    write a fasta file with spliced CDS for each GFF transcript
#  # -y    write a protein fasta file with the translation of CDS for each record



#convert gtf to gff
cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
gtf='p57_cufflinks.renamed.gtf'
gff='p57_cufflinks.renamed.gff'

gffread $gtf -o $gff
