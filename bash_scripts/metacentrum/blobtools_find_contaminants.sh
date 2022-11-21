#!/bin/bash

cd '/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/'

blob_dir='reports/'
blast_dir='blasts/'
base='Bfru'
table=$blob_dir$base'_tables/phylum.'$base'.blobDB.table.txt'
blast=$blast_dir$base'.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'

# mkdir $blob_dir$base'_contaminants'

# grep -v "^##" $table | grep -v -e Euglenozoa -e no-hit > $blob_dir$base'_contaminants/'$base'_contaminants.tsv'
grep -v "#" $blob_dir$base'_contaminants/'$base'_contaminants.tsv' | cut -f1 | sed -e 's/^/grep "/g' -e 's/$/" $blast/g' > $blob_dir$base'_contaminants/'$base'_get_cont_from_blast.sh'
# sh $blob_dir$base'_contaminants/'$base'_get_cont_from_blast.sh' > $blob_dir$base'_contaminants/'$base'_contaminants_blast.tsv'
