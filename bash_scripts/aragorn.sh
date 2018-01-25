#!/bin/bash

#aragorn -v -s -d -c -l -a -w -j -ifro<min>,<max> -t -mt -m -tv -gc -seq -br -fasta -fo -o <outfile> <filename>


inf="/home/kika/MEGAsync/Chlamydomonas/ont_reads/atpB+rpoC1/cont.txt"
# out_str="/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/out_str.txt"
out_fa="/home/kika/MEGAsync/Chlamydomonas/ont_reads/atpB+rpoC1/cont_tRNAs_aragorn.txt"

#secondary structure of tRNA
# aragorn -t -seq -o $out_str $inf

#primary sequence of tRNA
aragorn -t -fo -o $out_fa $inf