#!/bin/sh

cdseq='/Users/kika/programs/cdseq/cdseq'
genome='/Users/kika/ownCloud/blasto_comparative/genomes/FINAL/Ovol_genome_final_masked.fa'
gff='/Users/kika/ownCloud/blasto_comparative/proteins/gff_modified_forCDS/Ovol_companion.modified.gff3'
output='/Users/kika/ownCloud/blasto_comparative/proteins/Ovol_companion.CDS_cdseq.fna'

$cdseq $genome $gff > $output
# usage: cdseq [-h] [-t] [-e] [-i] [-c] [-m] [--tag tag] [-n] [-l] [--introns] [--truncate_introns int_length] [--print_arg_info] genome annotation

# Extract transcript/coding sequences from a genome using an annotation file

# positional arguments:
#   genome                genome file in FASTA format
#   annotation            annotation file in GFF[3]/GTF format

# options:
#   -h, --help            show this help message and exit
#   -t, --translate       translate the output sequence (default: False)
#   -e, --exon            use exons instead of CDS entries to define coding sequence (default: False)
#   -i, --isoforms        allow multiple isoforms per gene, instead of only longest (default: False)
#   -c, --coord_based_isoforms
#                         detect isoforms by overlapping coordindates in addition to shared parent (useful for annotations without gene entries) (default: False)
#   -m, --minimal_headers
#                         omit detailed coordinate information from output headers (default: False)
#   --tag tag             prepend headers with specified <tag> (default: None)
#   -n, --non_coding      include non-coding (intronic, UTR, etc.) sequence; uses only the coordinates of the transcript itself (incompatible with --introns) (default: False)
#   -l, --leave_lowercase
#                         leave lowercase genomic sequence intact in output (ignored if --introns) (default: False)
#   --introns             include intron sequences in lowercase (incompatible with -n) (default: False)
#   --truncate_introns int_length
#                         truncate intron sequences to length {int_length} (or {int_length} -1 if odd) (default: None)
#   --print_arg_info      print commented argument information before sequence records (default: False)
