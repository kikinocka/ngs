#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/combined/mgm1-containing/hsp70-enol/concat_enol-hsp70.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/combined/mgm1-containing/hsp70-enol/concat_enol-hsp70.MT.txt'
first=430
second=663

$mt $aln $matrix $first $second 2> $out 1> $out
