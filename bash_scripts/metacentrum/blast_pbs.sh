#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=10gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/sags/'
query=$datadir'found_proteins.fa'
out=$datadir'found_proteins.fwd.blast.xml'
# db='/storage/brno3-cerit/home/fussyz01/hampllab/MMETSP1310/nt_db/MMETSP1310.nt.fa.txt'
db='/storage/projects/BlastDB/nr'
program=blastp
task=blastp
outfmt=5
# eval=1e-4
max_seqs=5

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $PBS_NUM_PPN \
	-max_target_seqs $max_seqs \
	# -evalue $eval \
