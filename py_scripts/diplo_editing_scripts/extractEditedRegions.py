#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''
Created on 06 feb 2017

2017.02.07  Rather use edited sequence as template rather than non-edited  

@author: sam
'''

# IMPORT
import os , sys , argparse, re
import glob
from subprocess import Popen, PIPE
from time import time
from datetime import datetime
from Bio import SeqIO
import operator
import numpy
from collections import Counter

# ARGUMENTS
ARGS        = {}       # Command line arguments dictionary

''' USAGE 
'''

def parseoptions( ):
        """ Docstring 
            .... """

	print " ".join( sys.argv )

        parser = argparse.ArgumentParser( formatter_class=argparse.RawDescriptionHelpFormatter, description="Extract non-edited and edited sequences with translation")
        parser.add_argument( '-f',  '--fasta',   help="EDITED RNA reference fasta",   required=True )
        parser.add_argument( '-g',  '--gff',   help="gff file for reference including SNP features",   required=True )
        
        #parser.add_argument( '-t',  '--snpfreqmin',    default=0.5, type=float, help="SNP strictly above this frequency threshold will be incorporated.")
        #parser.add_argument( '-T',  '--snpfreqmax',    default=1.0, type=float, help="SNP strictly below this frequency threshold will be incorporated.")
        #parser.add_argument( '-q',  '--snpqual',    default=1000, type=int, help="SNP strictly above this quality will be incorporated.")


        #parser.add_argument( '-b',  '--blast',  default=0, type=int,   help="bla bla",   required=True|False )
        # Noter que les tirets dans les noms d'arguments sont transformes en souligne
        global ARGS             # Modify global variable ARGS
        ARGS = parser.parse_args()
        #globals().update(vars(args))        # Makes variables be seen globally

PREFIX 		= ""
LGFFCTG 	= []            # List of gff contigs with corresponding lines in the same order as in the file
GFFRRNA		= 'rrna' 	# GFF feature for rRNA in lower case
GFFPOLYU	= 'poly-u'	# GFF feature for poly-u in lower case
GFFCHROM	= 'chromosome'	# GFF feature for chromosome in lower case
GENETIC_CODE4 	= {	'TTT':'F', 'TTC':'F',
			'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 
			'ATT':'I', 'ATC':'I', 'ATA':'I',
			'ATG':'M',
			'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
			'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
			'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 
			'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 
			'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 
			'TAT':'Y', 'TAC':'Y',
			'TAA':'*', 'TAG':'*',
			'CAT':'H', 'CAC':'H',
			'CAA':'Q', 'CAG':'Q',
			'AAT':'N', 'AAC':'N',
			'AAA':'K', 'AAG':'K',
			'GAT':'D', 'GAC':'D',
			'GAA':'E', 'GAG':'E',
			'TGT':'C', 'TGC':'C',
			'TGA':'W', 'TGG':'W',
			'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 
			'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
INITCODON4	= ['TTA', 'TTG', 'CTG', 'ATT', 'ATC', 'ATA', 'ATG', 'GTG']
STOPCODON4	= ['TAA', 'TAG']

# MAIN
def main() :
	t1    = time()
	print "BEGIN " + str( datetime.now() )
        
    	# ARGS                                                                           
	parseoptions( )     # Parse sys.argv if you want quick and dirty script
                        # sys.argv[ 0 ] : name of the pgm
		
    	# Read GFF ; key = feature id, value = gff
    	dgff    = readgff( ARGS.gff )

    	# Read fasta ; key = fasta id, value = fasta
    	dfasta  = readFasta( ARGS.fasta )

        global LGFFCTG
        for rna in LGFFCTG :        # For all rna "contigs"
            start   = 0             # Start of snp cluster
            lpos    = []
            lref    = []
            lfreq   = []
            lgff    = dgff[ rna ]   # gff lines associated with this contig
            genetype= 'exon'
            for g in lgff :
                if not g.feature == 'snp' :
                    genetype    = g.feature
                if g.feature == 'snp' :
                    lpos.append( g.start)
                    lref.append( g.dattributes["ref"] )
                    lfreq.append( g.dattributes["freq"] )

                # End of cluster => print it
                if len(lpos) > 0 and (not g.feature  == 'snp' or lgff[-1] == g) :
                    start       = (max((lpos[0]//3) - 2, 0) * 3) + 1                 # Begins one or two codon upstream
                    end         = (min((lpos[-1]//3)+ 2, len(dfasta[rna].seq)) * 3)  # Ends one or two codon after last pos
                    #start = 1
                    #end = len(dfasta[rna].seq)
                    tmpnuced      = dfasta[rna].seq[start-1:end]
                    print "\n%s [%i - %i]"%(rna, start, end) 
                    tmpnuc    = ''
                    tmpfreq     = ''
                    tmpprot     = ''
                    tmpproted   = ''
                    for i in range ( start, end+1 ) :
                        # This is an edited position
                        if i in lpos :
                            idx         = lpos.index( i )
                            # Seq 
                            tmpnuc    += lref[ idx ]
                            # freq
                            freq        = float(lfreq[ idx ])
                            if freq < 0.2 :
                                tmpfreq += '.'
                            elif freq < 0.5 :
                                tmpfreq += ':'
                            elif freq < 0.8 :
                                tmpfreq += '|'
                            else :
                                 tmpfreq += '*'
                        # Position not edited
                        else :
                            tmpnuc      += dfasta[rna].seq[ i-1 ]
                            tmpfreq     += ' ' 
                    if not genetype == GFFRRNA :
                        print translate( tmpnuc, start )
                        print addSpaceEveryCodon( tmpnuc )   
                        print addSpaceEveryCodon( tmpfreq )
                        print addSpaceEveryCodon( tmpnuced )
                        print translate( tmpnuced, start )
                    else:
                        print tmpnuc
                        print tmpfreq
                        print tmpnuced
                    
                    # init for next 
                    lpos    = []
                    lref    = []
                    lfreq   = []
	dt = time()-t1

        print "Variant frequency symbols:\n\t[0.0-0.2[ .\n\t[0.2-0.5[ :\n\t[0.5-0.8[ |\n\t[0.8-1.0] *"

	print "END " + str( datetime.now() ) + " ---- time(s) = " + str(dt)


def addSpaceEveryCodon( seq ) :
    tmp = ''
    for i in range(0,len(seq)) :
        tmp += seq[i]
        if (i+1)%3 == 0 :
	    tmp += ' '
    return tmp
	
def filename( feature=None ) :
	#global PREFIX
        today = datetime.now()
	name = "%s"%( PREFIX,)
	if not feature is None and len( feature) > 0 :
		name += "_%s"%(feature,)
        # File already exists => backup
        bckup = name + "_%i%02i%02i"%(today.year, today.month, today.day) 
        for extension in [ ".gff", ".fasta"] :
            if os.path.exists( name + extension ) :
                cmd = "cp " +  name + extension + " " + bckup  + extension
                runcmd( cmd )
                print "#[OUT] Back-up file: %s"%( bckup  + extension ,) 
	return name
		

def updateSeqWithSNPs( seq, lvcf ) :
	lseq 	= list(seq)
	if not lvcf is None :
		for v in lvcf :
			lseq[v.pos-1] = v.altmax
	return "".join(lseq)

def gffWithSNPs( lvcf, contig, featureName, shift , featureStrand ) :
	gfflines = ""
	for v in lvcf :
		snpposstart = v.pos + shift      
		snpposend	= snpposstart + len(v.altmax) - 1
		snpname = "%s_%i_%s>%s"%(featureName,snpposstart,v.ref,v.altmax)
		snpdesc	= "ref=%s;alt=%s;freq=%.2f;qual=%.2f"%(v.ref,v.altmax,v.altmaxfreq,v.qual)
		gfflines += "%s\textractMitoSeq\tSNP\t%i\t%i\t.\t%s\t0\tID=%s;%s\n"%(contig,snpposstart,snpposend,featureStrand,snpname,snpdesc)
	return gfflines

def translate( seq, start ) :
	pos 	= 0 
	seq 	= seq.upper()
	seq 	= seq.replace('U','T') 
	lseq 	= list(seq)
	pep 	= ""

	while pos < len(lseq) :
		codon 	= "".join(lseq[pos:pos+3])
		if codon in GENETIC_CODE4 :
                        if pos == 1 and start == 1 and codon in INITCODON4 :
                            pep += ' M  '
                        else :
			    pep += ' ' + GENETIC_CODE4[ codon ] + '  '
                        if codon in STOPCODON4 :
                            return pep
		else :
			pep 	+= ' ?  '
		pos	+= 3
	return pep


#######  GFF
def readgff( fgff ) :
	print "\n#[IN] Read GFF file %s"%( fgff )

	f       	= open( fgff, "r" )     
	dgff    	= {}
	n               = 0
        global LGFFCTG

	for line in f :         
		if line[0] == '#' :     # comment             
			continue         
		if not line.strip() :   # Empty lines             
			continue         
		l   = line.split("\t")         
		if len(l) < 9 :         # Not a gff line  
			print "\tNot a gff line: %s"%( line.strip(), )           
			continue         
		g   = GFF(l)
                # Do not store features that do not have name
		if not g is None and len(g.contig) > 0 :
			n += 1
                        if not g.contig in dgff :
				LGFFCTG.append( g.contig )
				dgff[ g.contig ] = []
			dgff[g.contig].append( g )
			
	f.close()
	print "\t%i line(s) stored"%( n, )

	return dgff

class GFF : 
	def __init__(self, lvalues):
		if len(lvalues) < 9 :
			return None 
		self.contig      = lvalues[0].strip() 
		self.source     = lvalues[1].strip() 
		self.feature    = lvalues[2].strip().lower()
		self.start      = int(lvalues[3])
		self.end        = int(lvalues[4])
		self.score      = lvalues[5].strip()
		self.strand     = lvalues[6].strip()
		# if self.strand not in [ '.', '-', '+' ] :
		#     self.strand = '.'
		self.frame      = lvalues[7].strip()
		# if self.frame not in [ '.', '0', '1', '2' ] :
		#     self.frame = '.'
		self.attribute  = lvalues[8]
		self.dattributes = {}
		self.id         = ""
                self.name       = ""
		self.parent	= []

		# Parse attributes
		# To find attribute ID : dattributes["id"]
		# !!! attribute keys in LOWER CASE
		latt    = self.attribute.strip().split(';')
		for a in latt :
                        if len(a.strip()) == 0 or len(a.split("=")) < 2 :
                            continue
			k,v = a.split("=")
			if not k is None and not v is None :
				self.dattributes[ k.strip().lower() ] = v.strip()
	
		# ID is unique
		if "id" in self.dattributes :
			self.id     = self.dattributes["id"]
		else :
			self.id     = "%s_%s_%i-%i"%( self.contig, self.feature, self.start, self.end )
                # Name is the gene name
                if "name" in self.dattributes : 
                        self.name   = self.dattributes["name"]
                
		# Parent
		if "parent" in self.dattributes :
			lparent = self.dattributes["parent"].split(',')
			for p in lparent :
				self.parent.append( p )
	    
	def filtergff(self, feature ) :
		return self.feature == feature.lower() 

	def gff2text(self) :
		line = "%s\t%s\t%s\t%i\t%i\t%s\t%s\t%s\t%s"%(self.contig, self.source, self.feature, self.start, self.end, 
                                                self.score, self.strand, self.frame, self.attribute)  
		return line


		
# http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary        
def keyformaxdicoval( d ) :
	if len(d) == 0 :
		return 0
	return max(d.iterkeys(), key=(lambda key: d[key]))

	
###### FASTA
def readFasta( fastafile ) :
	print "\n#[IN] Parsing fasta file " 
	ffasta  = open( fastafile, "r" ) 
	dfasta  = {} 
	nfasta  = 0  
	for rec in SeqIO.parse(ffasta, "fasta") :
		afasta = fasta( rec.id, rec.description, "%s"%(rec.seq,) )
		dfasta[rec.id] = afasta
		#print rec
		#print rec.id + " " + rec.seq
	ffasta.close()
	print "\t%i sequence(s) read"%( len(dfasta), )

	return dfasta

class fasta : 
	def __init__( self, name, desc="", seq="") :   
		self.name = name
		self.desc = desc
		self.seq  = seq

###### VCF
def readVCF( vcffile, snpqual, snpfreqmin, snpfreqmax ) :
	print "\n#[IN] Parsing VCF file " 
	fvcf 	= open( vcffile, "r" )
	lvcf 	= []
	nline	= 0
	for line in fvcf :         
		if line[0] == '#' :     # comment             
			continue         
		if not line.strip() :   # Empty lines             
			continue         
		l   = line.split("\t")         
		if len(l) < 8 :         # Not a gff line  
			print "\tNot a vcf line: %s"%( line.strip(), )           
			continue      
		nline 	+= 1   
		v	= vcf(l, snpqual, snpfreqmin, snpfreqmax)
		if not v.fail :
			lvcf.append(v)
	fvcf.close()
	print "\t%i line(s) read, %i lines not passing SNP qual > %i and SNP freq in [%.2f,%.2f]"%( nline, nline-len(lvcf), snpqual, snpfreqmin, snpfreqmax )
	return lvcf
		
class vcf :
	def __init__(self, lvalues, snpqual, snpfreqmin, snpfreqmax):
		# Does the init failed
		self.fail 	= False
		
		if len(lvalues) < 8 :
			self.fail = True
		else :
			self.contig     = lvalues[0].strip() 
			self.pos      	= int(lvalues[1])
			self.dbid 		= lvalues[2].strip()
			self.ref		= lvalues[3].strip()
			
			# Alternative allele
			tmp				= lvalues[4].strip()
			self.alt		= tmp.split(',')
			self.altmax 	= ""
			
			self.qual 		= float(lvalues[5])
			self.qualfilter	= lvalues[6].strip()
			if self.qual < float(snpqual) :
				self.fail = True
			
			self.info 	= lvalues[7].strip()
			self.dinfo 	= {}
	
			# Parse attributes
			linfo   = self.info.split(';')
			for i in linfo :
				if '=' in i :
					k,v = i.split("=")
					if not k is None and not v is None :
						self.dinfo[ k.strip() ] = v.strip()
					
			# Allele frequency;Same order as self.alt
			self.altfreq	= []
			if "AF" in self.dinfo :
				self.altfreq = self.dinfo["AF"].split(',')
				
			# Search the max allele
			self.altmaxfreq = 0.0
			for i in range(0,len(self.alt)) :
				if float(self.altfreq[i]) > self.altmaxfreq :
					self.altmaxfreq = float(self.altfreq[i])
					self.altmax 	 = self.alt[i]

			if self.altmaxfreq < snpfreqmin :
				self.fail = True
			if self.altmaxfreq > snpfreqmax :
				self.fail = True

				
			if self.fail :
				print "\t- SNP DISCARDED : %s\t%i\t%s->%s\tqual=%.2f, freq=%.2f"%(self.contig, self.pos,self.ref, self.altmax, self.qual, self.altmaxfreq)
                        else :
                                print "\t+ SNP RETAINED : %s\t%i\t%s->%s\tqual=%.2f, freq=%.2f"%(self.contig, self.pos,self.ref, self.altmax, self.qual, self.altmaxfreq)
		
	
def revcomp(sequence ) :
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


def printandflush( mess ) :
    sys.stdout.write('\r')
    sys.stdout.write( mess )
    sys.stdout.flush()

# o,e = runcmd( mycmd )
# OR runcmd( mycmd )
def runcmd( cmd, verbose=False ) : 
    if verbose == True :
        print cmd 
    p = Popen( cmd , shell=True, stdout=PIPE, stderr=PIPE)
    outmess,errmess  = p.communicate()
    return "".join(outmess), "".join(errmess) 

def readfile( filename ) :
    f = open( filename , "r" )
    # Line by line ; If all lines at once lines = f.readlines()
    for line in f :
        # do some stuff
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

def version():
    mess =  "# Built on " + str( datetime.now() ) + "\n"
    mess +=  "# Built from " + os.path.abspath( ARGS.fasta ) + " modified on " + str(datetime.fromtimestamp(os.path.getmtime( ARGS.fasta ))) + "\n"
    mess +=  "# Built from " + os.path.abspath( ARGS.gff ) + " modified on " + str(datetime.fromtimestamp(os.path.getmtime( ARGS.gff ))) + "\n"
    if ARGS.vcf :
        mess +=  "# Built from " + os.path.abspath( ARGS.vcf ) + " modified on " + str(datetime.fromtimestamp(os.path.getmtime( ARGS.vcf ))) + "\n"
    return mess 

def loginfo( afile ) : 
    flog    = open( "log.txt", "a")
    flog.write( "# Create log.txt \n")
    flog.write( version() )
    flog.close() 




if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print >>sys.stderr, "Program canceled by user..."


