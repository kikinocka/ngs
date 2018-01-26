#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''
Created on 16 nov 2016

@author: sam
'''

# IMPORT
import os , sys , argparse, re
import glob
import math
from subprocess import Popen, PIPE
from time import time
from datetime import datetime

# ARGUMENTS
ARGS = {}       # Command line arguments dictionary

def parseoptions( ):
        """ Docstring 
            .... """

        #print " ".join( sys.argv )

        parser = argparse.ArgumentParser( description=" " )
        parser.add_argument( '-f',  '--fasta',  help="Input: fasta sequence of contigs",   required=True )
        parser.add_argument( '-o',  '--output', help="Output: list of chimeric contigs" )
        parser.add_argument( '-1', '--lib1', help="DNA or RNA-seq first file", required=True)
        parser.add_argument( '-2', '--lib2', help="DNA or RNA-seq second file", required=True)           
        parser.add_argument( '-p', '--param', default=" --very-fast --fr --end-to-end --no-unal -p 6 ", help="Bowtie param, default '--very-fast --fr  --end-to-end --no-unal -p 6'" )
        parser.add_argument( '-n', '--nstdev', default=3, type=int,   help="Number of stdev differences for a coverage value to be considerated as chimeric cov < or > median +/- n.stdev. Default = 3")
        parser.add_argument( '-l', '--chimerlen', default=50, type=int,   help="Number of chimeric positions for a contig to be considered as chimeric. Default = 50bp") 
        #parser.add_argument( '-b',  '--blast',  default=0, type=int,   help="bla bla",   required=True|False )
        #parser.add_argument( '--rna', help="Export RNA", action='store_true', default=False)
        # Noter que les tirets dans les noms d'arguments sont transformes en souligne
        global ARGS             # Modify global variable ARGS
        ARGS = parser.parse_args()
        #globals().update(vars(args))        # Makes variables be seen globally

# MAIN
def main() :
    t1    = time()
    #print "BEGIN " + str( datetime.now() )

    # ARGS                                                                           
    parseoptions( )     # Parse sys.argv if you want quick and dirty script
                        # sys.argv[ 0 ] : name of the pgm
                        # ARGS.output to access "output" argument value
    
    # splittext removes the last extension (even if more than one '.' in the file name
    # fileout = os.path.splitext(ARGS.input)[0]
    # basename WITHOUT the complete path
    # fileout = os.path.basename(ARGS.input).split(".")[0]
    e = ""

    print "\n# MAPPING ON FASTA"
    if ARGS.output :
        fsam = os.path.splitext( ARGS.output ) [0] + ".sam"
    else :
        fsam    = os.path.splitext( ARGS.fasta )[0] + "_X_" + os.path.splitext( ARGS.lib1 )[0] + ".sam"

    # Build library
    transcriptslib  = os.path.splitext( os.path.basename( ARGS.fasta ) )[0].upper()
    if not os.path.exists( transcriptslib + ".1.bt2" ) : 
        cmd = "bowtie2-build -f " + ARGS.fasta + " " + transcriptslib 
        runcmd( cmd )
    # Mapping
    if not os.path.exists( fsam ) : 
        cmd = "bowtie2 " + ARGS.param + " -x " + transcriptslib + " -1 " + ARGS.lib1 + " -2 " +  ARGS.lib2 + " -S " + fsam 
        o,e = runcmd( cmd )
    printOrExit( fsam, e ) 

    fbam    = os.path.splitext( fsam )[0] + ".bam"
    if not os.path.exists( fbam ) :
        cmd = "sam2bam.py -s " + fsam 
        o,e = runcmd( cmd )
    printOrExit( fbam, e )
    
    # Coverage
    fbed    = os.path.splitext( fsam )[0] + ".bedgraph"
    if not os.path.exists( fbed ) :
        cmd     = "bedtools genomecov -ibam " + fbam + " -bg > " + fbed 
        o,e = runcmd( cmd )
    printOrExit( fbed, e )

    #NODE_192_length_6348_cov_406.923_ID_456219 0   1   138
    #NODE_192_length_6348_cov_406.923_ID_456219  1   2   216
    #NODE_192_length_6348_cov_406.923_ID_456219  2   3   219
    #NODE_192_length_6348_cov_406.923_ID_456219  3   4   224

    # Breakpoint detection
    # Strategy 1 
    # Sliding window (SW) of size x?
    # if current mean cov of SW is << or >> of previous, then breakpoint
    # Strategy 2
    # 1- compute mean (median ????) read cov for a contig
    # 2- sliding window with cov > or < mean +- 3sd are copy nb variations 
    print "\n# CHIMERIC CONTIG DETECTION ( At least %i positions with coverage outside median_coverage +/- %i x Stdev )"%( ARGS.chimerlen, ARGS.nstdev)
    if ARGS.output :
        fchimer = ARGS.output
    else :
        fchimer  = os.path.splitext( fbed )[0] + "_chimer.gff"
    if not os.path.exists( fchimer ) :
        #swlen   = 50            # Sliding window size
        #lswval  = [0] * swlen
        contig  = ""
        start   = 0
        end     = 0
        lcov    = []
        fin     = open( fbed , "r" )
        fout    = open( fchimer , "w" )
        for line in fin : 
            lcol     = line.split( "\t" )
            # It is a new contig
            if (not contig ==  lcol[0]) and len(contig) > 0 :   # Change contig, but not the first one
                meancov = float(sum(lcov)) / max(len(lcov), 1)
                medcov  = median( lcov )
                sdcov   = math.sqrt( sum([(c-meancov)**2 for c in lcov]) / len(lcov) )
                mincov  = max( medcov - ARGS.nstdev * sdcov, 0.0)
                maxcov  = medcov + ARGS.nstdev * sdcov
                chimcovsum  = 0
                chimcovnb   = 0
                for i in range(0,len(lcov) ) :
                    cov = lcov[ i ]
                    if cov < mincov or cov > maxcov :
                        chimcovnb   += 1
                        chimcovsum  += cov
                if chimcovnb > ARGS.chimerlen :
                    chimcovmean = chimcovsum / chimcovnb
                    offset      = abs(chimcovmean-meancov) 
                    fout.write( contig + "\tSaM\tchimeric\t1\t%i\t%i\t.\t.\tctg_cov_med=%.1f,ctg_cov_sd=%.1f,chim_cov_mean=%.1f,chim_cov_pos=%i\n"%(end,offset,medcov,sdcov,chimcovmean,chimcovnb) )  
                lcov    = []
            
            # Compute 
            contig,start,end,cov = lcol[0],int(lcol[1]), int(lcol[2]), int(lcol[3])         
            for i in range(start, end+1) :
                lcov.append( cov )
        fin.close()
        fout.close()
    
    printOrExit( fchimer, e )



    dt = time()-t1
    print " ---- time(s) = " + str(dt) + " // @SaM"

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

def printandflush( mess ) :
    sys.stdout.write('\r')
    sys.stdout.write( mess )
    sys.stdout.flush()

# How to run a shell command
def runshellcmd( infile ):
    e = ""      # Errors
    print "\n# COMMENT ABOUT MY CMD"
    outfile = os.path.splitext( infile )[0] + ".EXTENSION"
    if not os.path.exists( outfile ) :
        # An example of shell cmd
        cmd     = "cp %s %s" %( infile, outfile )
        o,e     = runcmd( cmd )
    printOrExit( outfile, e )
    print "\nDONE"

def printOrExit( afile, err="" ) :
    mess = ""
    if len(err) > 0 :
        mess += "ERROR: " + err + "\n" 
    if not os.path.exists( afile ) :
        mess += "File " + afile + " not created.\n"
    if len(err) > 0 or not os.path.exists( afile ) :                    # Arbitrary. If I put 0, does not work
        sys.exit( mess + "Exit program." )
    print "[OUT] " + afile

# o, e = runcmd( mycmd )
# OR runcmd( mycmd )
def runcmd( cmd, verbose=True ) : 
    if verbose == True :
        print cmd 
    p = Popen( cmd , shell=True, stdout=PIPE, stderr=PIPE)
    outmess,errmess  = p.communicate()
    return "".join(outmess), "".join(errmess) 

# Read a fasta file
# head,seq    = readFasta( MYFILE ).next()
# OR
#for head,seq in readFasta( MYFILE ) :
def readFasta( filename ) :
    ffasta  = open( ARGS.fasta, "r")
    #pathead = re.compile( ">\s*(\S+)\s+(.*)$")
    #recid   = ""
    rechead = ""
    recseq  = ""

    # For each line in file 1
    for line in ffasta :
        # New record found
        #mathead = pathead.match( line )
        #if mathead :
        if line[0] == '>' :
            # Print previous record
            if len(recid) > 0 :
                yield rechead,recseq
                #print "%s\t%s\n%s"%( recid, recdesc, recseq )
            # Get info for new record
            #recid   = mathead.group( 1 )
            rechead = line.strip()
            recseq  = ""
        else :
            recseq += line.strip()

    # Print last record
    yield rechead, recseq
    #print "%s\t%s\n%s"%( recid, recdesc, recseq )    



def readfile( filename ) :
    f = open( filename , "r" )
    # Line by line ; If all lines at once lines = f.readlines()
    # for n,line in enumerate( f ) :
    for line in f : 
        # do some stuff
        col     = line.split( "\t" )
        print line
    f.close()

    # All lines at once
    #with open( filename , 'r' ) as f :
    #    alist = [ line.strip() for line in f ]

def writeinfile( filename , content ) :
    f  = open( filename , "a" )    # a : append ; w : overwrite
    if isinstance( content , str ) :
        f.write( content + "\n" )
    else :
        f.write( "\n".join(content) )
    f.close()

def removefile( filename ) :
    if os.path.exists( filename ) :
                os.remove( filename )

def outfilename( infile , suffix ) :
    fpat    = re.compile( r"(.*)\.(.*)" )
    match   = fpat.match( infile )
    fout    = match.group(1) + suffix
    return fout

# http://biopython.org/DIST/docs/api/Bio.SeqIO._convert-module.html
def fastq_illumina_to_fastq_sanger_Dico() :
    mapping = "".join([chr(0) for ascii in range(0, 64)] 
                + [chr(33 + q) for q in range(0, 62 + 1)]
                + [chr(0) for ascii in range(127, 256)])
    assert len(mapping) == 256 
    return mapping







if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print >>sys.stderr, "Program canceled by user..."

