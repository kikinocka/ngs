#!/bin/sh
#PBS -N metabinner-composition
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

comp_script='/storage/brno2/home/kika/.conda/envs/metabinner_env/bin/scripts/gen_kmer.py'
data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/metabinner/'

#copy files to scratch
cp $assembly_dir'scaffolds_len500.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

conda activate /storage/brno2/home/kika/.conda/envs/metabinner_env

assembly='scaffolds_len500.fa'
min_len=500
kmer=4

python $comp_script $assembly $min_len $kmer 

#copy files back
rm $assembly
cp -r * $data_dir
