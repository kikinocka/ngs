#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/hsp70/opa1/concat_hsp70-mic60.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/hsp70/opa1/concat_hsp70-mic60.MT.txt'
first=593
second=390

$mt $aln $matrix $first $second 2> $out 1> $out
