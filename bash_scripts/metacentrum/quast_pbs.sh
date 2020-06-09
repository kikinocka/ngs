#!/bin/bash
#PBS -N quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/kinetoplastids/cbom_genome/'
# mapping=$datadir'bw2_mapping/pilon10/'
outdir=$datadir'quast'

#copy files to scratch
# cp $mapping'ku80_p10_bw2_sorted.bam' $SCRATCHDIR
cp $datadir'/'*trusted.fa $SCRATCHDIR

assemblies='*trusted.fa'
# bam='ku80_p10_bw2_sorted.bam'
min_contig=500


#compute on scratch
cd $SCRATCHDIR
# quast.py -o $output -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote --bam $bam $f

for fasta in $assemblies; do
	echo $fasta
	out=`echo $fasta | cut -d '.' -f 2`
	full_out=$outdir'/'$out

	quast.py -o $SCRATCHDIR -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote $fasta
	mv -r * $full_out
done


#copy results to your folder
# rm $f $bam
rm $assemblies
