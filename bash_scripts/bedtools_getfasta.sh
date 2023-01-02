#!/bin/sh

genome='/Users/kika/ownCloud/blastocrithidia/ncbi_submission/LWC14.fsa'
gff='/Users/kika/ownCloud/blasto_comparative/tRNAs/BLAST/bnon_synteny2.gff'
output='/Users/kika/ownCloud/blasto_comparative/tRNAs/BLAST/bnon_synteny2.fa'

bedtools getfasta -fi $genome -bed $gff -fo $output -name -s

# -fi		Input FASTA file
# -fo		Output file (opt., default is STDOUT
# -bed		BED/GFF/VCF file of ranges to extract from -fi
# -name		Use the name field and coordinates for the FASTA header
# -name+		(deprecated) Use the name field and coordinates for the FASTA header
# -nameOnly	Use the name field for the FASTA header
# -split		Given BED12 fmt., extract and concatenate the sequences
# 		from the BED "blocks" (e.g., exons)
# -tab		Write output in TAB delimited format.
# 		- Default is FASTA format.
# -s		Force strandedness. If the feature occupies the antisense,
# 		strand, the sequence will be reverse complemented.
# 		- By default, strand information is ignored.
# -fullHeader	Use full fasta header.
# 		- By default, only the word before the first space or tab 
# 		is used.
