# Rosalind Problems - DNA & RNA Basics

### Counting DNA Nucleotides

def base_counts(seq):
    counts = {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }
    return counts

# Accepts sequence as input to make the function reusable
seq = input('Enter your DNA sequence: ').upper() or "ATGCGTAC"
print("Base counts:", base_counts(seq))


### Transcribing DNA into RNA

def Transcribe_DNA_to_RNA(seq):
    return seq.replace("T", "U")

seq = input('Enter your DNA sequence: ').upper() or "ATGCGTAC"
print("RNA: ", Transcribe_DNA_to_RNA(seq))


### Complementing a Strand of DNA

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([complement[base] for base in reversed(dna)])

dna = input('Enter your DNA sequence: ').upper() or "ATGCGTAC"
print(reverse_complement(dna))


### Hamming Distance

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

s1 = input('Enter your DNA sequence: ').upper() or "ATGCGTAC"
s2 = input('Enter your DNA sequence: ').upper() or "ATTCGCAG"
print(hamming_distance(s1, s2))


### Finding a Motif in DNA

def find_motif_positions(dna, motif):
    positions = []
    for i in range(len(dna) - len(motif) + 1):
        if dna[i:i+len(motif)] == motif:
            positions.append(i + 1)  # 1-based index
    return positions

dna = input().upper()
motif = input().upper()
print(find_motif_positions(dna, motif))


"""
🔗 Rosalind Problems: DNA & RNA Basics

- DNA: Counting DNA Nucleotides — http://rosalind.info/problems/dna/
- RNA: Transcribing DNA into RNA — http://rosalind.info/problems/rna/
- REVC: Complementing a Strand — http://rosalind.info/problems/revc/
- HAMM: Hamming Distance — http://rosalind.info/problems/hamm/
- SUBS: Finding a Motif in DNA — http://rosalind.info/problems/subs/

"""
