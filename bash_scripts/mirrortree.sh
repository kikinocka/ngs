#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/concat_enol-mic60.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/concat_enol-mic60.MT.txt'
first=1138
second=2483

$mt $aln $matrix $first $second 2> $out 1> $out
