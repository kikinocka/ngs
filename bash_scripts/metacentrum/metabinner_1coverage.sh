#!/bin/sh
#PBS -N metabinner-coverage
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

cov_script='/storage/brno2/home/kika/.conda/envs/metabinner_env/bin/scripts/gen_coverage_file.sh'
data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/'
assembly_dir=$data_dir'metabinner/'
read_dir=$data_dir'1-reads/'

#copy files to scratch
cp $assembly_dir'scaffolds_len500.fa' $SCRATCHDIR
cp $read_dir'BML_trimmed_1.fastq.gz' $SCRATCHDIR
cp $read_dir'BML_trimmed_2.fastq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

conda activate /storage/brno2/home/kika/.conda/envs/metabinner_env

gzip -d *.gz

assembly='scaffolds_len500.fa'
fwd='BML_trimmed_1.fastq'
rev='BML_trimmed_2.fastq'
min_len=500

$cov_script -t $PBS_NUM_PPN -m 20 -l $min_len -a $assembly -o $SCRATCHDIR $fwd $rev


#copy files back
rm $assembly $fwd $rev
cp -r * $data_dir'metabinner'
