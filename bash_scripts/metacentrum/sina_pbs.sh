#!/bin/bash
#PBS -N pynast
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE


sina='/storage/brno2/home/kika/tools/sina-1.2.11/sina'

database='/storage/brno3-cerit/home/kika/databases/silva/SILVA_138.1_SSURef_NR99_12_06_20_opt.arb'
data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/discoba/'

#copy files to scratch
cp $data'discoba_eukref_V9.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fasta='discoba_eukref_V9.fa'
aln='discoba_eukref_V9.sina.aln'

$sina -i $fasta --intype fasta -o $aln --outtype fasta --ptdb $database


#copy files back
rm $fasta
cp -R * $data
