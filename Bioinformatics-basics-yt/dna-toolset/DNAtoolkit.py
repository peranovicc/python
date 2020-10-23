import collections

Nucleotides = ["A","C","G","T"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    # freq = {"A":0,"C":0,"G":0,"T":0}
    # for nuc in seq:
    #     freq[nuc] += 1
    # return freq
    return dict(collections.Counter(seq))




