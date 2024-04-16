#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N Mosdepth
#PBS -l nodes=1:ppn=40
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'

eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"

fasta='Omod_genome_final_masked.fa'
base_name=${fasta%_genome_final_masked.fa}
# bam='duplicatesRemoved_w_read_groups_indelRealigner.bam'
# bed='*.regions.bed'

#1st get the largest 100 scaffolds, their length and format it
export LC_ALL=C
seqkit fx2tab --length --name --header-line $fasta | sort -g -r -k2 | head -100 |
	awk '{ len=length($2); res=""; for (i=0;i<=len;i++) { res=substr($2,len-i+1,1) res; 
	if (i > 0 && i < len && i % 3 == 0) { res = "," res } }; print $1"\t"res"" }' |
	sed 's/_lengt.*\t/\t/g' | sed '1i\scaff\tlength' > $base_name'.scaffolds_length.tsv'


#2nd get mean scaffold coverage
#first the mean read-depth was calculated for successive non-overlapping windows of 1 kb in each scaffold using mosdepth with default settings
#To estimate somy levels for each sample, we ﬁrst measured mean read-depth for successive 1 kb windows spanning each chromosome.
#using mosdepth, the file regions.bed.gz is created, where each window has a line with start of the block, end and mean depth.
#using this bam because it has duplications removed

conda activate mosdepth

mosdepth $base_name $bam --fast-mode --by 1000 --no-per-base -t 40
gunzip *.regions.bed.gz

cat $bed | datamash --full median 4 | cut -f1,5
cat $bed | datamash --full mean 4 | cut -f1,5


#3rd Calculate median of genome coverage 
#Then the median of genome coverage was calculated.
# calculated the median of these windowed depth-means (m), i.e., a median-of-means (Mm), for each chromosome.
# only for the 100 largest.
# this is simply the median of that observed (already calculated) means
###example:
#grep "Wcollosoma_618_length_159051" Wcollosoma.regions.bed | datamash --full median 4 | cut -f1,5

cut -f1 $base_name'.scaffolds_length.tsv' | sed -e 's/^/grep "/g' -e 's/$/" *.regions.bed | datamash --full median 4 | cut -f1,5/g' > $base_name'.get_median_mean_100_largest_scaf.sh' ;
 sh $base_name'.get_median_mean_100_largest_scaf.sh' | sed 's/_length.*\t/\t/g' | sed '1i\scaff\tmean_cov' > $base_name'.median_coverage_scaffolds.tsv'

paste $base_name'.scaffolds_length.tsv' $base_name'.median_coverage_scaffolds.tsv' > $base_name'.scaffolds_length_cov.tsv'


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: Mosdepth done
