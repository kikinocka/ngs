#!/bin/sh

#extract proteins
genome='/Users/kika/data/kinetoplastids/Vickermania_final_polished_1.fa'
gff='/Users/kika/data/kinetoplastids/Vickermania_scaffold.out_1.gff3'
# exons='/Users/kika/ownCloud/Euglena_gracilis/pellicle/lucia/titins/titins_chinese.exons.fna'
# cds='/Users/kika/ownCloud/Euglena_gracilis/pellicle/lucia/titins/titins_chinese.cds.fna'
proteins='/Users/kika/data/kinetoplastids/Vickermania_proteins_1.faa'

# gffread $gff -g $genome -w $exons 
# gffread $gff -g $genome -x $cds
gffread $gff -g $genome -y $proteins
 
 # -w    write a fasta file with spliced exons for each transcript
 # -x    write a fasta file with spliced CDS for each GFF transcript
 # -y    write a protein fasta file with the translation of CDS for each record



# #convert gtf to gff
# cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/'
# gtf='p57_cufflinks.renamed.gtf'
# gff='p57_cufflinks.renamed.gff'

# gffread $gtf -o $gff
