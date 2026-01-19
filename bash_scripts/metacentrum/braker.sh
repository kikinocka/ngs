#!/bin/bash
#PBS -N braker
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'
rna_dir='/storage/brno12-cerit/home/kika/paratrimastix/RNA_reads'
prot_dir='/storage/brno12-cerit/home/kika/databases/'


#copy files to scratch
cp $genome_dir'PaPyr_JAPMOS01.fa' $SCRATCHDIR
cp $rna_dir'/'* $SCRATCHDIR
cp $prot_dir'metamonads.faa' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome=PaPyr_JAPMOS01.fa
rna_ids=SRR651098,SRR651041,SRR33713718_1,SRR33713718_2
# bam=
prot=metamonads.faa
name='paratrimastix_pyriformis'

singularity exec /cvmfs/singularity.metacentrum.cz/Braker/braker3-v.3.0.8.sif braker.pl \
	--genome=$genome \
	--rnaseq_sets_ids=$rna_ids --rnaseq_sets_dir=$SCRATCHDIR \
	--prot_seq=$prot \
	--species=$name \
	--threads $PBS_NUM_PPN \
	--gff3 

# --bam=rnaseq.bam
# --rnaseq_sets_ids=SRR1111,SRR1115
# --rnaseq_sets_dir=/path/to/rna_dir1


#copy files back
rm $genome *.fastq $prot
cp * $datadir
