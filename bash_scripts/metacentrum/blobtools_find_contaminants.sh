#!/bin/bash

cd '/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/'

report_dir='reports/'
blast_dir='blasts/'
base='Bfru'
table=$report_dir$base'_tables/phylum.'$base'.blobDB.table.txt'
blast=$blast_dir$base'.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'

# mkdir $report_dir$base'_contaminants'

# grep -v "^##" $table | grep -v -e Euglenozoa -e no-hit > $report_dir$base'_contaminants/'$base'_contaminants.tsv'

grep -v "#" $report_dir$base'_contaminants/'$base'_contaminants.tsv' | cut -f1 | sed -e "s/^/grep /g" | sed -i "s/$/ $blast/g" > $report_dir$base'_contaminants/'$base'_get_cont_from_blast.sh'
# sh $report_dir$base'_contaminants/'$base'_get_cont_from_blast.sh' > $report_dir$base'_contaminants/'$base'_contaminants_blast.tsv'
