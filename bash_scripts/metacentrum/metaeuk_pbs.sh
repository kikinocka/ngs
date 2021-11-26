#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/'
metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
database='/storage/brno3-cerit/home/kika/databases/MERC_MMETSP_Uniclust50_profiles.tar.gz'

#copy files to scratch
cp $data_dir'7-tiara/eukarya.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

contigs='eukarya.fa'
out='euk_metaeuk'

$metaeuk easy-predict $contigs $database $out ${SCRATCHDIR} --mpi-runner mpirun -np $PBS_NUM_PPN

#copy files back
rm $contigs
cp -r * $data_dir'8-metaeuk'
