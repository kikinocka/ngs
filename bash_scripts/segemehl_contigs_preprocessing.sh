#!/bin/bash

contig_dir='/media/4TB1/diplonema/mapping/segemehl/1604/'
contigs_in=$contig_dir'additional_contigs.fa'
contigs_se=$contig_dir'additional_contigs_se.fa'
contigs_polyT=$contig_dir'additional_contigs_se_polyT.fa'

cat $contigs_in | sed 's/->/ to /g' > $contigs_se
cat $contigs_se > $contigs_polyT
perl -e 'print ">polyT\n".("T" x 100)."\n"' >> $contigs_polyT
