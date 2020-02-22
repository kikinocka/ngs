#!/bin/bash
#PBS -N blastp
#PBS -l select=1:ncpus=20:mem=80gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/storage/brno3-cerit/home/kika/proteromonas/peroxisomal/'
query=$datadir'possibly_peroxisomal.fa'
out=$datadir'peroxisomal.blastp_nr.xml'
report=$datadir'peroxisomal.blastp_nr.report'
db_dir='/storage/projects/BlastDB/'
db=$db_dir'nr'

program=blastp
task=blastp
outfmt=5
# max_seqs=1
# eval=1e-3

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	# -max_target_seqs $max_seqs \
	# -evalue $eval \
	-num_threads $PBS_NUM_PPN \
	2>$report
