#!/bin/bash

#tRNAscan-SE [-options] <FASTA file(s)>
#option -N: codons instead of anticodons in output
#option -O: search for organellar tRNAs

inf="/home/kika/ownCloud/zoli_mt_genome/mt_genome.txt"
out_str="/home/kika/ownCloud/zoli_mt_genome/mt_genome_tRNAscanSE.txt"
# out_cod="/home/kika/Dropbox/blasto_project/jaculum/genes/tRNAs/jac_org-tRNAs_anticodons_tRNAscan.txt"


#table output
tRNAscan-SE -O -o $out_str $inf

#secondary structures
# tRNAscan-SE -O -f $out_str $inf