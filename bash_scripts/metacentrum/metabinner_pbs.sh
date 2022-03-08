#!/bin/sh
#PBS -N metabinner
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

bin_script='/storage/brno2/home/kika/.conda/envs/metabinner_env/bin/run_metabinner.sh'
data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/'
assembly_dir=$data_dir'2a-spades_default/'
out_dir=$data_dir'metabinner/'

#copy files to scratch
cp $assembly_dir'scaffolds.fasta' $SCRATCHDIR
cp $out_dir'coverage_profile.tsv' $SCRATCHDIR
cp $out_dir'kmer_4_f500.csv' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

conda activate /storage/brno2/home/kika/.conda/envs/metabinner_env

metabinner_path=$(dirname $(which run_metabinner.sh))
assembly='scaffolds.fasta'
cov='coverage_profile.tsv'
kmer='kmer_4_f500.csv'

$bin_script -a $SCRATCHDIR'/'$assembly -o $SCRATCHDIR -d $SCRATCHDIR'/'$cov -k $SCRATCHDIR'/'$kmer -p ${metabinner_path} -t $PBS_NUM_PPN


#copy files back
rm $assembly $cov $kmer
cp -r * $out_dir
