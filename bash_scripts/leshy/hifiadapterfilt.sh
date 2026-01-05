#!/bin/sh

export PATH="/mnt/mokosz/home/kika/tools/HiFiAdapterFilt:/mnt/mokosz/home/kika/tools/HiFiAdapterFilt/DB:$PATH"

cd '/mnt/mokosz/home/kika/egracilis/PacBio/reads/'

hififilt='hifiadapterfilt.sh'
prefix='euglena_m21121_251212_153655.hifi_reads.bc2002'

$hififilt -p $prefix -t 10 2> $prefix.filt.log


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HiFiAdapterFilt done
