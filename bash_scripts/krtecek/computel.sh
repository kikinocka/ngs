#!/bin/sh

computel='/home/software/computel/computel.sh'

workdir='/home/users/kika/p57/'
fw='p57_trimmed_1.fq'
rv='p57_trimmed_2.fq'
out=$workdir'computel/'
pattern='TTAGGG'
threads=15

$computel -proc $threads -pattern $pattern -1 $fw -2 $rv -o $out
