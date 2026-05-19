#!/bin/bash
#PBS -N braker
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load augustus

#setting augustus config file environment variable
mkdir $SCRATCHDIR/augustus_configs
cp -r $AUGUSTUS_CONFIG_PATH/* $SCRATCHDIR/augustus_configs/
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs


genome_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/pfran/'
# map_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/pfran/hisat2/'
# rna_dir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/pfran/reads'
prot_dir='/storage/brno12-cerit/home/kika/databases/'

#copy files to scratch
cp $genome_dir'GCA_001766655.1_upd.fna' $SCRATCHDIR
# cp $map_dir'Pfra_ht2_sorted.bam' $SCRATCHDIR
# cp $map_dir'/'*.fastqc.gz $SCRATCHDIR
cp $prot_dir'kinetoplastids.faa' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome='GCA_001766655.1_upd.fna'
# bam='Pfra_ht2_sorted.bam'
# reads='ERR1655128,ERR1655129'
prot='kinetoplastids.faa'
name='Phytomonas_francai'

singularity exec --home $SCRATCHDIR /cvmfs/singularity.metacentrum.cz/Braker/braker3-v.3.0.8.sif braker.pl \
	--genome=$genome \
	--prot_seq=$prot \
	--species=$name \
	--workingdir=$SCRATCHDIR \
	--threads $PBS_NUM_PPN \
	--gff3

# --home $SCRATCHDIR - after "exec" when Augustus tries to write to /opt/... and fails
# --min_contig=3000 - when fails in /opt/ETP/bin/gmes/gmes_petap.pl step

# --bam=rnaseq.bam
# --rnaseq_sets_ids=SRR1111,SRR1115
# --rnaseq_sets_dir=/path/to/rna_dir1


#copy files back
rm $genome $prot
rm -r augustus_configs
cp -r * $genome_dir'braker/'
