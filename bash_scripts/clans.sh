#!/bin/bash


work_dir='/Users/kika/ownCloud/membrane-trafficking/trees/all_adaptors/'
fasta=$work_dir'large-beta.fa'

clans_dir='/Users/kika/programs/clans/'
clans=$clans_dir'clans.jar'
blastp=$clans_dir'blastp'
makeblastdb=$clans_dir'makeblastdb'
threads=7

cd $work_dir
java -Xmx3g -jar $clans -infile $fasta -blastpath "$blastp" -formatdbpath "$makeblastdb -dbtype prot" -eval 1 -pval 0.1 -cpu $threads
