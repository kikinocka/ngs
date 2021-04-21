#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/concat_mic60-opa1.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/concat_mic60-opa1.MT.txt'
first=2514
second=4470

$mt $aln $matrix $first $second 2> $out 1> $out
