#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=3gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast-plus/blast-plus-2.12.0-gcc-8.3.0-ohlv7t4

datadir='/storage/brno3-cerit/home/kika/trafficking/trappC13/'

#copy files to scratch
cp $datadir'eukprot_trappc13.hmm_hits.fa' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

query='eukprot_trappc13.hmm_hits.fa'
out='eukprot_trappc13.hmm_hits.rev_blast.xml'
db='/storage/projects/BlastDB/nr'
program=blastp
task=blastp
eval=1e-05
max_seqs=1
max_hsps=1

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt 5 \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	# -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore ppos" \

#copy files back
rm $query
cp -R * $datadir
