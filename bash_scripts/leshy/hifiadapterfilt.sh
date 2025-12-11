#!/bin/sh

cd '/mnt/mokosz/home/kika/egracilis/PacBio/hifi_reads/'

hififilt='hifiadapterfilt.sh'
name='m21121_251126_103750'

$hififilt -p $name -t 10 2> $name.filt.log


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HiFiAdapterFilt done
