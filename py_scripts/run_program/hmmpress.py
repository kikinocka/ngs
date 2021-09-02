#!/usr/bin/env python3
import os
import subprocess

hmmpress = '/Users/kika/miniconda3/bin/hmmpress'

os.chdir('/Users/kika/ownCloud/ARF_db-hmmscan/')
hmm = 'ScrollSaw_all.hmm'

subprocess.call('{} {}'.format(hmmpress, hmm), shell=True)
