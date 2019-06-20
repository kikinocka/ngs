#!/bin/bash
#PBS -N TopHat2
#PBS -l select=1:ncpus=25:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

#since tophat removes /1 and /2 from the read names, you need to modify the reads which you input to mark them 
#with -1 and -2 instead of /1 and /2

cat $PBS_NODEFILE

#add module
module add tophat-2.1.1
module add bowtie2-2.3.0
module add samtools-1.3.1

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/
cp pelomyxa_final_genome.fa $SCRATCHDIR/pelo_final_bw2.fa

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/
cp merged_trimmed_renamed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='pelo_final_bw2.fa'
index='pelo_final_bw2'
fwd='merged_trimmed_renamed_1.fq'
rv='merged_trimmed_renamed_2.fq'
out='tophat_out/'
bam=$out'accepted_hits.bam'
sam=$out'accepted_hits.sam'

bowtie2-build --threads $PBS_NUM_PPN $genome $index

tophat2 -r 50 --mate-std-dev 50 -i 30 -p $PBS_NUM_PPN -o $out $index $fwd $rv

# samtools view $bam > $sam -@ $PBS_NUM_PPN
# samtools index $bam

#copy files back
cd $out
cp -r * /storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2/for_augustus/.
