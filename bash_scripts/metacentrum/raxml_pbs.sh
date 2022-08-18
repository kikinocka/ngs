#!/bin/sh
#PBS -N raxml
#PBS -l select=1:ncpus=20:mem=1gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add raxml-8.2.8

data='/storage/brno3-cerit/home/kika/trafficking/wdr/wdr5/RAxML/'

#copy files to scratch
cp $data'wdr.CD.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

#proteins
aln='wdr.CD.trimal_gt-0.8.aln'
out=${aln%.trimal_gt-0.8.aln}

raxmlHPC-PTHREADS -m PROTGAMMALG4XF -f a -T $PBS_NUM_PPN -x 123 -N 100 -p 12345 -s $aln -n $out


# #18S
# aln='heterolobosea.trimal_gt-0.25_cons-50.aln'
# out='heterolobosea'

# raxmlHPC-PTHREADS -m GTRCAT -p 12345 -N 3 -s $aln -n $out\1 -T $PBS_NUM_PPN
# raxmlHPC-PTHREADS -m GTRCAT -p 12345 -b 12345 -N 100 -f d -s $aln -n $out\2 -T $PBS_NUM_PPN
# raxmlHPC-PTHREADS -m GTRCAT -p 12345 -f b -t RAxML_bestTree.$out\1 -z RAxML_bootstrap.$out\2 -n $out\3 -T 1$PBS_NUM_PPN


#copy files back
rm $aln
cp -R * $data
