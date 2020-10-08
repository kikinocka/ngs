#add commands directly in R on Veles

#first get rid of mRNA and CDS lines from gff, since they have same ID with gene and each other, respectively
#grep -v "mRNA" pelomyxa_prediction_final_corr.gff3 | grep -v "CDS" > pelomyxa_exons_only.gff

library(GenomicFeatures)

## make TxDb from GTF file 
txdb <- makeTxDbFromGFF('pelomyxa_exons_only.gff3')

## get intron information
all.introns <- intronicParts(txdb)


library('rtracklayer')
export(all.introns, 'pelomyxa_introns.gff', format = 'GFF3')
