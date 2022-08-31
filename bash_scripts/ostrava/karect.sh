#PBS -d .
#PBS -v PATH
#PBS -l walltime=400:00:00,nodes=1:ppn=5

read_dir='/mnt/data/bojana/Genomic/Obscuromonas_oborniki/Obscuromonas_oborniki_trimmed/trimmed75/'
fwd=$read_dir'M09_trimmed_75_1.fq.gz'
rev=$read_dir'M09_trimmed_75_2.fq.gz'

cd '/mnt/data/kika/blastocrithidia/o_oborniki/reads/'
log='o_oborniki.karect_correct.txt'
karect -correct -threads=12 -matchtype=hamming -celltype=diploid -inputfile=$fwd -inputfile=$rev 2> $log

# karect -align -threads=12 -matchtype=hamming \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -refgenomefile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_assembled/trimmed75/scaffolds.l500.fasta \
#       -alignfile=O_eliasi_align.txt &> log_karect_align_o_eliasi.txt

# karect -eval -threads=12 -matchtype=hamming \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_2.fq \
#       -resultfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/karrect/karect_PNG74_trimmed_75_1.fq \
#       -resultfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/karrect/karect_PNG74_trimmed_75_2.fq \
#       -refgenomefile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_assembled/trimmed75/scaffolds.l500.fasta \
#       -alignfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/O_eliasi_align.txt \
#       -evalfile=O_eliasi_eval.txt
