#add commands directly in R on Veles

#first get rid of feature lines from gff except gene and exon
#	(mRNA, CDS, intergenic_region, five_prime_UTR, three_prime_UTR, ...)
#grep -v "mRNA" pelomyxa_prediction_final_corr.gff3 | grep -v "CDS" > pelomyxa_exons_only.gff
#check that exons bear the same Parent=<identifier> as is gene ID=<identifier>

library(GenomicFeatures)

## make TxDb from GTF file 
txdb <- makeTxDbFromGFF('masba_cds_only.gff3')

## get intron information
all.introns <- intronicParts(txdb)


library('rtracklayer')
export(all.introns, 'masba_introns-from_R.gff3', format = 'GFF3')
