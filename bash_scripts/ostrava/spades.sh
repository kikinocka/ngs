#!/bin/bash
#SBATCH --job-name=spades
#SBATCH --output=spades.%j.out
#SBATCH --error=spades.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --time=24:00:00
#SBATCH --export=ALL

work_dir='/home/kika/pkld/spades/'
read_dir='/home/kika/pkld/trimmed_all/'
fwd=$read_dir'BHU814_trimmed_1.fq.gz'
rev=$read_dir'BHU814_trimmed_2.fq.gz'

cd $work_dir
conda run -n assembly spades.py \
	--pe1-1 $fwd --pe1-2 $rev -t 40 --careful -o $work_dir
