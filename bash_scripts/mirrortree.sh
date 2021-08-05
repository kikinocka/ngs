#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/hsp70/mgm1/2-enol-orgn/concat_hsp70-mgm1.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/hsp70/mgm1/2-enol-orgn/concat_hsp70-mgm1.MT.txt'
first=663
second=616

$mt $aln $matrix $first $second 2> $out 1> $out
