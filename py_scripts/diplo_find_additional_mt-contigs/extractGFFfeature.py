#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''
Created on 11 mars 2013

@author: sam
2015 05 19 : Handling feature on reverse strand
'''

# IMPORT
import os , sys , argparse, re
import glob
from subprocess import Popen, PIPE
from time import time
from datetime import datetime
from Bio import SeqIO

# ARGUMENTS
ARGS = {}       # Command line arguments dictionary

FTELL   = "FTELL"
NLINE   = "NLINE"

SEQ         = "SEQ"
SOURCE      = "SOURCE"

FEATURE     = "FEATURE"
CDS         = "CDS"
FIVE_PRIME_UTR  = "five_prime_UTR"
START       = "START"
END         = "END"
SCORE       = "SCORE"
STRAND      = "STRAND"
FRAME       = "FRAME"
ATTRIBUTE   = "ATTRIBUTE"
ID          = "id"
PARENT      = "parent"
NOTE        = "name"

STATUS      = "STATUS"
ORIGINAL    = "ORIGINAL"
MODIFIED    = "MODIFIED"
NEW         = "NEW"

DEBUG = True
DEBUGFILE   = "extractGFFfeature.out"

def parseoptions( ):
        """ Docstring 
            .... """

        print " ".join( sys.argv )

        exgff = "[--gff] GFF file:\n\
7180000453559   transdecoder    gene    3546    5608    .       +       .       ID=CUFF.106.1|g.336;Name=ORF\n\
7180000453559   transdecoder    mRNA    3546    5608    .       +       .       ID=CUFF.106.1|m.336;Parent=CUFF.106.1|g.336;Name=ORF\n\
7180000453559   transdecoder    five_prime_UTR  3546    3547    .       +       .       ID=CUFF.106.1|m.336.utr5p1;Parent=CUFF.106.1|m.336\n\
7180000453559   transdecoder    exon    3546    5608    .       +       .       ID=CUFF.106.1|m.336.exon1;Parent=CUFF.106.1|m.336\n\
7180000453559   transdecoder    CDS     3548    4987    .       +       .       ID=cds.CUFF.106.1|m.336;Parent=CUFF.106.1|m.336\n\
7180000453559   transdecoder    three_prime_UTR 4988    5608    .       +       .       ID=CUFF.106.1|m.336.utr3p1;Parent=CUFF.106.1|m.336\n\
"
        parser = argparse.ArgumentParser( description="Extract feature (third column gff keyword) defined in gff and output corresponding sequences\n\
            %s"%(exgff,) )
        parser.add_argument( '-f',  '--fasta',    help="Input fasta sequence file",   required=True )
        parser.add_argument( '-g',  '--gff',    help="GFF file ",   required=True )
        parser.add_argument( '-l',  '--list',    help="List of feature to filter. If no parameters are set, all features are extracted ")
        parser.add_argument( '-o',  '--out',   help="Output fasta sequence file" )
        global ARGS             # Modify global variable ARGS
        ARGS = parser.parse_args()

# MAIN
def main() :
    t1    = time()
    print "BEGIN " + str( datetime.now() )
    print "!!!! Features composed of different parts (ex: CDS composed of different exons i.e. features with \"parents\") are not merged\n\
    They are reported independently\n"

    # ARGS                                                                           
    parseoptions( )     # Parse sys.argv if you want quick and dirty script
                        # sys.argv[ 0 ] : name of the pgm
                        # ARGS.output to access "output" argument value
    
    # Outfile
    out      = ""
    if ARGS.out :
        out      = ARGS.out 
    else :
        out      = os.path.basename(ARGS.fasta).split(".")[0] + "_filt.fasta"
    #print "=>Output extracted sequence file of features: " + out

    lgff   = readGFF( ARGS.gff ) # List of genome gff lines
    lfeatname   = []
    if not ARGS.list is None :
        lfeatname   = ARGS.list.split(",")
    #print lfeatname
    lgfffeat    = filterGFF( lgff, lfeatname )   # sublist of selected features from genome gff lines
    lseq        = readFasta( ARGS.fasta )       # dico of sequence from genome 

    fout        = open(out, 'w')
    ffasta      = open(ARGS.fasta, 'r')
    fdebug      = open(DEBUGFILE, 'w')
    nfeat       = 0                         # Number of feature extracted

    # Search for sequence of features
    for seq in lseq :
        seqATGC     = ""
        ffasta.seek( seq[FTELL] )
        ffasta.readline()               #header
        for li in range(0,seq[NLINE]-1) :
            seqATGC += ffasta.readline().strip()
        #print seq[ID]
        #print seqATGC

        for feat in lgfffeat :

            if feat[SEQ] == seq[ID] :
                mess = "%s\t%s\t%i-%i"%(seq[ID], feat[FEATURE],feat[START], feat[END])
                #print mess
                fdebug.write( mess + "\n" )
                if feat[END] > len(seqATGC) :
                    print "Feature end (%i) > length sequence (%i) for %s" %(feat[END], len(seqATGC), mess)
                else :
                    identif = "%s_%s_%i-%i"%(seq[ID], feat[FEATURE],feat[START], feat[END])
                    if not feat['name'] is None and len(feat['name']) >0:
                        identif = feat['name']
                    fout.write(">%s\n"%(identif,))
                    start   = int(feat[START]) - 1
                    end     = int(feat[END]) 
                    if feat[STRAND] == '-' :
                        fout.write("%s\n"%revseq(seqATGC[start:end]) )
                    else :
                        #print seqATGC[start:end]
                        fout.write("%s\n"%seqATGC[start:end])
                    nfeat += 1        

    fout.close()
    ffasta.close()
    fdebug.close()

    print "[OUT] %i features extracted and written to %s" %(nfeat, out)

    dt = time()-t1
    print "\nEND " + str( datetime.now() ) + " ---- time(s) = " + str(dt)

def revseq( sequence ) : 
    if not sequence :
        return ''

    basecomplement = {'a':'t', 'c':'g', 't':'a', 'g':'c' , 'A':'T' , 'C':'G' , 'T':'A' , 'G':'C' }
    letters = list(sequence)
    letters.reverse()
    rc = ''
    for base in letters:
        if base in basecomplement :
            rc += basecomplement[base]
        else :
            rc += base
    return rc

def readFasta( ffasta ):

    # Read seq file
    # Description line : >7180000433251_4 [5820 - 7673] 1134 24001 bases
    f           = open(ffasta, "r")
    #f_iterator  = SeqIO.parse(f, "fasta")    # Fasta iterator
    patseq      = re.compile("^>\s*(\S+)")
    lseqs       = []
    ftell       = f.tell()
    line        = f.readline()
    li          = 0
    n           = 0
    seq         = {}
    nseq        = 0
    #seqATGC     = ""

    while line  :
        li += 1
        #print record.description

        if line[0] == '>' :

            match   = re.match( patseq, line )
            if match :
                # Update previous ORF nb of lines. For the first round, update the empty dico, not a pbm
                #print seq
                #print seqATGC
                seq[NLINE]  = nseq

                # New seq
                nseq    = 0
                #seqATGC = ""
                n       += 1
                seq         = {}
                seq[ID]     = match.group(1)
                seq[FTELL]  = ftell
                lseqs.append(seq)
        #else :
        #    seqATGC += line.strip()

        nseq    += 1
        ftell   = f.tell()
        line    = f.readline()

        if li%100==0 :
            mess = "%i\t lines read - %i\t sequences found"%(li,n)
            printandflush( mess )
    seq[NLINE]  = nseq
    print "\r[IN] %i\t lines read in fastat file - %i\t sequences found"%(li,n)
    f.close()

    return lseqs

def readGFF( fgff ) :
    f       = open( fgff, "r" )
    lgff    = []
    for line in f :
        if line[0] == '#' : # comment
            continue
        if not line.strip() :   # Empty lines
            continue
        l               = line.split("\t")
        if len(l) < 9 :     # Not a gff line
            continue
        gff             = newgffline()
        gff[SEQ]        = l[0].strip()
        gff[SOURCE]     = l[1].strip()
        gff[FEATURE]    = l[2].strip()
        gff[START]      = int(l[3])
        gff[END]        = int(l[4])
        gff[SCORE]      = l[5].strip()
        gff[STRAND]     = l[6].strip()
        gff[FRAME]      = l[7].strip()
        gff[ATTRIBUTE]  = l[8].strip()
        gff[STATUS]     = ORIGINAL
        latt            = gff[ATTRIBUTE].split(';')
        for a in latt :
            if '=' in a :
                k,v = a.split('=')
                gff[k.strip().lower()] = v.strip().lower()
        lgff.append(gff)
    return lgff

def filterGFF( lgff, lfeatname ) :
    # Extract ALL feature => all gff entries
    if lfeatname is None or len(lfeatname) == 0 :
        return lgff

    lfeaturelower = []
    for feat in  lfeatname :
        lfeaturelower.append( feat.lower() )
    #print lfeaturelower
    lfeatgff = []
    for g in lgff :
        if g[FEATURE].lower() in lfeaturelower :
            lfeatgff.append(g)

    print "[IN] %i features found in GFF file" %(len(lfeatgff),)
    return lfeatgff


# def findORF( hmm, lORFS) :
#     for orf in lORFS:
#         if orf[SEQ] == hmm[SEQ] and orf[STRAND] == hmm[STRAND] :
#             hmmlen      = hmm[END] - hmm[START]
#             overl       = overlap( hmm[START], hmm[END], orf[START], orf[END] ) / hmmlen
#             #if overl    == 1 and inframe(hmm[START], orf[START] ) : 
#             if hmm[STRAND] == "+" :
#                 if overl ==  1 and inframe(hmm[START], orf[START]) :
#                     return orf
#             else :
#                 if overl ==  1 and inframe(hmm[END], orf[END]) :
#                     return orf
#     return None

# def matchInGenomeCDS( hmm, lCDS ):
#     for cds in lCDS :
#         if cds[SEQ] == hmm[SEQ] and cds[STRAND] == hmm[STRAND]:
#             hmmlen      = hmm[END] - hmm[START]
#             overl       = overlap(hmm[START], hmm[END], cds[START], cds[END] ) / hmmlen
#             # hmm and CDS overlap and both are inframe 
#             # => hmm is in an already existing ORF
#             # PBM : to see if features are infrmae, we need the "phase" info in GFF
#             # if hmm[STRAND] == "+" :
#             #     if overl >  0.95 and inframe(hmm[START], cds[START]) :
#             #         return True
#             # else :
#             #     if overl >  0.95 and inframe(hmm[END], cds[END]) :
#             #         return True
#             if overl > 0.95 :
#                 return True
#     return False

# def gff2text( gff ) :
#     patnote     = re.compile("Note=(\S+)", re.IGNORECASE)
#     patid     = re.compile("Id=(\S+)", re.IGNORECASE)
#     patparent     = re.compile("Parent=(\S+)", re.IGNORECASE)

#     line    = ""
#     line    += "%s\t"%(gff[SEQ],)
#     line    += "%s\t"%(gff[SOURCE],)
#     line    += "%s\t"%(gff[FEATURE],)
#     line    += "%i\t"%(gff[START],)
#     line    += "%i\t"%(gff[END],)
#     line    += "%s\t"%(gff[SCORE],)
#     line    += "%s\t"%(gff[STRAND],)
#     line    += "%s\t"%(gff[FRAME],)

#     attribute = gff[ATTRIBUTE] 
#     if len(gff[ID]) > 0 and not patid.search(attribute) :
#         attribute = "ID=%s;"%(gff[ID],) + attribute
#     if len(gff[PARENT]) > 0 and not patparent.search(attribute) :
#         attribute += "Parent=%s;"%(gff[PARENT],)

#     if len(gff[NOTE]) > 0 :
#         if patnote.search( gff[ATTRIBUTE] ) :
#             attribute   = patnote.sub("Note=%s" % gff[NOTE], gff[ATTRIBUTE])
#         else :
#             attribute   = gff[ATTRIBUTE] + ";Note=%s"%(gff[NOTE])

#     line    += "%s\t"%(attribute)
#     return line

# def overlap( Astart, Aend, Bstart, Bend ) :
#     return max(0, min(Aend, Bend) - max(Astart, Bstart))

# Are A and B in frame
# def inframe( Astart, Bstart ) :
#     return ( ((Astart - Bstart)%3) == 0 )

def newgffline(seq='', source='', feature='', start='', end='', score='.', strand='.', frame='.', idfeat='', parent='', note='', ) :

    latt = []
    if len(idfeat) > 0 :
        latt.append("%s=%s"%("ID",idfeat))
    if len(parent) > 0 :
        latt.append("%s=%s"%("Parent",parent))
    if len(note) > 0 :
        latt.append("%s=%s"%("Note",note))

    attribute  = ';'.join(latt)

    d = {   SEQ:seq,     SOURCE:source,  FEATURE:feature, START:start,   END:end, SCORE:score,
            STRAND:strand,  FRAME:frame,   ATTRIBUTE:'', ID:idfeat, PARENT:parent, NOTE:note, STATUS:NEW}
    return d


def printandflush( mess ) :
    sys.stdout.write('\r')
    sys.stdout.write( mess )
    sys.stdout.flush()


def removefile( filename ) :
    if os.path.exists( filename ) :
                os.remove( filename )


if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print >>sys.stderr, "Program canceled by user..."

