#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/mgm1/concat_enol-mgm1.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/mgm1/concat_enol-mgm1.MT.txt'
first=652
second=3242

$mt $aln $matrix $first $second 2> $out 1> $out
