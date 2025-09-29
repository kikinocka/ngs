#!/bin/bash
#PBS -N blast-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load blast

datadir='/storage/brno12-cerit/home/kika/Egr_2025/'
db_dir='/storage/projects/BlastDB/'


#copy files to scratch
cp $datadir'HBDM01.transdecoder_clstr99.rep_seq.fasta' $SCRATCHDIR
cp $db_dir'nr'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

db='nr'
program=blastp
task=blastp
evalue=1e-10
max_seqs=1
max_hsps=1

for query in *.fasta; do
	echo $query
	out=${query%.fasta}'.ncbi-nr_'$evalue'.tsv'
	# out='check_cont6.fwd_ncbi-nt.tsv'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
		-num_threads $PBS_NUM_PPN \
		-evalue $evalue \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps
	echo ***BLAST done***
done
# -outfmt '6 qseqid staxids bitscore std' \
# 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore' = equivalent to 'std'

#copy files back
rm *.fasta nr*
cp * $datadir
