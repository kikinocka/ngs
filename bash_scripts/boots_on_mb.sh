#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/kinetoplastids/IDH/tree/idh3/combined'

tree=$path'IDH3.CD.nex.con.tre'
bootstrap=$path'IDH3_guide_tree_stdBoots.boottrees'
out=$path'IDH3.CD.mb+iqtree.tre'

$placer $tree $bootstrap $out
