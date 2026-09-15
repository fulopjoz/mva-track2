# Q7a sequence analysis artifacts (computed 2026-09-05, Ensembl REST GRCh38 e115+, maxentpy, RESCUE-ESE 238 hexamers (Wayback genes.mit.edu/burgelab/rescue-ese/ESE.txt), Zhang&Chasin 2004 PESE(2060)/PESS(1019) octamers + full 65536-octamer z table (Wayback cubweb))

## Region
BUB1B exon 17 = ENSE00001029409, chr15:40,209,635-40,209,775 (+), 141 bp, 141%3=0. Window chr15:40,207,635-40,211,775 (exon @ 2001-2141).
Neighbors: exon16 ENSE00001029391 134bp (intron16 = 865 bp), exon18 ENSE00001029401 101bp (intron17 = 335 bp).
DMD exons (ENST00000357033): ex45 ENSE00003988228 176bp, ex51 ENSE00003669071 233bp, ex53 ENSE00001258577 212bp.

## Motif density (per kb; meanZ = mean Zhang-Chasin octamer z over exon)
BUB1B ex16: ESE 141.8, PESE 74.6, PESS 22.4, meanZ +0.521, GC 45.5
BUB1B ex17: ESE 113.5, PESE 70.9, PESS 0.0,  meanZ +0.603, GC 43.3
BUB1B ex18: ESE 128.7, PESE 89.1, PESS 9.9,  meanZ -0.059, GC 35.6
DMD ex45:    ESE 153.4, PESE 11.4, PESS 5.7,  meanZ +0.546, GC 46.0
DMD ex51:    ESE 107.3, PESE 85.8, PESS 17.2, meanZ +0.662, GC 46.4
DMD ex53:    ESE 268.9, PESE 99.1, PESS 18.9, meanZ +0.859, GC 43.9

## Native junction MaxEntScan (5' score of 9-mer; 3' score of 23-mer)
BUB1B ex17: donor TAGGTAAGT 9.66 | acceptor CCTTTCCCTCCCACTGGCAGAAA 9.29
DMD ex45: donor GAGGTAGGG 7.81 | acceptor +11.32
DMD ex51: donor AAGGTATGA 9.11 | acceptor +3.73 (weak)
DMD ex53: donor AAGGTTAGT 8.54 | acceptor +8.55

## Cryptic-site scan (exon17 +/- 2 kb, 4141 nt)
Donors score>=5.0: 14 total (3.4/kb); ZERO inside exon 17 other than native; 3 >= native donor (10.67 @ intron16 -135; 9.79 @ intron16 -867; native 9.66).
Acceptors score>=4.0: 33 total (8.0/kb); ZERO inside exon 17 other than native; 1 >= native acceptor (10.02 @ intron17 +879 [exon17-intron-17 boundary window actually in intron 17]); note short introns.
Top intronic acceptors: +879 10.02, +455 8.99, +704 8.83 (all downstream intron(s)).

## PTC
c.2210T>G: exon offset 66 (0-based), codon TTA(65-67) -> TGA. PTC 75 nt from 17|18 junction, 6 downstream EJCs (wave2 NMD geometry confirmed).
Junction codon after skipping: GAA(codon715) -> GGT = E715G (verified from CDS ENST00000287598).

## ESE clusters inside exon 17 (RESCUE-ESE hit starts)
[0, 46, 47, 48, 91, 92, 93, 112-126 dense cluster (9 hits in 30-mer window at 108-138, 3' end next to donor)]
Top 30-mer ASO landing pad: exon pos 108-138 (~109-141): GCCTAAGTTGGAAATTGAGAAGGAAATTGA...  (9 ESE hexamers + adjacent donor overlap possible)

Exon17 transcript-strand sequence:
AAAACCCTACTCAGTCACCATGGTGTTCACAGTATCGCAGACAGCTACTGAAGTCCCTACCAGAGTTAAGTGCCTCTGCAGAGTTGTGTATAGAAGACAGACCAATGCCTAAGTTGGAAATTGAGAAGGAAATTGAATTAG
Intron16 3' end (last 60): CCATTTTAAGCATTAGGGTTTTTTTGGTGATATATTTTCACCTTTCCCTCCCACTGGCAG
Intron17 5' end (first 60): GTAAGTACCATTGAACTCATGTCCTCTGGTTCATGACAGTATACAAATAAGTGATTATTT
