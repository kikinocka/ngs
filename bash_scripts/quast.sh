#!/bin/sh

f='/home/kika/ownCloud/pelomyxa_schiedti/transcriptome_assembly/pelomyxa_transcriptome_clean.fa'
output='/home/kika/ownCloud/pelomyxa_schiedti/transcriptome_assembly/quast/pelo_clean/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
