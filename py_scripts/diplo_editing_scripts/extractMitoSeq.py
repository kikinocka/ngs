#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''
Created on 31 august 2015

@author: sam
2017 02 07
    - When modules are on '-' strand, report reverse-complement for SNPs
2016 11 09
    - Switch "name" and "id" function. ID is the unique identifier of a feature whereas features with same name group together features belonging to the same gene
 
2016 11 02
    - if a file with the same name already exists, create a backup with current date

2015 11 20
    - Start codons are translated in M even if it is not ATG

2015 10 30
    - Handling rna sequences not ending with a stop codon
    - Annotation of poly-A in gff
2015 09 17
    - Exon are always on the + strand with regard to RNA
    - rRNA were not exported in module files
2015 09 15
    - Adding parameter -T for max SNP frequency
    - List of SNP retained in sequence are written in the gff file
    - Add '-snp' to the name of output files when a VCF file is submitted

2015 10 15
    - Bug in cassette export with SNP
    - Add 'snp' to file casssette name when VCF file is used
 
WARNING :
	- Never tested with insertion and deletion in VCF
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
 EXPORT NON-EDITED MODULES, RNA and PROTEINS
>> extractMitoSeq.py -f Dp_mito_Cass.fasta -g Dp_mito_Cass.gff --module --rna --pep -o Dp_mito 

 EXPORT EDITED MODULES, RNA and PROTEINS 
>> extractMitoSeq.py -f Dp_mito_Cass.fasta -g Dp_mito_Cass.gff -v Dp_mito_SNP-RNA.vcf --module --rna --pep -o Dp_mito

With custom frequency and quality threshold
>> extractMitoSeq.py -f Dp_mito_Cass.fasta -g Dp_mito_Cass.gff -v Dp_mito_SNP-RNA.vcf -snpfreq X.X -snpqual Q --module --rna --pep  -o Dp_mito    

 EXPORT ONLY EDITED PROTEINS 
>> extractMitoSeq.py -f Dp_mito_Cass.fasta -g Dp_mito_Cass.gff -v Dp_mito_SNP-RNA.vcf --pep -o Dp_mito

 EXPORT NEW CASSETTE REFERENCE WITH GIVEN SNP ON DNA
>> extractMitoSeq.py -f Dp_mito_Cass.fasta -g Dp_mito_Cass.gff -v Dp_mito_SNP-DNA.vcf --cassette -o Dp_mito
'''
''' NOTE on GFF
For all modules belonging to the SAME gene, NAME are THE SAME, ex: Name=Da_atp6
For all modules belonging to the SAME gene, ID are uniques, ex: ID=Da_atp6-m2 
Modules should be listed in the correct RNA order (e.g. Da_atp6-m1, Da_atp6-m2, .... )
Poly-u should always be listed AFTER the module which is polyuridilated even if it is on minus strand

Example:
Re_y5-m1        Geneious        chromosome      1       883     .       +       .       ID=Re_y5-m1_k;class=A1
Re_y5-m1        Geneious        misc_feature    398     631     .       -       .       ID=Re_y5-m1_cass
Re_y5-m2        Geneious        chromosome      1       778     .       +       .       ID=Re_y5-m2_k;class=A3
Re_y5-m2        Geneious        misc_feature    315     484     .       +       .       ID=Re_y5-m2_cass
Re_cob-m5_y5-m3      Geneious        misc_feature    235     540     .       -       .       ID=Re_cob-m5_Re_y5-m3_cass
Re_cob-m5_y5-m3      Geneious        chromosome      1       783     .       +       .       ID=Re_cob-m5_Re_y5-m3_k;class=A3

Re_y5-m1        Geneious        mRNA    436     629     .       -       .       Name=Re_y5;ID=Re_y5-m1
Re_y5-m1        Geneious        poly-u  418     435     .       -       .       Name=Re_y5;ID=Re_y5-m1-pU18
Re_y5-m2        Geneious        mRNA    351     459     .       +       .       Name=Re_y5;ID=Re_y5-m2
Re_cob-m5_Re_y5-m3      Geneious        mRNA    471     526     .       +       .       Name=Re_y5;ID=Re_y5-m3
Re_cob-m5_Re_y5-m3      Geneious        poly-u  527     528     .       +       .       Name=Re_y5;ID=Re_y5-m3-pU2
'''

def parseoptions( ):
        """ Docstring 
            .... """

	print " ".join( sys.argv )

        parser = argparse.ArgumentParser( formatter_class=argparse.RawDescriptionHelpFormatter, description="Read a fasta and a gff file and export module, transripts and protein sequences. \nWhen a VCF file is provided, sequences are updated with SNPs above --snpfreq and --snpqual threshold. SNPs can be on RNA (editing) or on DNA.\nNOTE on GFF\nAll modules belonging to the SAME gene have THE SAME NAME, ex: Name=Da_atp6\nAll modules belonging to the SAME gene have UNIQUE ID, ex: ID=Da_atp6_m2 \nModules should be listed in the correct RNA order (e.g. Da_atp6_m1, Da_atp6_m2, .... )\nPoly-u should always be noted on the + strand even if module is on the '-' and AFTER the module" )
        parser.add_argument( '-f',  '--fasta',   help="Chromosomes/Cassettes reference fasta",   required=True )
        parser.add_argument( '-g',  '--gff',   help="gff file for reference including gene and rna",   required=True )
        parser.add_argument( '-v',  '--vcf',   help="vcf file for SNP/RNA editing on reference.",   required=False )        
        parser.add_argument( '-o',  '--output',  help="Prefix for output. Output name will be in format: PREFIX + _ + module|rna|pep + _ + DATE + .fasta",   required=False  )
        
        parser.add_argument( '--cassette', help="Export cassettes", action='store_true', default=False)
        parser.add_argument( '--module', help="Export modules", action='store_true', default=False)
        parser.add_argument( '--rna', help="Export RNA", action='store_true', default=False)
        parser.add_argument( '--pep', help="Export proteins", action='store_true', default=False)
        
        #parser.add_argument( '-s',  '--snp',  default='RNA', help="Are SNPs on RNA (RNA editing, default) or DNA. For SNP on DNA, a new version of the chromosomes is provided. Values ['RNA' (default),'DNA']",   required=False )
        parser.add_argument( '-t',  '--snpfreqmin',    default=0.5, type=float, help="SNP strictly above this frequency threshold will be incorporated.")
        parser.add_argument( '-T',  '--snpfreqmax',    default=1.0, type=float, help="SNP strictly below this frequency threshold will be incorporated.")
        parser.add_argument( '-q',  '--snpqual',    default=1000, type=int, help="SNP strictly above this quality will be incorporated.")


        #parser.add_argument( '-b',  '--blast',  default=0, type=int,   help="bla bla",   required=True|False )
        # Noter que les tirets dans les noms d'arguments sont transformes en souligne
        global ARGS             # Modify global variable ARGS
        ARGS = parser.parse_args()
        #globals().update(vars(args))        # Makes variables be seen globally

PREFIX 		= ""
LGFFNAME 		= [] # List of gff id in the same order as in the file
GFFMRNA		= 'mrna' 	# GFF feature for mRNA in lower case
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
                        # ARGS.output to access "output" argument value
        # Nothing to do
        if not ARGS.module and not ARGS.cassette and not ARGS.rna and not ARGS.pep :
            print "\nEasy peasy, I have nothing to do ! Please give me some work (--cassette, --module, --rna, --pep)\n"
            sys.exit(0)
    
	# PREFIX for output file
	global PREFIX
	if not ARGS.output :
		# splittext removes the last extension (even if more than one '.' in the file name
    		PREFIX = os.path.splitext(ARGS.fasta)[0]
        else :
                PREFIX =  ARGS.output
		
    	# Read GFF ; key = feature id, value = gff
    	dgff    = readgff( ARGS.gff )

    	# Read fasta ; key = fasta id, value = fasta
    	dfasta  = readFasta( ARGS.fasta )
	
	# Read VCF
	lvcf 	= None
	if ARGS.vcf :
		lvcf	= readVCF( ARGS.vcf, ARGS.snpqual, ARGS.snpfreqmin, ARGS.snpfreqmax )
	
	# Extract modules
	if ARGS.module  :
		extractModules(dfasta,dgff,lvcf)
	
	# Update K (with SNP) => change only fasta
	if ARGS.cassette :
		updateCassettes(dfasta, dgff, lvcf)
	
	# Extract RNA and pep
	if ARGS.rna or ARGS.pep :
		extractRNAandPep(dfasta, dgff, lvcf)
	
	dt = time()-t1
	print "END " + str( datetime.now() ) + " ---- time(s) = " + str(dt)

def extractRNAandPep(dfasta,dgff,lvcf=None) :

	# If output RNA
	if ARGS.rna :
		if not lvcf is None :
			fnamerna	= filename( "RNA-snp" ) 
		else :
			fnamerna	= filename( "RNA" ) 
		foutrnafasta            = open( fnamerna + ".fasta", "w") 
		foutrnagff 		= open( fnamerna + ".gff", "w")
		print "\n#[OUT] RNA files\n\t%s\n\t%s "%( fnamerna + ".fasta", fnamerna + ".gff" )
                
                # foutrnafasta.write( version() )
                loginfo( fnamerna + ".fasta" )
                foutrnagff.write( version() )
                loginfo( fnamerna + ".gff" )

	# If output protein
	if ARGS.pep :
		if not lvcf is None :
			fnamepep	= filename( "pep-snp" ) 
		else :
			fnamepep	= filename( "pep" ) 			
		foutpepfasta 	= open( fnamepep + ".fasta", "w") 
		print "\n#[OUT] Protein file\n\t%s "%( fnamepep + ".fasta", )	

                #foutpepfasta.write( version() )
                loginfo( foutpepfasta )

		if not lvcf is None :
			print "\t!!! Exported sequence updated with SNP"
	
	# For all gff entries
	for gffname in LGFFNAME :
		if not gffname in dgff :
			continue

		lgff 	= dgff[ gffname ]
                # Comment line with gene  name
                for g in lgff :
                    if g.feature.lower() == GFFRRNA or g.feature.lower() == GFFMRNA :
                        foutrnagff.write("# " + gffname + "\n" )
                        break;

		seqRNA 	= ""
		posRNA	= 0 		# Last position of RNA
		i 	= 0		# Rank of exon
		isrRNA	= False 	# Is it a ribosomal RNA => Do not translate
		ismRNA	= False
		for g in lgff :
			if g.feature.lower() == GFFRRNA :
				isrRNA = True
			if g.feature.lower() == GFFMRNA :
				ismRNA = True

			lvcf_filt 	= []
				
			if g.feature.lower() in [GFFMRNA, GFFRRNA] :
				if not g.contig in dfasta :
					print "\t!!!No fasta sequence for chromosome %s. The fasta sequence and gff for RNA and/or Protein %s will probably be wrong"%(g.contig,gffname)
					continue	

				# Sequence of contig (with SNP, eventually)			
				seqcontig 	= dfasta[ g.contig ].seq
				lvcf_filt	= listOfSNPsForSeq( seqcontig, g, lvcf )
				seqcontig	= updateSeqWithSNPs( seqcontig, lvcf_filt )
				# seqcontig	= updateSeqWithSNPs( seqcontig, g, lvcf )
                                #print g.name + " " + g.id + " SNP  nb %i "%(len(lvcf_filt),)

				# Sequence of feature
				seqfeature      = seqcontig[g.start-1:g.end]
				if g.strand == '-' :
					seqfeature 	= revcomp( seqfeature )
				seqRNA 			+= seqfeature

			if g.feature.lower() == GFFPOLYU :
				seqRNA 		+= (g.end-g.start+1) * 'T'
				
			# Add GFF 
			if ARGS.rna and (g.feature.lower() in [GFFMRNA, GFFRRNA, GFFPOLYU] ) :
				# Rank of exon in RNA
				i 		+= 1 	
				# GFF ID attribute
				if "id" in g.dattributes :
					gffid = g.dattributes["id"]
				else :
					gffid = gffname + '_%i'%(i,)
				# GFF Feature field
				feature = g.feature
				if g.feature.lower() == GFFMRNA :
					feature = 'exon'
				
				foutrnagff.write("%s\textractMitoSeq\t%s\t%i\t%i\t.\t%s\t0\tID=%s\n"%(gffname,feature,posRNA+1,len(seqRNA),'+',gffid))
				# SNP
                                shift = posRNA + 1 - g.start
                                if g.strand == '-' :
                                    shift = posRNA + 1 + g.end
				foutrnagff.write( gffWithSNPs( lvcf_filt, gffname, gffname, shift, g.strand ) )

				# Update last position of RNA
				posRNA 		= len(seqRNA) 
		

                # If mRNA is not a multiple of 3, complete with A of poly-A
		#if ismRNA :
		#	remainder	= len(seqRNA)%3
	        #	pA		= 0
		#	if not remainder == 0 :
		#		pA = 3 - remainder
		#		print "\t%s - Added %i 'A' at the end of RNA sequence"%( gffname, pA )
		#		if ARGS.rna :
		#			foutrnagff.write("%s\textractMitoSeq\tpoly-A\t%i\t%i\t.\t+\t0\tNote=%i_A_added_for_translation\n"%(gffname,len(seqRNA)+1,len(seqRNA)+1,pA))
		#		seqRNA 	+= pA * 'A'
                # If no STOP on mRNA, complete with up to 3 A of poly-A (sqc multiple of 3)
                if ismRNA :
                        # Poly-A gff line
                        polyAgff        = "%s\textractMitoSeq\tpoly-A\t%i\t%i\t.\t+\t0\t"%(gffname,len(seqRNA)+1,len(seqRNA)+1)
                        notepolyAgff    = ""

                        # List of  codon
                        lcodon  = []
                        for i in range( 0, len(seqRNA), 3 ):
                            lcodon.append( seqRNA[ i:i+3 ] ) 
                        # Does list of codon contains a stop
                        isStop          = False
                        for stop in STOPCODON4 :
                            if stop in lcodon :
                                isStop = True
                        # No STOP codon found, add A from poly-A until multiple of 3
                        if not isStop :
                            lastcodon   = lcodon[-1]
                            #remainder  = len(seqRNA)%3
                            pA      = 3 - len(lastcodon)
                            if pA >  0 :
                                lastcodon   += pA * 'A'
                                seqRNA      += pA * 'A'
                                # Adding 'A' has created a STOP codon
                                print "\t%s - Added %i 'A' at the end of RNA sequence for translation"%( gffname, pA )
                                if ARGS.rna :
                                    notepolyAgff    += "%i_A_added_for_translation "%(pA,)
                                if lastcodon in STOPCODON4 :
                                    isStop  = True
                        # Still no stop codon for this RNA
                        if not isStop :
                            print "\t%s - No STOP codon"%( gffname, )
                            if ARGS.rna : 
                                notepolyAgff    += "No STOP codon"
                            
                        # Add poly-A line in GFF
                        if ARGS.rna and len( notepolyAgff ) > 0  :
                            foutrnagff.write( polyAgff + "Note=" + notepolyAgff + "\n" )
                        if ARGS.rna and len( notepolyAgff ) == 0 :
                            foutrnagff.write( polyAgff  + "\n" ) 



		# Add fasta of RNA	
		if ARGS.rna and (ismRNA or isrRNA) :
			foutrnafasta.write(">%s \n%s\n"%(gffname,seqRNA))

		# Add fasta of PEP	
		if ARGS.pep and ismRNA and not isrRNA :
			# Test start and stop codon
			codonstart = seqRNA[:3]
			if not codonstart in INITCODON4 :
				print "\t%s - RNA sequence does not begin with a regular start codon (%s) "%(gffname,codonstart)
			#codonstop  = seqRNA[-3:]
			#if not codonstop in STOPCODON4 :
			#	print "\t%s - RNA sequence does not end with a regular stop codon (%s) "%(gffname,codonstop)
			seqpep 	= translate( seqRNA )
			foutpepfasta.write(">%s \n%s\n"%(gffname.upper(),seqpep))

	if ARGS.rna :
		foutrnafasta.close()
		foutrnagff.close()
	if ARGS.pep :
		foutpepfasta.close()
		

def extractModules(dfasta,dgff,lvcf=None) :

	if not lvcf is None :
		fname		= filename( "module-snp" ) 
	else :
		fname		= filename( "module" ) 

	foutfasta 	= open( fname + ".fasta", "w") 
	foutgff 	= open( fname + ".gff", "w")

        #foutfasta.write( version() )
        loginfo( fname + ".fasta" ) 
        foutgff.write( version() )
        loginfo( fname + ".gff" ) 
	
	print "\n#[OUT] Module files\n\t%s\n\t%s "%( fname + ".fasta", fname + ".gff" )
	if not lvcf is None :
		print "\t!!! Exported sequence updated with SNP"	

	for gffname in LGFFNAME :
		if not gffname in dgff :
			continue
		lgff = dgff[ gffname ]
		i = 0
		for g in lgff :
			if g.feature.lower() in [GFFMRNA, GFFRRNA] :
				if not g.contig in dfasta :
					print "\t!!!No fasta sequence for chromosome %s"%(g.contig,)
					continue				
				i += 1
				seqcontig 	= dfasta[ g.contig ].seq
				if g.strand == '-' :
					seqcontig = revcomp( seqcontig )
				lvcf_filt	= listOfSNPsForSeq( seqcontig, g, lvcf )
				seqcontig	= updateSeqWithSNPs( seqcontig, lvcf_filt )
				#seqcontig	= updateSeqWithSNPs( seqcontig, g, lvcf )
				seq 		= seqcontig[g.start-1:g.end]
				if "id" in g.dattributes :
					gffid = g.dattributes["id"]
				else :
					gffid = g.name + '_%i'%(i,)
				foutfasta.write(">%s \n%s\n"%(name,seq))
				foutgff.write("%s\textractMitoSeq\texon\t1\t%i\t.\t%s\t0\tID=%s\n"%(gffid,len(seq),'+',gffid))
				shift = 1 - g.start
                                foutgff.write( gffWithSNPs( lvcf_filt, gffid, gffid, shift, g.strand ) )
			
	foutfasta.close()
	foutgff.close()

	
# Update K (with SNP) => change only fasta
def updateCassettes(dfasta, dgff, lvcf) :

        if not lvcf is None :
            fname   = filename( "cass-snp" ) 
        else :
            fname   = filename( "cass" )    

	foutfasta	= open( fname  + ".fasta", "w" )
	print "\n#[OUT] New cassette file \n\t%s"%( fname + ".fasta", )
        #foutfasta.write( version() )
        loginfo(  fname  + ".fasta" ) 

        if not lvcf is None :
                print "\t!!! Exported sequence updated with SNP"    
        	

	for gffname in LGFFNAME :
		if not gffname in dgff :
			continue
		lgff = dgff[ gffname ]
		for g in lgff :
			if g.feature.lower() == GFFCHROM :
				if not g.contig in dfasta :
					print "\t!!!No fasta sequence for chromosome %s"%(g.contig,)
					continue
				seqcontig 	= dfasta[ g.contig ].seq
				lvcf_filt       = listOfSNPsForSeq( seqcontig, g, lvcf )
                                seqcontig	= updateSeqWithSNPs( seqcontig, lvcf_filt )
				foutfasta.write(">%s \n%s\n"%(g.contig,seqcontig))
	
	foutfasta.close()
	
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
		

def listOfSNPsForSeq( seq, gff, lvcf ) :
	lvcffilt = []
	if not lvcf is None :
		for v in lvcf :
			# If SNP on the contig and in the module
			if v.contig == gff.contig and v.pos >= gff.start and v.pos <= gff.end :
				#print "%s %i REF in VCF:%s ; REF in fasta: %s ==> ALT: %s"%(v.contig,v.pos,v.ref,seq[v.pos-1], v.altmax )
				if not v.ref == seq[v.pos-1] :
					print "WARNING: %s %i REF in VCF:%s ; REF in fasta: %s"%(v.contig,v.pos,v.ref,seq[v.pos-1] )
					print "WARNING: Reference base in VCF is different from base in fasta. Change it anyway"
				lvcffilt.append(v)
        return lvcffilt

def updateSeqWithSNPs( seq, lvcf ) :
	lseq 	= list(seq)
	if not lvcf is None :
		for v in lvcf :
			lseq[v.pos-1] = v.altmax
	return "".join(lseq)

# Strand is the strand of the feature bit SNP are reported on '+'
def gffWithSNPs( lvcf, contig, featureName, shift , featureStrand ) :
	gfflines = ""
        if featureStrand == '-' : 
            ltmp = reversed( lvcf )
            lvcf = ltmp
	for v in lvcf :
		snpposstart     = v.pos + shift
                snpposend       = snpposstart + len(v.altmax) - 1      
                if featureStrand == '-' :
                    snpposstart = shift - v.pos - len(v.altmax) + 1
		    snpposend	= shift - v.pos 
		snpref  = v.ref
                snpalt  = v.altmax
                if featureStrand == '-' :
                    snpref  = revcomp(v.ref)
                    snpalt  = revcomp(v.altmax)
                snpname = "%s_%i_%s>%s"%(featureName,snpposstart,snpref,snpalt)
                snpdesc	= "ref=%s;alt=%s;freq=%.2f;qual=%.2f"%(snpref,snpalt,v.altmaxfreq,v.qual)
		gfflines += "%s\textractMitoSeq\tSNP\t%i\t%i\t.\t+\t0\tID=%s;%s\n"%(contig,snpposstart,snpposend,snpname,snpdesc)
	return gfflines

def updateSeqWithSNPsOLD( seq, gff, lvcf ) :
	lseq 	= list(seq)
	if not lvcf is None :
		for v in lvcf :
			# If SNP on the contig and in the module
			if v.contig == gff.contig and v.pos >= gff.start and v.pos <= gff.end :
				#print "%s %i REF in VCF:%s ; REF in fasta: %s ==> ALT: %s"%(v.contig,v.pos,v.ref,seq[v.pos-1], v.altmax )
				if not v.ref == seq[v.pos-1] :
					print "WARNING: %s %i REF in VCF:%s ; REF in fasta: %s"%(v.contig,v.pos,v.ref,seq[v.pos-1] )
					print "WARNING: Reference base in VCF is different from base in fasta. Change it anyway"
				lseq[v.pos-1] = v.altmax
	return "".join(lseq)

def translate( seq ) :
	pos 	= 0 
	seq 	= seq.upper()
	seq 	= seq.replace('U','T') 
	lseq 	= list(seq)
	pep 	= ""

	while pos < len(lseq) :
		codon 	= "".join(lseq[pos:pos+3])
		if codon in GENETIC_CODE4 :
                        if pos == 1 and codon in INITCODON4 :
                            pep += 'M'
                        else :
			    pep += GENETIC_CODE4[ codon ]
                        if codon in STOPCODON4 :
                            return pep
		else :
			pep 	+= '?'
		pos	+= 3
	return pep


#######  GFF
def readgff( fgff ) :
	print "\n#[IN] Read GFF file %s"%( fgff )

	f       	= open( fgff, "r" )     
	dgff    	= {}
	global LGFFNAME
	
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
		if not g is None and len(g.name) > 0 :
			if not g.name in dgff :
				LGFFNAME.append( g.name )
				dgff[ g.name ] = []
			dgff[g.name].append( g )
			
	f.close()
	print "\t%i line(s) read"%( len(dgff), )

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
		latt    = self.attribute.split(';')
		for a in latt :
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


