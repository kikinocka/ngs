#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=5gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/sags/reassembly/'
query=$datadir'spades/contigs.fasta'
out=$datadir'blast/EU1718_contigs.vs_nr.1e-4.out'
# db=$datadir'genome_db/pzop_genome.fa'
db='/storage/projects/BlastDB/nr'
program=blastx
task=blastx
outfmt='6 qseqid staxids bitscore std'
eval=1e-4
max_seqs=1

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
