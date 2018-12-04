#!/bin/bash
#PBS -N SPAdes
#PBS -q uv@wagap-pro.cerit-sc.cz -l select=1:ncpus=30:ompthreads=30:mem=1000gb:scratch_local=500gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add modules
module add spades-3.11.1bin

corrected='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/all_reads/corrected/'
nano='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/nanopore/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/all_reads_k-mers/'

#copy reads to scratch
cd $corrected
cp p1_trimmed_1.fq.00.0_0.cor.fastq.gz p1_trimmed_2.fq.00.0_0.cor.fastq.gz p1_trimmed__unpaired.00.0_0.cor.fastq.gz $SCRATCHDIR
cp p2_trimmed_1.fq.00.1_0.cor.fastq.gz p2_trimmed_2.fq.00.1_0.cor.fastq.gz p2_trimmed__unpaired.00.1_0.cor.fastq.gz $SCRATCHDIR
cp p3_trimmed_1.fq.00.2_0.cor.fastq.gz p3_trimmed_2.fq.00.2_0.cor.fastq.gz p3_trimmed__unpaired.00.2_0.cor.fastq.gz $SCRATCHDIR
cp p4_trimmed_1.fq.00.3_0.cor.fastq.gz p4_trimmed_2.fq.00.3_0.cor.fastq.gz p4_trimmed__unpaired.00.3_0.cor.fastq.gz $SCRATCHDIR
cp p5_trimmed_1.fq.00.4_0.cor.fastq.gz p5_trimmed_2.fq.00.4_0.cor.fastq.gz p5_trimmed__unpaired.00.4_0.cor.fastq.gz $SCRATCHDIR
cp pelo2_001_trimmed_1.fq.00.5_0.cor.fastq.gz pelo2_001_trimmed_2.fq.00.5_0.cor.fastq.gz pelo2_001_trimmed__unpaired.00.5_0.cor.fastq.gz $SCRATCHDIR
cp pelo2_002_trimmed_1.fq.00.7_0.cor.fastq.gz pelo2_002_trimmed_2.fq.00.7_0.cor.fastq.gz pelo2_002_trimmed__unpaired.00.7_0.cor.fastq.gz $SCRATCHDIR
cp pelo5_001_trimmed_1.fq.00.6_0.cor.fastq.gz pelo5_001_trimmed_2.fq.00.6_0.cor.fastq.gz pelo5_001_trimmed__unpaired.00.6_0.cor.fastq.gz $SCRATCHDIR
cp pelo5_002_trimmed_1.fq.00.8_0.cor.fastq.gz pelo5_002_trimmed_2.fq.00.8_0.cor.fastq.gz pelo5_002_trimmed__unpaired.00.8_0.cor.fastq.gz $SCRATCHDIR

cd $nano
cp pelomyxa_nanopore.fastq.gz $SCRATCHDIR

pe11='p1_trimmed_1.fq.00.0_0.cor.fastq.gz'
pe12='p1_trimmed_2.fq.00.0_0.cor.fastq.gz'
pe1u='p1_trimmed__unpaired.00.0_0.cor.fastq.gz'

pe21='p2_trimmed_1.fq.00.1_0.cor.fastq.gz'
pe22='p2_trimmed_2.fq.00.1_0.cor.fastq.gz'
pe2u='p2_trimmed__unpaired.00.1_0.cor.fastq.gz'

pe31='p3_trimmed_1.fq.00.2_0.cor.fastq.gz'
pe32='p3_trimmed_2.fq.00.2_0.cor.fastq.gz'
pe3u='p3_trimmed__unpaired.00.2_0.cor.fastq.gz'

pe41='p4_trimmed_1.fq.00.3_0.cor.fastq.gz'
pe42='p4_trimmed_2.fq.00.3_0.cor.fastq.gz'
pe4u='p4_trimmed__unpaired.00.3_0.cor.fastq.gz'

pe51='p5_trimmed_1.fq.00.4_0.cor.fastq.gz'
pe52='p5_trimmed_2.fq.00.4_0.cor.fastq.gz'
pe5u='p5_trimmed__unpaired.00.4_0.cor.fastq.gz'

pe61='pelo2_001_trimmed_1.fq.00.5_0.cor.fastq.gz'
pe62='pelo2_001_trimmed_2.fq.00.5_0.cor.fastq.gz'
pe6u='pelo2_001_trimmed__unpaired.00.5_0.cor.fastq.gz'

pe71='pelo5_001_trimmed_1.fq.00.6_0.cor.fastq.gz'
pe72='pelo5_001_trimmed_2.fq.00.6_0.cor.fastq.gz'
pe7u='pelo5_001_trimmed__unpaired.00.6_0.cor.fastq.gz'

pe81='pelo2_002_trimmed_1.fq.00.7_0.cor.fastq.gz'
pe82='pelo2_002_trimmed_2.fq.00.7_0.cor.fastq.gz'
pe8u='pelo2_002_trimmed__unpaired.00.7_0.cor.fastq.gz'

pe91='pelo5_002_trimmed_1.fq.00.8_0.cor.fastq.gz'
pe92='pelo5_002_trimmed_2.fq.00.8_0.cor.fastq.gz'
pe9u='pelo5_002_trimmed__unpaired.00.8_0.cor.fastq.gz'

nanopore='pelomyxa_nanopore.fastq.gz'

report='spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $pe11 --pe1-2 $pe12 --pe1-s $pe1u \
--pe2-1 $pe21 --pe2-2 $pe22 --pe2-s $pe2u \
--pe3-1 $pe31 --pe3-2 $pe32 --pe3-s $pe3u \
--pe4-1 $pe41 --pe4-2 $pe42 --pe4-s $pe4u \
--pe5-1 $pe51 --pe5-2 $pe52 --pe5-s $pe5u \
--pe6-1 $pe61 --pe6-2 $pe62 --pe6-s $pe6u \
--pe7-1 $pe71 --pe7-2 $pe72 --pe7-s $pe7u \
--pe8-1 $pe81 --pe8-2 $pe82 --pe8-s $pe8u \
--pe9-1 $pe91 --pe9-2 $pe92 --pe9-s $pe9u \
--nanopore $nanopore \
--only-assembler --sc -k 21,33,55,77,99,121 -t $PBS_NUM_PPN -m 1000 -o out 2> $report
# --careful

#copy results to your folder
cd out
cp -R * $outdir
cp ../$report $outdir
