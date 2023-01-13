#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/kinetoplastids/IDH/tree/idh1-2/combined'

tree=$path'IDH1-2.CD.nex.con.tre'
bootstrap=$path'IDH_1_2_guide_tree_BS.boottrees'
out=$path'IDH1-2.CD.mb+iqtree.tre'

$placer $tree $bootstrap $out
