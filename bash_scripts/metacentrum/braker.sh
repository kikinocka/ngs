#!/bin/bash
#PBS -N braker
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir=''
rna_dir=''
prot_dir=''


#copy files to scratch
cp $genome_dir'' $SCRATCHDIR
cp $rna_dir'' $SCRATCHDIR
cp $prot_dir'' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome=
bam=
prot=
name=

singularity exec /cvmfs/singularity.metacentrum.cz/Braker/braker3-v.3.0.8.sif braker.pl \
	--genome=$genome --bam=$bam  --prot_seq=$prot --species=$name --gff3 --threads $PBS_NUM_PPN

# --bam=rnaseq.bam
# --rnaseq_sets_ids=SRR1111,SRR1115
# --rnaseq_sets_dir=/path/to/rna_dir1


#copy files back
rm $genome $bam $prot
cp * $datadir
