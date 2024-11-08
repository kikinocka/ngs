#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/mantamonas/ARFs/ver2/'

tree=$path'mrbayes/arfs.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'raxml/RAxML_bootstrap.arfs.CD'
out=$path'combined/arfs.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
