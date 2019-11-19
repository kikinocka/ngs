#!/bin/bash
#PBS -N blobtools
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blobtools-1.0

cp /storage/brno3-cerit/home/kika/sags/reassembly/mapping/bbmap/EU1718_bbm_mapped_all.sorted.bam $SCRATCHDIR
cp /storage/brno3-cerit/home/kika/sags/reassembly/spades/contigs.fasta $SCRATCHDIR

genome='contigs.fasta'
bam='EU1718_bbm_mapped_all.sorted.bam'
out='EU1718_blobtools'

cd SCRATCHDIR
blobtools map2cov -i $genome -b $bam -o $out

rm $genome $bam
cp -r * /storage/brno3-cerit/home/kika/sags/reassembly/reports/.


# assembly_dir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
# blast_dir='/storage/brno3-cerit/home/kika/sags/reassembly/blast/'
# mapping_dir='/storage/brno3-cerit/home/kika/sags/reassembly/mapping/bbmap/'
# ncbi='/storage/brno3-cerit/home/kika/ncbi_db/'
# blob_dir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/blobtools/'

# #copy files to scratch
# cp $assembly_dir'contigs.fasta' $SCRATCHDIR
# cp $blast_dir'EU1718.fa_vs_nt_1e-10.megablast' $SCRATCHDIR
# cp $mapping_dir'EU1718_bbm_mapped_all.sorted.bam' $SCRATCHDIR
# cp $ncbi'nodes.dmp' $ncbi'names.dmp' $SCRATCHDIR

# #compute on scratch
# cd $SCRATCHDIR
# mkdir tables
# mkdir images

# genome='contigs.fasta'
# blast='EU1718.fa_vs_nt_1e-10.megablast'
# bam='EU1718_bbm_mapped_all.sorted.bam'
# tax_nodes='nodes.dmp'
# tax_names='names.dmp'
# base='EU1718_blobtools'

# echo 'Running BlobTools create'
# blobtools create -i $genome --nodes $tax_nodes --names $tax_names -t $blast -b $bam -o $base
# echo 'Running BlobTools View - Phylum'
# blobtools view -i $base'.blobDB.json' --out tables/phylum --rank 'phylum'
# echo 'Running BlobTools View - Super Kingdom'
# blobtools view -i $base'.blobDB.json' --out tables/superkingdom --rank 'superkingdom'
# echo 'Running BlobTools Plot PNG - Phylum'
# blobtools plot -i $base'.blobDB.json' --out images/. --rank 'phylum' 
# echo 'Running BlobTools Plot PNG - Super Kingdom'
# blobtools plot -i $base'.blobDB.json' --out images/. --rank 'superkingdom' 
# echo 'Running BlobTools Plot SVG - Phylum'
# blobtools plot -i $base'.blobDB.json' --out images/. --rank 'phylum' --format 'svg'
# echo 'Running BlobTools Plot SVG - Super Kingdom'
# blobtools plot -i $base'.blobDB.json' --out images/. --rank 'superkingdom' --format 'svg'

# # blobtools taxify -f $dmnd -m $taxid -s 1 -t 2
# # blobtools create -i $transcriptome -s $sam -t $taxified -o $base
# # blobtools view -i $base'.blobDB.json' --cov -o table
# # blobtools plot -i $base'.blobDB.json' -r $rank -o plot 

# #copy files back
# rm $genome $blast $bam $tax_names $tax_nodes
# cp -r * $blob_dir

# # rm $transcriptome $sam $dmnd $taxid
# # cp -r * $data_dir'blobtools/pelo_clean/' || export CLEAN_SCRATCH=false
