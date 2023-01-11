#!/bin/bash
#PBS -N cufflinks
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add cufflinks-2.2.1

gffread='/storage/brno3-cerit/home/kika/miniconda3/pkgs/gffread-0.12.7-h9a82719_0/bin/gffread'
bam_dir='/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/braa/final_corrected2'
out_dir='/storage/brno3-cerit/home/kika/blasto_comparative/cufflinks/'

#copy files to scratch
cp $bam_dir'/'*_sorted.bam $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

species='Braa'
cufflinks -p $PBS_NUM_PPN -o . *_sorted.bam
$gffread transcripts.gtf -o $species'_transcripts_cufflinks.gff'

#copy files back
rm *_sorted.bam
cp -r * $out_dir
