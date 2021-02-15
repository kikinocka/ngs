#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/mgm1/concat_enol_mic60.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/mgm1/concat_enol_mic60.MT.txt'
first=533
second=1050

$mt $aln $matrix $first $second 2> $out 1> $out
