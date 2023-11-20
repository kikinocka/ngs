#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/home/users/kika/kap3/'

eval "$(/home/users/bio/anaconda3/bin/conda shell.bash hook)"
conda activate /home/users/bio/anaconda3/
# query='kap3_hits.fa'
db='/mnt/data/kika/references/human.GCF_000001405.40_GRCh38.p14_protein.faa'
program=blastp
task=blastp
eval=1e-04
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	out=${query%.fa}'.hsap_'$eval'.'$program'.tsv'
	# out=${db%.fa}'.ref_'$eval'.tsv'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
		-num_threads 10 \
		-evalue $eval \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps
	echo ***BLAST done***
done

conda deactivate

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
