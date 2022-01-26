#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=15:mem=3gb:scratch_local=3gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/6-metaeuk/profiles/'

#copy files to scratch
cp $datadir'euk_metaeuk.fas' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

query='euk_metaeuk.fas'
out='euk_metaeuk.blast.out'
db='/storage/projects/BlastDB/nr'
program=blastp
task=blastp
# outfmt=5
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

#copy files back
rm $query
cp -R * $datadir
