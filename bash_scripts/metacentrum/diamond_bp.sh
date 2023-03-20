#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

db='/storage/brno3-cerit/home/kika/dmnd/refseq.dmnd'
data_dir='/storage/brno3-cerit/home/kika/diplonema/oxphos'
taxify='/storage/brno2/home/kika/scripts/py_scripts/taxify_DMND_nr_gz.py'


#copy files to scratch
cp $data_dir'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

eval=1e-3
max_seqs=1

for query in *.fa ; do
	echo $query
	out=${query%.fa}.dmnd.out
	diamond blastp \
		-q $query \
		-d $db \
		-o $out \
		--outfmt 6 qseqid bitscore sseqid qcovhsp pident qlen length \
		--threads $PBS_NUM_PPN \
		--evalue $eval \
		--max-target-seqs $max_seqs \
		--sensitive
	echo '***BLAST done***'
	python2 $taxify -i $out
done


#copy files back
rm *.fa
mv * $data_dir
