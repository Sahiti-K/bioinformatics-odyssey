# 02_control_flow_dna_patterns.py
# Bioinformatics Odyssey – Control Flow, Loops, and Motif Search in DNA

def is_valid_dna(seq):
    # Check if the input contains only A, T, G, and C.
    return all(base in "ATGC" for base in seq)

def gc_content(seq):
    # Calculate the GC content (%) of the DNA sequence.
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def base_counts(seq):
    # Return the count of each nucleotide in the sequence.
    return {base: seq.count(base) for base in "ATGC"}

def transcribe(seq):
    # Transcribe DNA to RNA by replacing T with U.
    return seq.replace("T", "U")

def reverse_complement(seq):
    # Return the reverse complement of the DNA sequence.
    return seq.translate(str.maketrans("ATGC", "TACG"))[::-1]

def sequence_length_category(seq):
    #Categorize sequence based on length.
    length = len(seq)
    if length < 50:
        return "Short sequence"
    elif length < 200:
        return "Medium sequence"
    else:
        return "Long sequence"

def find_start_codons(seq):
    # Return the positions where the start codon ATG is found.
    return [i for i in range(len(seq) - 2) if seq[i:i+3] == "ATG"]

def scan_until_stop(seq):
    # Scan sequence in triplets until a stop codon is found.
    stop_codons = ["TAA", "TAG", "TGA"]
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in stop_codons:
            return f"Stop codon {codon} found at position {i}"
    return "No stop codon found in reading frame"

def find_motif(seq, motif):
    # Return a list of positions (1-based) where the motif occurs.
    return [i + 1 for i in range(len(seq) - len(motif) + 1) if seq[i:i+len(motif)] == motif]

# --- Interactive Input Block ---
# Get user input
seq = input("Enter a DNA sequence: ").upper()

# --- Sample test run ---
if __name__ == "__main__":
    seq = "ATGCGTAAGTAAATGC"
    
    if is_valid_dna(seq):
        print("Valid DNA sequence")
        print("GC Content:", f"{gc_content(seq):.2f}%")
        print("Base Counts:", base_counts(seq))
        print("Reverse Complement:", reverse_complement(seq))
        print("Transcription:", transcribe(seq))
        print("Length:", len(seq))
        print("Length Category:", sequence_length_category(seq))
        print("Start Codon Positions:", find_start_codons(seq))
        print("Stop Scan:", scan_until_stop(seq))
        print("Motif 'TAA' at:", find_motif(seq, "TAA"))
    else:
        print("Invalid DNA sequence")
