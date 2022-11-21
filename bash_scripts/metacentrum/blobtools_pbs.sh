#!/bin/bash
#PBS -N blobtools
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blobtools-1.0

work_dir='/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/'
assembly_dir=$work_dir'assemblies/'
blast_dir=$work_dir'blasts/'
mapping_dir=$work_dir'mapping/'
blob_dir=$work_dir'report/'
ncbi='/storage/brno3-cerit/home/kika/ncbi/'

#copy files to scratch
cp $assembly_dir'Bfru.platanus_rnd2_scaffold.l500.gapcloser.fa' $SCRATCHDIR
cp $blast_dir'Bfru.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast' $SCRATCHDIR
cp $mapping_dir'Bfru.bw2_sorted.bam' $SCRATCHDIR
cp $ncbi'nodes.dmp' $ncbi'names.dmp' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
base='Bfru'
mkdir $base'tables'
mkdir $base'images'

genome=$base'.platanus_rnd2_scaffold.l500.gapcloser.fa'
blast=$base'.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'
bam=$base'.bw2_sorted.bam'
tax_nodes='nodes.dmp'
tax_names='names.dmp'

echo 'Running BlobTools create'
blobtools create -i $genome --nodes $tax_nodes --names $tax_names -t $blast -b $bam -o $base
echo 'Running BlobTools View - Phylum'
blobtools view -i $base'.blobDB.json' --out $base'tables/phylum' --rank 'phylum'
echo 'Running BlobTools View - Super Kingdom'
blobtools view -i $base'.blobDB.json' --out $base'tables/superkingdom' --rank 'superkingdom'
echo 'Running BlobTools Plot PNG - Phylum'
blobtools plot -i $base'.blobDB.json' --out $base'images'/. --rank 'phylum' 
echo 'Running BlobTools Plot PNG - Super Kingdom'
blobtools plot -i $base'.blobDB.json' --out $base'images'/. --rank 'superkingdom' 
echo 'Running BlobTools Plot SVG - Phylum'
blobtools plot -i $base'.blobDB.json' --out $base'images'/. --rank 'phylum' --format 'svg'
echo 'Running BlobTools Plot SVG - Super Kingdom'
blobtools plot -i $base'.blobDB.json' --out $base'images'/. --rank 'superkingdom' --format 'svg'

# blobtools taxify -f $dmnd -m $taxid -s 1 -t 2
# blobtools create -i $transcriptome -s $sam -t $taxified -o $base
# blobtools view -i $base'.blobDB.json' --cov -o table
# blobtools plot -i $base'.blobDB.json' -r $rank -o plot 

#copy files back
rm $genome $blast $bam $tax_names $tax_nodes
cp -r * $blob_dir

# rm $transcriptome $sam $dmnd $taxid
# cp -r * $data_dir'blobtools/pelo_clean/' || export CLEAN_SCRATCH=false
