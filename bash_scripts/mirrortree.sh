#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/mgm1/no_redundancy_trimmed/concat_enol-mic60.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/mgm1/no_redundancy_trimmed/concat_enol-mic60.MT.txt'
first=430
second=494

$mt $aln $matrix $first $second 2> $out 1> $out
