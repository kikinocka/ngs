#!/bin/bash
#PBS -N kma
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=15gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kma-1.3.0

reads='/storage/brno3-cerit/home/kika/oil_sands/metagenome/reads/'

#copy files to scratch
cp $reads'BML_trimmed_1.fq.gz' $SCRATCHDIR
cp $reads'BML_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

db='/storage/praha5-elixir/home/leontovyc_roman/DBs_software_installations/compress_ncbi_nt/ncbi_nt'
fwd='BML_trimmed_1.fq.gz'
rev='BML_trimmed_2.fq.gz'
out='bml_kma'

kma -ipe $fwd $rev -o $out -t_db $db -t $PBS_NUM_PPN -1t1 -mem_mode -and -apm f -ef
