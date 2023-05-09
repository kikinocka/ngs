#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=3gb
#PBS -l walltime=196:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load blast

datadir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/'
db_dir='/storage/projects/BlastDB/'


#copy files to scratch
cp $datadir'otus_blast.fa' $SCRATCHDIR
cp $db_dir'nt'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

query='otus_blast.fa'
out='otus_blast.fwd_ncbi-nt.tsv'
db='nt'
program=blastn
task=blastn
eval=1e-05
max_seqs=1
max_hsps=1

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore ppos" \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	# -outfmt 5 \

#copy files back
rm $query nt*
cp -R * $datadir
