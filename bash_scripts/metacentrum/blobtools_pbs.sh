#!/bin/bash
#no need to compute on scratch

#add module
module add blobtools-1.0

cd '/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/'
assembly_dir='assemblies/'
blast_dir='blasts/'
mapping_dir='mapping/'
blob_dir='reports/'
ncbi='/storage/brno3-cerit/home/kika/ncbi/'

base='Bfru'
mkdir $blob_dir$base'_tables'
mkdir $blob_dir$base'_images'

genome=$assembly_dir$base'.platanus_rnd2_scaffold.l500.gapcloser.fa'
blast=$blast_dir$base'.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'
bam=$mapping_dir$base'.bw2_sorted.bam'
tax_nodes=$ncbi'nodes.dmp'
tax_names=$ncbi'names.dmp'


echo 'Running BlobTools create'
blobtools create -i $genome --nodes $tax_nodes --names $tax_names -t $blast -b $bam -o $blob_dir$base
echo 'Running BlobTools View - Phylum'
blobtools view -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_tables/phylum' --rank 'phylum'
echo 'Running BlobTools View - Super Kingdom'
blobtools view -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_tables/superkingdom' --rank 'superkingdom'
echo 'Running BlobTools Plot PNG - Phylum'
blobtools plot -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_images' --rank 'phylum' 
echo 'Running BlobTools Plot PNG - Super Kingdom'
blobtools plot -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_images' --rank 'superkingdom' 
echo 'Running BlobTools Plot SVG - Phylum'
blobtools plot -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_images' --rank 'phylum' --format 'svg'
echo 'Running BlobTools Plot SVG - Super Kingdom'
blobtools plot -i $blob_dir$base'.blobDB.json' --out $blob_dir$base'_images' --rank 'superkingdom' --format 'svg'

# blobtools taxify -f $dmnd -m $taxid -s 1 -t 2
# blobtools create -i $transcriptome -s $sam -t $taxified -o $base
# blobtools view -i $base'.blobDB.json' --cov -o table
# blobtools plot -i $base'.blobDB.json' -r $rank -o plot 
