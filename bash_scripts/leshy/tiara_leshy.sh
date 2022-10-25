#!/bin/bash

cd '/mnt/mokosz/home/kika/workdir/'
metagenome='bml_meta.spades_def.fa'
out='tiara.out'
length=3000
cpu=10

tiara -i $metagenome -o $out -t $cpu -m $length --tf all --pr
# -m MIN_LEN, --min_len MIN_LEN
#                       Minimum length of a sequence. Sequences shorter than min_len are discarded. 
#                               Default: 3000.
# --first_stage_kmer FIRST_STAGE_KMER, --k1 FIRST_STAGE_KMER
#                       k-mer length used in the first stage of classification. Default: 6.
# --second_stage_kmer SECOND_STAGE_KMER, --k2 SECOND_STAGE_KMER
#                       k-mer length used in the second stage of classification. Default: 7.
# -p cutoff [cutoff ...], --prob_cutoff cutoff [cutoff ...]
#                       Probability threshold needed for classification to a class. 
#                               If two floats are provided, the first is used in a first stage, the second in the second stage
#                               Default: [0.65, 0.65].
# --to_fasta class [class ...], --tf class [class ...]
#                       Write sequences to fasta files specified in the arguments to this option.
#                               The arguments are: mit - mitochondria, pla - plastid, bac - bacteria, 
#                               arc - archaea, euk - eukarya, unk - unknown, pro - prokarya, 
#                               all - all classes present in input fasta (to separate fasta files).
# -t THREADS, --threads THREADS
#                       Number of threads used.
# --probabilities, --pr
#                       Whether to write probabilities of individual classes for each sequence to the output.
# -v, --verbose         Whether to display some additional messages and progress bar during classification.
# --gzip, --gz          Whether to gzip results or not.

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Tiara done
