#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=30gb:scratch_local=10gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/storage/brno3-cerit/home/fussyz01/hampllab/MMETSP1310/rRNA/'
query=$datadir'1310_rRNA.fwd_hits.fa'
out=$datadir'1310_rRNA.rev.blast.xml'
# db='/storage/brno3-cerit/home/fussyz01/hampllab/MMETSP1310/nt_db/MMETSP1310.nt.fa.txt'
db='/storage/projects/BlastDB/nt'
program=blastn
task=blastn
outfmt=5
eval=1e-4
# max_seqs=1

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	# -max_target_seqs $max_seqs \
