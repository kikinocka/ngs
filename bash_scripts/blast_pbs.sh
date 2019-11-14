#!/bin/bash
#PBS -N blastn-megablast
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=100gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/storage/brno3-cerit/home/kika/sags/reassembly/'
query=$datadir'spades/contigs.fasta'
out=$datadir'blast/EU1718.fa_vs_nt_1e-10.megablast'
report=$datadir'blast/EU1718.fa_vs_nt_1e-10.megablast.report'

program=blastn
task=megablast
db='/storage/brno3-cerit/home/kika/ncbi_db/nt'
outfmt=6 qseqid staxids bitscore std
max_seqs=1
max_hsps=1
evalue=1e-10


$program -task $task -query $query -db $db -out $out -num_threads $PBS_NUM_PPN \
-outfmt $outfmt -max_target_seqs $max_seqs -max_hsps $max_hsps -evalue $evalue 2>$report
