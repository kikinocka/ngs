#!/bin/bash
#PBS -N blastn-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast-plus/blast-plus-2.12.0-gcc-8.3.0-ohlv7t4

datadir='/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/reports/contaminants'

#copy files to scratch
cp $datadir'/'*_possible_cont.fa $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

db='/storage/projects/BlastDB/nr'
program=blastx
task=blastx
# task=megablast
eval=1e-10
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	out=${query%.fa}'.nr_'$eval'.'$program
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt "6 qseqid staxids bitscore std" \
		-num_threads $PBS_NUM_PPN \
		-evalue $eval \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps
	echo ***BLAST done***
done
# 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore' = equivalent to 'std'

#copy files back
rm *.fa
cp * $datadir
