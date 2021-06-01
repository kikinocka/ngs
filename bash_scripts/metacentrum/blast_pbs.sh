#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=3gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'bml_meta.spades_def.fa' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

query='bml_meta.spades_def.fa'
out='bml_meta.spades_def.blast'
db='/storage/projects/BlastDB/nt'
program=blastn
task=blastn
# outfmt=5
eval=1e-02
max_seqs=5
max_hsps=1

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps 


#copy files back
rm $query
cp -R * $datadir'filtration'
