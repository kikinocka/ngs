#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/noX/concat_enol-mgm1.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/noX/concat_enol-mgm1.MT.txt'
first=626
second=1975

$mt $aln $matrix $first $second 2> $out 1> $out
