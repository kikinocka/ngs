#!/bin/bash
#PBS -N eukan
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'
read_dir='/storage/brno12-cerit/home/kika/paratrimastix/RNA_reads'

#copy files to scratch
cp $genome_dir'flye_assembly.pilon.remove_contaminants.260210.fasta' $SCRATCHDIR
cp $read_dir'/'*fq.gz $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

#Prepare RNA-seq data to produce input files for the main pipeline.
genome='flye_assembly.pilon.remove_contaminants.260210.fasta'
fwd='SRR33713718_trimmed_1.fq.gz'
rev='SRR33713718_trimmed_2.fq.gz'
sg1='SRR651041_trimmed.fq.gz'
sg2='SRR651098_trimmed.fq.gz'
max_intron=10000

singularity exec /storage/brno12-cerit/home/kika/tools/eukan.sif /bin/bash /opt/eukan/transcriptome_assembly.sh \
	-l $fwd -r $rev -s $sg1,$sg2 \
	-g $genome \
	-M $max_intron \
	-A -T -P \
	-n $PBS_NUM_PPN

#copy files back
rm $genome $fwd $rev $sg1 $sg2
cp -r * $genome_dir'transcriptome'
