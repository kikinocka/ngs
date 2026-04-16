#!/bin/bash
#SBATCH --job-name=blast
#SBATCH --output=blast.%j.out
#SBATCH --error=blast.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=20:00:00
#SBATCH --export=ALL


cd '/home/kika/omod/'

query='GCA_023091115.2_OSU_Omodryi_genomic.fna'
db='Omod_genome_final_masked.fa'
# db='/mnt/data/blastdbs/nr'
program=blastn
task=blastn
evalue=1e-05
max_seqs=1
max_hsps=1

for file in *.fna ; do 
	for query in $file ; do
		echo $query
		# out=${query%.fa}'.nr_'$evalue'.'$program'.tsv'
		out=${query%_OSU_Omodryi_genomic.fna}'.'$program'_'$evalue'.tsv'
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
