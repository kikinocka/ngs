#!/bin/bash
#PBS -N blastn
#PBS -l select=1:ncpus=10:mem=1gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast-plus/blast-plus-2.12.0-gcc-8.3.0-ohlv7t4

datadir='/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/'

#copy files to scratch
# cp $datadir'/'*.fa $SCRATCHDIR
cp $datadir'Tbruc427_DNA.bw2_mapped_vsearch.KP.fa' $SCRATCHDIR
cp $datadir'RNAs/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

query='Tbruc427_DNA.bw2_mapped_vsearch.KP.fa'
db='RNAs_final.fa'
out='Tbruc427_DNA.bw2_mapped_vsearch.best_blast.KP.out'
max_seqs=1

blastn -query $query -db $db -out $out \
	-outfmt "6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send" \
	-max_target_seqs $max_seqs \
	-num_threads $PBS_NUM_PPN


# program=blastn
# db='/storage/projects/BlastDB/nt'
# outfmt=5
# word=11
# evalue=1e-03

# for query in *.fa; do
# 	echo $query
# 	out=${query%.fa}'.blastn.xml'
# 	$program -query $query -db $db -out $out -outfmt $outfmt -word_size $word -evalue $evalue -num_threads $PBS_NUM_PPN
# 	echo ***BLAST done***
# done

#copy files back
# rm *fa
rm $query $db
cp * $datadir
