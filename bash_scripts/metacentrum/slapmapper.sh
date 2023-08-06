#!/bin/bash
#PBS -N slapmapper
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load bowtie2
module load trimmomatic

slap_mapper='/storage/brno2/home/kika/tools/SLaPMapper/SLaPMapper.pl'
genome_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
read_dir='/storage/brno3-cerit/home/kika/blasto_comparative/sp_HR-05/transcriptome_reads/'
datadir='/storage/brno3-cerit/home/kika/blasto_comparative/slapmapper/kmers/braa/'


#copy files to scratch
cp $genome_dir'Braa_genome_final_corrected2_masked.fa' $SCRATCHDIR
cp $read_dir'braa_trimmed_1.fq.gz' $SCRATCHDIR
cp $read_dir'braa_trimmed_2.fq.gz' $SCRATCHDIR
cp $datadir'braa_kmers.txt' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR
touch 'braa_empty.gff'

genome='Braa_genome_final_corrected2_masked.fa'
fwd='braa_trimmed_1.fq.gz'
rev='braa_trimmed_1.fq.gz'
kmers='braa_kmers.txt'
gff='braa_empty.gff'
# SL='AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG' #blastocrithidia
min_length='6'


while read line; do
	# echo $line
	mkdir $line
	cd $line
	$slap_mapper -g $genome -l $fwd -r $rev -a $gff -i $line -s $min_length
	cd ..
done < $kmers

# $slap_mapper -g $genome -l $fwd -r $rev -a $gff -i $SL -s $min_length

#copy files back
rm *.fa *fq.gz
cp -r * $datadir
