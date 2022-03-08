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
data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/metabinner/'

#copy files to scratch
cp $data_dir'scaffolds_len500.fa' $SCRATCHDIR
cp $data_dir'coverage_profile.tsv' $SCRATCHDIR
cp $data_dir'kmer_4_f500.csv' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

conda activate /storage/brno2/home/kika/.conda/envs/metabinner_env

metabinner_path=$(dirname $(which run_metabinner.sh))
assembly='scaffolds_len500.fa'
cov='coverage_profile.tsv'
kmer='kmer_4_f500.csv'

$bin_script -a $SCRATCHDIR'/'$assembly -o $SCRATCHDIR -d $SCRATCHDIR'/'$cov -k $SCRATCHDIR'/'$kmer -p ${metabinner_path} -t $PBS_NUM_PPN


#copy files back
rm $assembly $cov $kmer
cp -r * $data_dir
