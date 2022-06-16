#!/usr/bin/env python3
import os

raxml = '/Users/kika/miniconda3/bin/raxmlHPC-PTHREADS'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/SM/ver4/')
tree = 'MrBayes/sm.trimal_gt-0.8.nwk'
bootstraps = 'RAxML/RAxML_bootstrap.sm'
out = 'sm.ML_on_MB'


os.system('{} -m PROTGAMMALG4X -p 12345 -f b -t {} -z {} -n {} -T 5'.format(raxml, tree, bootstraps, out))
