#!/bin/bash

#run on Veles
workdir='/mnt/mokosz/home/kika/rhizomastix_reassembly/'
fasta='rhizomastix_reassembly.trinity.NTfilt.fasta'
genes='rhizomastix_reassembly.trinity.NTfilt.prodigal_bct.gb'
proteins='rhizomastix_reassembly.trinity.NTfilt.prodigal_bct.faa'
setting=meta
table=1

cd $workdir
prodigal -i $fasta -o $genes -a $proteins -p $setting #-g 1 -n

# -a:  Write protein translations to the selected file.
# -c:  Closed ends. Do not allow genes to run off edges.
# -d:  Write nucleotide sequences of genes to the selected file.
# -f:  Select output format (gbk, gff, or sco).  Default is gbk.
# -g:  Specify a translation table to use (default 11).
# -h:  Print help menu and exit.
# -i:  Specify FASTA/Genbank input file (default reads from stdin).
# -m:  Treat runs of N as masked sequence; don't build genes across them.
# -n:  Bypass Shine-Dalgarno trainer and force a full motif scan.
# -o:  Specify output file (default writes to stdout).
# -p:  Select procedure (single or meta).  Default is single.
# -q:  Run quietly (suppress normal stderr output).
# -s:  Write all potential genes (with scores) to the selected file.
# -t:  Write a training file (if none exists); otherwise, read and use
#      the specified training file.
# -v:  Print version number and exit.
