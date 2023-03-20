#!/bin/bash
#PBS -N cufflinks
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add cufflinks-2.2.1

gffread='/storage/brno3-cerit/home/kika/miniconda3/pkgs/gffread-0.12.7-h9a82719_0/bin/gffread'
bam_dir='/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/oobo'
out_dir='/storage/brno3-cerit/home/kika/blasto_comparative/cufflinks/oobo/'
gen_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
annotscript='/storage/brno2/home/kika/scripts/others/getAnnoFasta.pl'

#copy files to scratch
cp $bam_dir'/'*_sorted.bam $SCRATCHDIR
cp $gen_dir'Oobo_genome_final_masked.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

species='Oobo'
cufflinks -p $PBS_NUM_PPN -o . *_sorted.bam
$gffread transcripts.gtf -o $species'_cufflinks.gff'
perl $annotscript --seqfile=$species'_genome_final_masked.fa' --protein=off --codingseq=on $species'_cufflinks.gff'
awk 'BEGIN{FS=" "}{if(!/>/){print toupper($0)}else{print $1}}' $species'_cufflinks.mrna' > $species'_cufflinks.fa'

#copy files back
rm *_sorted.bam $genome
cp -r * $out_dir
