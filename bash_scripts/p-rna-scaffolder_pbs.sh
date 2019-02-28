#!/bin/bash
#PBS -N P_RNA_scaffolder
#PBS -l select=1:ncpus=15:mem=100gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add bioperl-1.6.9-gcc

#setting perl config file environment variable
perl_configs='/storage/brno3-cerit/home/kika/perl_configs/'
mkdir $SCRATCHDIR/perl_configs/
cp -r $perl_configs/* $SCRATCHDIR/perl_configs/ || exit 1
export PERL5LIB=$SCRATCHDIR/perl_configs
export PATH=$PATH:$SCRATCHDIR/perl_configs

#copy files to scratch
cd /storage/brno2/home/kika/tools/
cp -r P_RNA_scaffolder $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/clean/
cp pelomyxa_clean.fa $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2/
cp accepted_hits.sam $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/
cp merged_trimmed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

scaf_dir='P_RNA_scaffolder/'
scaffolder=$scaf_dir'P_RNA_scaffolder.sh'
assembly='pelomyxa_clean.fa'
sam_file='accepted_hits.sam'
fwd='merged_trimmed_1.fq.gz'
rv='merged_trimmed_2.fq.gz'
out='clean_merged_tophat2_p-rna-scaffolder'

sh $scaffolder -d $scaf_dir -i $sam_file -j $assembly -F $fwd -R $rv -o $out -t $PBS_NUM_PPN -f 3

#copy files back
cp -r $out /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/. || export CLEAN_SCRATCH=false
