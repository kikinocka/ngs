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

datadir='/storage/brno12-cerit/home/kika/p57/predicted_proteins/blast_transcriptome/'
# db_dir='/storage/projects/BlastDB/'
db_dir='/storage/brno12-cerit/home/kika/p57/predicted_proteins/blastDB'


#copy files to scratch
cp $datadir'transcript_hits.fa' $SCRATCHDIR
cp $db_dir'/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

query='transcript_hits.fa'
out='bnon_transcripts.rev_proteins.tsv'
db='bnon_proteins_annotated.no_mtDNA.fa'
program=blastx
task=blastx
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
rm $query bnon_proteins_annotated.no_mtDNA.fa.p*
cp -R * $datadir
