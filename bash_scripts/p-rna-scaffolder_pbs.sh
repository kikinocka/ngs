#!/bin/bash
#PBS -N P_RNA_scaffolder
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add bioperl-1.6.9.-gcc

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/
cp pelomyxa_clean.fa $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/mapping/
cp pelo_clean_bw2.sam $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/
cp *.fq.gz $SCRATCHDIR

cd /storage/brno2/home/kika/tools/
cp -r P_RNA_scaffolder/ $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

scaf_dir='P_RNA_scaffolder/'
scaffolder=$scaf_dir'P_RNA_scaffolder.sh'
assembly='pelomyxa_clean.fa'
sam_file='pelo_clean_bw2.sam'
fwd='pelo1_trimmed_1.fq.gz','pelo2_trimmed_1.fq.gz','pelo3_trimmed_1.fq.gz','pelo5_trimmed_1.fq.gz','pelo6_trimmed_1.fq.gz'
rv='pelo1_trimmed_2.fq.gz','pelo2_trimmed_2.fq.gz','pelo3_trimmed_2.fq.gz','pelo5_trimmed_2.fq.gz','pelo6_trimmed_2.fq.gz'
out='clean_p-rna-scaffolder/'

sh $scaffolder -d $scaf_dir -i $sam_file -j $assembly -F $fwd -R $rv -o $out -t $PBS_NUM_PPN -f 3

#copy files back
cp -r $out /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/. || export CLEAN_SCRATCH=false
