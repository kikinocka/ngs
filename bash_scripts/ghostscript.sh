#!/bin/sh

ghostscript='/Users/kika/miniconda3/pkgs/ghostscript-9.53.3-hb1e8313_1/bin/gs'

cd '/Users/kika/ownCloud/manuscripts/Euglenozoan_SAGs/figures/'

infile='Suppl.Fig.1.pdf'
outfile='Suppl.Fig.1_compr.pdf'

$ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$outfile $infile
