#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=3gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load blast

datadir='/storage/brno12-cerit/home/kika/p57/predicted_proteins/'
# db_dir='/storage/projects/BlastDB/'
db_dir='/storage/brno12-cerit/home/kika/p57/transcriptome/blastdb'


#copy files to scratch
cp $datadir'bnon_proteins_annotated.no_mtDNA.fa' $SCRATCHDIR
cp $db_dir'/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

query='bnon_proteins_annotated.no_mtDNA.fa'
out='bnon_proteins.transcriptome.tsv'
db='p57_GG_trinity.fasta'
program=tblastn
task=tblastn
eval=1e-05
max_seqs=1
max_hsps=1

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	# -outfmt 5 \

#copy files back
rm $query p57_GG_trinity.fasta.n*
cp -R * $datadir
