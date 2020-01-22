#!/bin/sh

computel='/home/software/computel/computel.sh'

workdir='/home/users/kika/p57/'
fw=''
rv=''
out=$workdir'p57_telomeres.csv'


$computel -1 $fw -2 $rv -o $out