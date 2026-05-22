#!/bin/bash
#PBS -N cufflinks
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add cufflinks
module add gffread

gen_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/vinge/'
bam_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/vinge/hisat2/'
out_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/vinge/cufflinks/'
annotscript='/storage/brno12-cerit/home/kika/scripts/others/getAnnoFasta.pl'

#copy files to scratch
cp $gen_dir'GCA_010157825.1_ASM1015782v1_genomic.fna' $SCRATCHDIR
cp $bam_dir'Ving_ht2_sorted.bam' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

genome='GCA_010157825.1_ASM1015782v1_genomic.fna'
bamfile='Ving_ht2_sorted.bam'

species='Pfra'
cufflinks -p $PBS_NUM_PPN -o . $bamfile
gffread transcripts.gtf -o $species'_cufflinks.gff'
perl $annotscript --seqfile=$genome --protein=off --codingseq=on $species'_cufflinks.gff'
awk 'BEGIN{FS=" "}{if(!/>/){print toupper($0)}else{print $1}}' $species'_cufflinks.mrna' > $species'_cufflinks.fa'

#copy files back
rm $genome $bamfile
cp -r * $out_dir && clean_scratch
