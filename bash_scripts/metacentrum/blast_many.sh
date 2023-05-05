#!/bin/bash
#PBS -N blastn-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=196:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast-plus/blast-plus-2.12.0-gcc-8.3.0-ohlv7t4

datadir='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9'
db_dir='/storage/projects/BlastDB/'


#copy files to scratch
cp $datadir'/check_cont2.fa' $SCRATCHDIR
cp $db_dir'nt'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

db='nt'
program=blastn
task=blastn
# task=megablast
eval=1e-05
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	# out=${query%.fa}'.nr_'$eval'.'$program
	out='check_cont2.fwd_ncbi-nt.tsv'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore ppos" \
		-num_threads $PBS_NUM_PPN \
		-evalue $eval \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps
	echo ***BLAST done***
done
# -outfmt "6 qseqid staxids bitscore std" \
# 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore' = equivalent to 'std'

#copy files back
rm *.fa $db
cp * $datadir
