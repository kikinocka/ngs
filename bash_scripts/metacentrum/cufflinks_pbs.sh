#!/bin/bash
#PBS -N cufflinks
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add cufflinks-2.2.1
module add bedtools-2.26.0

gffread='/storage/brno3-cerit/home/kika/miniconda3/pkgs/gffread-0.12.7-h9a82719_0/bin/gffread'
bam_dir='/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/omod'
out_dir='/storage/brno3-cerit/home/kika/blasto_comparative/cufflinks/omod/'
gen_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'

#copy files to scratch
cp $bam_dir'/'*_sorted.bam $SCRATCHDIR
cp $gen_dir'Omod_genome_final_masked.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

species='Omod'
genome=$species'_genome_final_masked.fa'
cufflinks -p $PBS_NUM_PPN -o . *_sorted.bam
$gffread transcripts.gtf -o $species'_transcripts_cufflinks.gff'
bedtools getfasta -fi $genome -bed $species'_transcripts_cufflinks.gff' -fo $species'_transcripts_cufflinks.fa'

#copy files back
rm *_sorted.bam $genome
cp -r * $out_dir
