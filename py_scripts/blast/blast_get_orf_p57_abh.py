#!/usr/bin/env python3
from Bio import SeqIO
from Bio.Blast import NCBIXML

#homedir = '/Users/morpholino/Downloads/blasto/'
#homedir = '/Volumes/zoliq data/Downloads/blasto/'
homedir = '/Users/kika/ownCloud/blasto_comparative/genomes/'
blastdir = '/Users/kika/ownCloud/blasto_comparative/proteins/BLASTs/'
resultdir = '/Users/kika/ownCloud/blasto_comparative/proteins/'

genome = 'Btri' 
#Braa -> Braa_genome_final_corrected2_masked.fa
#Bfru, Oeli, Omod, Oobo, Ovol
#BLAST results only for Bfru, Braa, Btri

genomefile = homedir + genome + '_genome_final_masked.fa'
blastfile = blastdir + genome + '_genome.fwd_Bnon_proteins.blast.xml'
nt_outfile = resultdir + genome + '_proteins.fna'
aa_outfile = resultdir + genome + '_proteins.faa'
errorfile = resultdir + genome + '_proteins.errors.txt'


def _filter_overlaps(overlap):
    #https://www.geeksforgeeks.org/python-remove-redundant-substrings-from-strings-list/
    seqs = [str(x[2]) for x in overlap]
    seqs.sort(key = len)
    dump = [val for idx,val in enumerate(overlap) if any(str(val[2]) in x for x in seqs[idx + 1:])]
    if len(overlap) > 10:
        print(len(overlap), ">", len(dump))
    return dump


def _overlaps_to_ranges(overlap):
    if len(overlap) == 1:
        return f"{overlap[0][0]}-{overlap[0][1]}"
    else:
        printlist = []
        for item in overlap:
            printlist.append(f"{item[0]}-{item[1]}")
        return ",".join(printlist)

    
def _overlaps(moduleA, moduleB):
    startA = moduleA[0]
    endA = moduleA[1]
    startB = moduleB[0]
    endB = moduleB[1]
    if startA <= startB <= endA or startA <= endB <= endA:
        #overlaplow, overlaphigh = max(startA, startB), min(endA, endB)
        overlaplen = min(endA, endB) - max(startA, startB) + 1
        #print(moduleA, moduleB, overlaplow, overlaphigh, overlaplen)
        if overlaplen > 2:
            overlap = True
        else:
            overlap = False
    elif startB <= startA <= endB or startB <= endA <= endB:
        overlaplen = min(endA, endB) - max(startA, startB) + 1
        if overlaplen > 2:
            overlap = True
        else:
            overlap = False
    else:
        overlap = False
    return overlap


def translation(sequence):
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'B', 'TAG':'Z',
    'TGC':'C', 'TGT':'C', 'TGA':'J', 'TGG':'W'}
    cut_seq = []
    for i in range(0,len(sequence)-2,3):
        cut_seq.append(sequence[i:i+3])
    aa = []
    for codon in cut_seq:
        if 'N' in codon:
            aa.append('X')
        else:
            aa.append(gencode[codon])
    return ''.join(aa)


def blast_parser(blast_records):
    result = {}
    errors = set()
    for record in blast_records:
        try:
            for i,best in enumerate(record.alignments):
                #best = record.alignments[0]
                min_sstart = False
                max_send = False
                min_qstart = False
                max_qend = False
                frame = best.hsps[0].frame[1]
                evalue = best.hsps[0].expect
                if evalue > 0.01:
                    err_out.write('{}:\tevalue too high\n'.format(record.query.split(' ')[0]))
                else:
                    for hsp in best.hsps:
                        if frame == hsp.frame[1]:
                            if not min_qstart:
                                min_qstart = hsp.query_start
                                if frame in [1, 2, 3]:
                                    min_sstart = best.hsps[0].sbjct_start
                                else:
                                    min_sstart = best.hsps[0].sbjct_end
                            if not max_qend:
                                max_qend = hsp.query_end
                                if frame in [1, 2, 3]:
                                    max_send = best.hsps[0].sbjct_end
                                else:
                                    max_send = best.hsps[0].sbjct_start
                                    
                            #in repetitive regions, HSPs might actually be reshuffled
                            #first check that that the position of HSPs corresponds to order in query
                            if frame in [1, 2, 3]:
                                if min_qstart > hsp.query_start:
                                    if min_sstart > hsp.sbjct_start:
                                        min_sstart = hsp.sbjct_start
                                        min_qstart = hsp.query_start
                                if max_qend < hsp.query_end:
                                    if max_send < hsp.sbjct_end:
                                        max_qend = hsp.query_end
                                        max_send = hsp.sbjct_end
                            else:
                                if min_qstart > hsp.query_start:
                                    if min_sstart < hsp.sbjct_end:
                                        min_sstart = hsp.sbjct_end
                                        min_qstart = hsp.query_start
                                if max_qend < hsp.query_end:
                                    if max_send > hsp.sbjct_start:
                                        max_send = hsp.sbjct_start
                                        max_qend = hsp.query_end
                        else:
                            errors.add(record.query.split(' ')[0])
                            if frame in [1, 2, 3]:
                                min_sstart = best.hsps[0].sbjct_start
                                max_send = best.hsps[0].sbjct_end
                            else:
                                min_sstart = best.hsps[0].sbjct_end
                                max_send = best.hsps[0].sbjct_start
                    if frame in [1, 2, 3]:
                        result["{}__{}__{}".format(record.query.split(' ')[0],evalue,i)] = [min_sstart, max_send, frame, best.hit_id,
                        record.query_length, min_qstart, max_qend]
                    else:
                        result["{}__{}__{}".format(record.query.split(' ')[0],evalue,i)] = [max_send, min_sstart, frame, best.hit_id, 
                        record.query_length, min_qstart, max_qend]
        except:
            err_out.write('{}:\tno hit found\n'.format(record.query.split(' ')[0]))
    #errors = set(errors)
    #for i in errors:
    #    err_out.write('{}:\thsps frames do not correspond\n'.format(i))
    return result


print(f"Dataset: {genome}")
print("reading BLAST results...")
with open(blastfile) as result_handle,\
     open(errorfile, 'w') as err_out:
    blast_records = NCBIXML.parse(result_handle)
    blast_dict = blast_parser(blast_records)
    #print(blast_dict)


print("processing BLAST hits...")
with open(errorfile, 'a') as err_out:
    #err_out.write("hit\tmin_sstart<=>max_send, frame, best.hit_id, record.query_length, min_qstart, max_qend")
    contig_d = {seq.name: seq for seq in SeqIO.parse(genomefile, 'fasta')}

    # contains all sequences and the id of the "best query" in seqname
    seq_d = {}

    for key, value in blast_dict.items():
        #err_out.write(f"{key}\t{value}\n")
        try:
            contig = contig_d[value[3]] #all blast hits are in the genome so should not throw an error
        except KeyError:
            print("Invalid contig number! Skipping", value[3])
            continue
        frame = value[2]
        ref_name = key.split("__")[0]
        ref_evalue = float(key.split("__")[1])
        ref_length = value[4]
        ref_start = value[5]-1
        ref_end = value[6]
        ref_dif = ref_length - ref_end
        contig.seq = contig.seq.upper()
        if frame in [1, 2, 3]:
            #print(contig.name + '_____forward')
            seq_start = value[0]-1
            seq_end = value[1]
            if ref_start == 1:
                if translation(contig.seq[seq_start:seq_start+3]) == 'M':
                    seq_start = seq_start
                else:
                    while translation(contig.seq[seq_start:seq_start+3]) != 'M':
                        if seq_start > 2:
                            seq_start = seq_start - 3
                        else:
                            seq_start = seq_start
                            break
                    else:
                        seq_start = seq_start
            else:
                if seq_start > 3*ref_start: 
                    seq_start = seq_start - 3*ref_start
                else:
                    if frame == 1:
                        seq_start = 0
                    elif frame == 2:
                        seq_start = 1
                    elif frame == 3:
                        seq_start = 2
                while translation(contig.seq[seq_start:seq_start+3]) != 'M':
                    if seq_start > 2:
                        seq_start = seq_start - 3
                    else:
                        seq_start = seq_start
                        break
                else:
                    seq_start = seq_start
            if ref_end == ref_length:
                if translation(contig.seq[seq_end-3:seq_end]) == 'B':
                    seq_end = seq_end
                else:
                    while translation(contig.seq[seq_end-3:seq_end]) != 'B':
                        if seq_end < len(contig.seq) - 3:
                            seq_end = seq_end + 3
                        else:
                            seq_end = seq_end
                            break
                    else:
                        seq_end = seq_end
            else:
                if seq_end + 3*ref_dif < len(contig.seq) - 3:
                    seq_end = seq_end + 3*ref_dif
                    while translation(contig.seq[seq_end-3:seq_end]) != 'B':
                        if seq_end < len(contig.seq) - 3:
                            seq_end = seq_end + 3
                        else:
                            seq_end = seq_end
                            break
                    else:
                        seq_end = seq_end
                else:
                    seq_end = len(contig.seq)
            nucleotides = contig.seq[seq_start:seq_end]
            if translation(nucleotides[-3:]) == 'B':
                protein = translation(nucleotides[:-3]).replace('B', 'E').replace('Z', 'E').replace('J', 'W') + '*'
            else:
                protein = translation(nucleotides).replace('B', 'E').replace('Z', 'E').replace('J', 'W')

            if seq_start > seq_end:
                print("seq_start higher than seq_end, frame", frame, value[0], value[1])
            if len(nucleotides) < 1:
                print("No fw sequence extracted", len(contig.seq), seq_start, seq_end)
                err_out.write(f"No fw sequence extracted: {key}\n")
                continue

            if nucleotides not in seq_d:
                seq_d[nucleotides] = {"contig": contig.name, "strand": "+", "evalue": ref_evalue, "seq_start": seq_start, "seq_end": seq_end, "ref_name": ref_name, "protein": protein}
            elif ref_evalue < seq_d[nucleotides]["evalue"]:
                if seq_d[nucleotides]["contig"] != contig.name:
                    print("Warning, identical sequences on multiple contigs? Only the first is saved!", contig.name, "<=>", seq_d[nucleotides]["contig"])
                    #while seq_d.get(nucleotides, {"contig": contig.name})["contig"] != contig.name:
                    while nucleotides in seq_d and seq_d[nucleotides]["contig"] != contig.name:
                        #print("Warning, identical sequences on multiple contigs? Only the first is saved!", contig.name, "<=>", seq_d.get(nucleotides, {"contig": "NA"})["contig"])
                        print(nucleotides[-21:])
                        nucleotides += "NNN"
                        print(nucleotides[-21:])
                seq_d[nucleotides] = {"contig": contig.name, "strand": "+", "evalue": ref_evalue, "seq_start": seq_start, "seq_end": seq_end, "ref_name": ref_name, "protein": protein}             
        else:
            #print(contig.name + '_____reverse')
            reverse = contig.seq.reverse_complement()
            seq_start = len(reverse) - value[1]
            seq_end = len(reverse) - value[0] + 1
            if ref_start == 1:
                if translation(reverse[seq_start:seq_start+3]) == 'M':
                    seq_start = seq_start
                else:
                    while translation(reverse[seq_start:seq_start+3]) != 'M':
                        if seq_start > 2:
                            seq_start = seq_start - 3
                        else:
                            seq_start = seq_start
                            break
                    else:
                        seq_start = seq_start
            else:
                if seq_start > 3*ref_start:
                    seq_start = seq_start - 3*ref_start
                else:
                    if frame == 1:
                        seq_start = 0
                    elif frame == 2:
                        seq_start = 1
                    elif frame == 3:
                        seq_start = 2
                while translation(reverse[seq_start:seq_start+3]) != 'M':
                    if seq_start > 2:
                        seq_start = seq_start - 3
                    else:
                        seq_start = seq_start
                        break
                else:
                    seq_start = seq_start
            if ref_end == ref_length:
                if translation(reverse[seq_end-3:seq_end]) == 'B':
                    seq_end = seq_end
                else:
                    while translation(reverse[seq_end-3:seq_end]) != 'B':
                        if seq_end < len(reverse) - 3:
                            seq_end = seq_end + 3
                        else:
                            seq_end = seq_end
                            break
                    else:
                        seq_end = seq_end
            else:
                if seq_end + 3*ref_dif < len(reverse) - 3:
                    seq_end = seq_end + 3*ref_dif
                    while translation(reverse[seq_end-3:seq_end]) != 'B':
                        if seq_end < len(reverse) - 3:
                            seq_end = seq_end + 3
                        else:
                            seq_end = seq_end
                            break
                    else:
                        seq_end = seq_end
                else:
                    seq_end = len(reverse)
            nucleotides = reverse[seq_start:seq_end]
            if translation(nucleotides[-3:]) == 'B':
                protein = translation(nucleotides[:-3]).replace('B', 'E').replace('Z', 'E').replace('J', 'W') + '*'
            else:
                protein = translation(nucleotides).replace('B', 'E').replace('Z', 'E').replace('J', 'W')

            if seq_start > seq_end:
                print("seq_start higher than seq_end, frame", frame, value[1], value[0])
            if len(nucleotides) < 1:
                print("No rv sequence extracted", len(reverse), seq_start, seq_end)
                err_out.write(f"No rv sequence extracted: {key}\n")
                continue
                
            if nucleotides not in seq_d:
                seq_d[nucleotides] = {"contig": contig.name, "strand": "-", "evalue": ref_evalue, "seq_start": seq_start, "seq_end": seq_end, "ref_name": ref_name, "protein": protein}
            elif ref_evalue < seq_d[nucleotides]["evalue"]:
                if seq_d[nucleotides]["contig"] != contig.name:
                    print("Warning, identical sequences on multiple contigs? Only the first is saved!", contig.name, "<=>", seq_d[nucleotides]["contig"])
                    #while seq_d.get(nucleotides, {"contig": contig.name})["contig"] != contig.name:
                    print(nucleotides)
                    while nucleotides in seq_d and seq_d[nucleotides]["contig"] != contig.name:
                        #print("Warning, identical sequences on multiple contigs? Only the first is saved!", contig.name, "<=>", seq_d.get(nucleotides, {"contig": "NA"})["contig"])
                        print(nucleotides[-21:])
                        nucleotides += "NNN"
                        print(nucleotides[-21:])
                seq_d[nucleotides] = {"contig": contig.name, "strand": "-", "evalue": ref_evalue, "seq_start": seq_start, "seq_end": seq_end, "ref_name": ref_name, "protein": protein}

        #nt_out.write('>{}:{}-{} {}\n{}\n'.format(contig.name, seq_start, seq_end, ref_name, nucleotides))
        #aa_out.write('>{}:{}-{} {}\n{}\n'.format(contig.name, seq_start, seq_end, ref_name, protein))


print(len(seq_d), "primary hits")


print("comparing hit overlaps...")
with open(errorfile, 'a') as err_out:
#dictionary of scaffold: [(start, end, seq), ...]
    unique_loci = {}  #consists of tuples of (start, end, seq)
    banned = set()    #consists of tuples of (contig, start, end)

    for seq in seq_d:
        item = seq_d[seq]
        contig, seq_start, seq_end, ref_name, nucleotides, protein = item["contig"], item["seq_start"], item["seq_end"], item["ref_name"], seq, item["protein"]
        if contig in unique_loci:
            overlap = [x for x in unique_loci[contig] if _overlaps([seq_start, seq_end], [x[0], x[1]])]
            if overlap == []:
                unique_loci[contig].add((seq_start, seq_end, nucleotides))
            else:
                #determine if nucleotide is identical or subset of any already stored sequence: [x[2] for x in overlap] to get sequences
                #also within overlaps -> new sequence might be spanning two previously partial overlaps
                #https://www.geeksforgeeks.org/python-remove-redundant-substrings-from-strings-list/
                dump = _filter_overlaps(overlap + [(seq_start, seq_end, nucleotides)])
                for i in dump:
                    unique_loci[contig].remove(i) #consider e-value?
                    banned.add((contig, i[0], i[1]))
                if (seq_start, seq_end, nucleotides) not in dump:
                    unique_loci[contig].add((seq_start, seq_end, nucleotides))
                
        else:
            unique_loci[contig] = {(seq_start, seq_end, nucleotides)}


print("writing results...")
with open(nt_outfile, 'w') as nt_out,\
     open(aa_outfile, 'w') as aa_out,\
     open(errorfile, 'a') as err_out:
    #print(banned)
    c = 0
    for seq in seq_d:
        item = seq_d[seq]
        contig, strand, seq_start, seq_end, ref_name, nucleotides, protein = item["contig"], item["strand"], item["seq_start"], item["seq_end"], item["ref_name"], seq, item["protein"]
        if (contig, seq_start, seq_end) in banned:
            continue
        c += 1
        nt_out.write(f'>{contig}:{seq_start}-{seq_end}_{strand} {ref_name}\n{nucleotides}\n')
        aa_out.write(f'>{contig}:{seq_start}-{seq_end}_{strand} {ref_name}\n{protein}\n')

print(c, "sequences written. Done!")
