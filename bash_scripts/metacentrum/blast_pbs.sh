#!/bin/bash
#PBS -N blastp
#PBS -l select=1:ncpus=20:mem=80gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/storage/brno3-cerit/home/kika/proteromonas/rabs/'
query=$datadir'Plac.fwd_hits.fa'
out=$datadir'Plac.rev_nr.blast.xml'
report=$datadir'Plac.rev_nr.blast.report'
db_dir='/storage/projects/BlastDB/'
db=$db_dir'nr'
program=blastp
task=blastp
outfmt=5
eval=1e-3
# max_seqs=1

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-evalue $eval \
	-num_threads $PBS_NUM_PPN \
	2>$report
	# -max_target_seqs $max_seqs \
