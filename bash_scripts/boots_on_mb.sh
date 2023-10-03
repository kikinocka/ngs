#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ver10/combined/'

tree=$path'arfs.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.arfs.CD'
out=$path'arfs.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
