#!/bin/bash
#PBS -d .
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/home/users/kika/angomonas_EAPs/hmm/rnd1/'

eval "$(/home/users/bio/anaconda3/bin/conda shell.bash hook)"
conda activate /home/users/bio/anaconda3/

# query='kap3_hits.fa'
db='/home/users/kika/references/Angomonas_deanei_EAPs.faa'
# db='/mnt/data/blastdbs/nr'
program=blastp
task=blastp
evalue=1e-04
max_seqs=1
max_hsps=1

for file in CAD2221027.2_all.hmm_hits.fa ; do 
	for query in $file ; do
		echo $query
		# out=${query%.fa}'.nr_'$evalue'.'$program'.tsv'
		out=${query%.fa}'.Adea_'$evalue'.'$program'.tsv'
		# out=${db%.fa}'.ref_'$evalue'.tsv'
		$program -task $task \
			-query $query \
			-db $db \
			-out $out \
			-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
			-num_threads 10 \
			-evalue $evalue \
			-max_target_seqs $max_seqs \
			-max_hsps $max_hsps
		echo ***BLAST done***
	done
done

conda deactivate


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
