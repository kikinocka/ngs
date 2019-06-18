#!/bin/bash

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/

sed -E 's/(@.*) ([[:digit:]]).*/\1-\2/' merged_trimmed_2.fq > merged_trimmed_renamed_2.fq
