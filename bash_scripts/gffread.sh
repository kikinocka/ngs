#!/bin/sh

#extract proteins
genome='/Users/kika/mapping/euglena/chinese/GCA_039621445.1_ASM3962144v1_genomic.fna'
gff='/Users/kika/ownCloud/Euglena_gracilis/pellicle/lucia/titins/titins_chinese.gff3'
proteins='/Users/kika/ownCloud/Euglena_gracilis/pellicle/lucia/titins/titins_chinese.faa'

gffread $gff -g $genome -y $proteins 
 
 # -w    write a fasta file with spliced exons for each transcript
 # -x    write a fasta file with spliced CDS for each GFF transcript
 # -y    write a protein fasta file with the translation of CDS for each record



# #convert gtf to gff
# cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
# gtf='p57_cufflinks.renamed.gtf'
# gff='p57_cufflinks.renamed.gff'

# gffread $gtf -o $gff
