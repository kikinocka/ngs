#!/bin/bash
#PBS -N quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/kinetoplastids/angomonas/'
# outdir=$datadir'3-quast/'

#copy files to scratch
cp $datadir'TriTrypDB-65_AdeanaiCavalhoATCCPRA-265_Genome.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assemblies='TriTrypDB-65_AdeanaiCavalhoATCCPRA-265_Genome.fasta'
min_contig=500

quast.py -o $SCRATCHDIR -t $PBS_NUM_PPN --min-contig $min_contig $assemblies
# quast.py -o $SCRATCHDIR -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote $assemblies

# for fasta in *.fasta; do
# 	echo $fasta
# 	out=`echo $fasta | cut -d '.' -f 1`
# 	full_out=$SCRATCHDIR'/'$out

# 	quast.py -o $full_out -t $PBS_NUM_PPN --min-contig 500 --eukaryote $fasta
# done


#copy results to your folder
rm $assemblies
# rm *.fa
# cp -r * $outdir
cp -r * $datadir
