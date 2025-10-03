#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

# #add module
# module add diamond

db_dir='/storage/projects-du-praha/BlastDB/'
data_dir='/storage/brno12-cerit/home/kika/Egr_2025/'
taxify='/storage/brno2/home/kika/scripts/py_scripts/taxify_DMND_nr_gz.py'


#copy files to scratch
cp $data_dir'HBDM01.transdecoder_clstr99.rep_seq.fasta' $SCRATCHDIR
cp $db_dir'nr'* $SCRATCHDIR #better to copy the large db to scratch

#compute on scratch
cd $SCRATCHDIR

eval=1e-10
max_seqs=1
db='nr'


for query in *.fasta ; do
	echo $query
	out=${query%.rep_seq.fasta}.dmnd.tsv
	mamba run -n busco-6.0.0 diamond blastp \
		--query $query \
		--db $db \
		--out $out \
		--outfmt 6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send \
		--threads $PBS_NUM_PPN \
		--evalue $eval \
		--max-target-seqs $max_seqs \
		--sensitive
	echo '***BLAST done***'
	python2 $taxify -i $out
done


#copy files back
rm *.fasta nr*
mv * $data_dir
