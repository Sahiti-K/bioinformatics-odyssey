# 01_python_basics_dna.py
# Bioinformatics Odyssey – Python Basics for Bioinformatics

# --- Variables and Data Types ---
gene_length = 1500              # int
gc_content = 56.2               # float
gene_name = "BRCA1"             # string
has_start_codon = True          # bool

print("Types:", type(gene_length), type(gc_content), type(gene_name), type(has_start_codon))

# --- DNA String Operations ---
dna = "ATGCGTAC"

print("DNA Sequence:", dna)
print("Length:", len(dna))
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))
print("GC Content:", (dna.count("G") + dna.count("C")) / len(dna) * 100)
print("First base:", dna[0])
print("Last 3 bases:", dna[-3:])
print("Codons (first 3):", dna[0:9])
print("RNA Transcript:", dna.replace("T", "U"))

# --- Lists and Indexing ---
bases = ['A', 'T', 'G', 'C']
print("All bases:", bases)
print("Second base:", bases[1])
for base in bases:
    print("Base:", base)

genes = ['BRCA1', 'TP53', 'EGFR']
genes.append('MYC')
print("Genes:", genes)

# --- Functions ---
def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def transcribe(seq):
    return seq.replace("T", "U")

def base_counts(seq):
    return {base: seq.count(base) for base in "ATGC"}

def has_start_codon(seq):
    return "ATG" in seq

def reverse_complement(seq):
    return seq.translate(str.maketrans("ATGC", "TACG"))[::-1]

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# --- Tests ---
print("GC%:", gc_content("GGGCCC"))
print("RNA:", transcribe("ATGC"))
print("Base counts:", base_counts("ATGCATGC"))
print("Start codon present?", has_start_codon("CGGATGCCGAT"))
print("Rev. Complement:", reverse_complement("ATGC"))
print("Hamming Distance:", hamming_distance("GAGCCT", "CATCGT"))

# Summary
# Practiced core Python data types and string operations using DNA examples.
# Functions defined for GC content, transcription, reverse complement, etc.
