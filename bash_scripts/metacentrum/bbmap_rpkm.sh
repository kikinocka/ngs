#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load bbmap

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/adean/'

#copy files to scratch
cp $datadir'TriTrypDB-68_AdeanaiCavalhoATCCPRA-265_AnnotatedCDSs.fasta' $SCRATCHDIR
cp $datadir'wt/'*fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
assembly='TriTrypDB-68_AdeanaiCavalhoATCCPRA-265_AnnotatedCDSs.fasta'
# fw='p57_trimmed_1.fq.gz'
# rv='p57_trimmed_2.fq.gz'
# all='el_reads_new.fa'

base=adean.
sam=$base'sam'
rpkm=$base'rpkm_bbmap.tsv'
report=$base'report_bbmap.txt'

# #separate read files
# bbmap.sh ref=$assembly in=$fw in2=$rv out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

one read file
bbmap.sh ref=$assembly in=*fq.gz out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
# rm $assembly $fw $rv
rm $assembly *fq.gz
cp -r * $datadir
