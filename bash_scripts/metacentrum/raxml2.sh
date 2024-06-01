#!/bin/sh
#PBS -N raxml2
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=1gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add raxml/8.2.12-gcc-10.2.1-nu7c3k5

data='/storage/brno12-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/apus+brev/ref_tree/'

#copy files to scratch
cp $data'apus+brev.trimal_gt-0.25_cons-50.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

# #proteins
# aln='rabs.trimal_gt-0.8.aln'
# out=${aln%.trimal_gt-0.8.aln}

# raxmlHPC-PTHREADS -m PROTGAMMALG4XF -f a -T $PBS_NUM_PPN -x 123 -N autoMRE_IGN -p 12345 -s $aln -n $out


#18S
aln='apus+brev.trimal_gt-0.25_cons-50.aln'
out=${aln%.trimal_gt-0.25_cons-50.aln}

raxmlHPC-PTHREADS -m GTRCAT -p 12345 -N 3 -s $aln -n $out\1 -T $PBS_NUM_PPN
raxmlHPC-PTHREADS -m GTRCAT -p 12345 -b 12345 -N autoMRE_IGN -f d -s $aln -n $out\2 -T $PBS_NUM_PPN
raxmlHPC-PTHREADS -m GTRCAT -p 12345 -f b -t RAxML_bestTree.$out\1 -z RAxML_bootstrap.$out\2 -n $out\3 -T $PBS_NUM_PPN


#copy files back
rm $aln
cp -R * $data
