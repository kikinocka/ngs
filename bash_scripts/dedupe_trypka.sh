#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/genome/merged'
merged=$read_dir'YPF1601_merged.fq'
deduplicated=$read_dir'YPF1601_merged_deduplicated.fq'

/home/kika/tools/bbmap/dedupe.sh in=$merged out=$deduplicated ac=f