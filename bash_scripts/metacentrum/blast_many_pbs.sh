#!/bin/bash
#PBS -N blastn-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=196:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast-plus/blast-plus-2.12.0-gcc-8.3.0-ohlv7t4

datadir='/storage/brno3-cerit/home/kika/blasto_comparative/blobtools'

#copy files to scratch
cp $datadir'/'*.fa $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

db='/storage/projects/BlastDB/nt'
program=blastn
task=megablast
eval=1e-20
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	out=${query%.fa}'.nt_1e-20.megablast'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt "6 qseqid staxids bitscore std" \
		# 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore' = equivalent to 'std'
		-num_threads $PBS_NUM_PPN \
		-evalue $eval \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps
	echo ***BLAST done***
done

#copy files back
rm *.fa
cp * $datadir
