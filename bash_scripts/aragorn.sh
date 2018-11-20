#!/bin/bash

#aragorn -v -s -d -c -l -a -w -j -ifro<min>,<max> -t -mt -m -tv -gc -seq -br -fasta -fo -o <outfile> <filename>


inf="/home/kika/ownCloud/zoli_mt_genome/mt_genome.txt"
# out_str="/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/out_str.txt"
out_fa="/home/kika/ownCloud/zoli_mt_genome/mt_genome_aragorn.txt"

#secondary structure of tRNA
# aragorn -t -seq -o $out_str $inf

#primary sequence of tRNA
aragorn -t -fo -o $out_fa $inf