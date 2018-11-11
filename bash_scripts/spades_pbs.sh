#!/bin/bash
#PBS -N SPAdes
#PBS -q uv@wagap-pro.cerit-sc.cz -l select=1:ncpus=30:ompthreads=30:mem=1000gb:scratch_local=500gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add modules
module add spades-3.11.1

prel='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/preliminary_seq/'
deep_hi='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/deep_hiseq/'
deep_mi='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/deep_miseq/'
nano='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/nanopore/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/'

#copy reads to scratch
cd $prel
cp pelo2_001_trimmed_1.fq.gz pelo2_001_trimmed_2.fq.gz pelo5_001_trimmed_1.fq.gz pelo5_001_trimmed_2.fq.gz $SCRATCHDIR

cd $deep_hi
cp p1_trimmed_1.fq.gz p1_trimmed_2.fq.gz p2_trimmed_1.fq.gz p2_trimmed_2.fq.gz p3_trimmed_1.fq.gz p3_trimmed_2.fq.gz p4_trimmed_1.fq.gz p4_trimmed_2.fq.gz p5_trimmed_1.fq.gz p5_trimmed_2.fq.gz $SCRATCHDIR

cd $deep_mi
cp pelo2_002_trimmed_1.fq.gz pelo2_002_trimmed_2.fq.gz pelo5_002_trimmed_1.fq.gz pelo5_002_trimmed_2.fq.gz $SCRATCHDIR

cd $nano
cp pelomyxa_nanopore.fastq.gz $SCRATCHDIR

pe1-1='p1_trimmed_1.fq.gz'
pe1-2='p1_trimmed_2.fq.gz'
pe2-1='p2_trimmed_1.fq.gz'
pe2-2='p2_trimmed_2.fq.gz'
pe3-1='p3_trimmed_1.fq.gz'
pe3-2='p3_trimmed_2.fq.gz'
pe4-1='p4_trimmed_1.fq.gz'
pe4-2='p4_trimmed_2.fq.gz'
pe5-1='p5_trimmed_1.fq.gz'
pe5-2='p5_trimmed_2.fq.gz'

pe6-1='pelo2_001_trimmed_1.fq.gz'
pe6-2='pelo2_001_trimmed_2.fq.gz'
pe7-1='pelo5_001_trimmed_1.fq.gz'
pe7-2='pelo5_001_trimmed_2.fq.gz'

pe8-1='pelo2_002_trimmed_1.fq.gz'
pe8-2='pelo2_002_trimmed_2.fq.gz'
pe9-1='pelo5_002_trimmed_1.fq.gz'
pe9-2='pelo5_002_trimmed_2.fq.gz'

nanopore='pelomyxa_nanopore.fastq.gz'

report='spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $pe1-1 --pe1-2 $pe1-2 \
--pe2-1 $pe2-1 --pe2-2 $pe2-2 \
--pe3-1 $pe3-1 --pe3-2 $pe3-2 \
--pe4-1 $pe4-1 --pe4-2 $pe4-2 \
--pe5-1 $pe5-1 --pe5-2 $pe5-2 \
--pe6-1 $pe6-1 --pe6-2 $pe6-2 \
--pe7-1 $pe7-1 --pe7-2 $pe7-2 \
--pe8-1 $pe8-1 --pe8-2 $pe8-2 \
--pe9-1 $pe9-1 --pe9-2 $pe9-2 \
--nanopore $nanopore \
--careful -k 127 -t $PBS_NUM_PPN -m 1000 -o out 2> $report

#copy results to your folder
cd out
cp -R * $outdir
cp ../$report $outdir
