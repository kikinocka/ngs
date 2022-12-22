#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/kinetoplastids/IDH/tree/ver2/combined/'

tree=$path'IDHs.linsi.automated1.CD.nex.con.tre'
bootstrap=$path'automated1-strict_MFP_madd_guide_tree_stdBoots.boottrees'
out=$path'IDHs.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
