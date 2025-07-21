# 03_fasta_file_handling.py
# Bioinformatics Odyssey - File Handling & FASTA Parsing 

# PART 1: Create a raw DNA sequence file
def create_sample_dna_file():
    dna_seq = "ATGCGTACAGTAACGTAGCTGACTGATCGATCGATCGTAGCTAGCTAGT"
    with open("dna_sequence.txt", "w") as f:
        f.write(dna_seq)
    print("[✔] dna_sequence.txt created.")

# PART 2: Read and clean the DNA sequence
def clean_dna_sequence(input_file, output_file):
    with open(input_file, "r") as file:
        sequence = file.read().strip()
    with open(output_file, "w") as f:
        f.write(sequence.upper())
    print(f"[✔] Cleaned sequence written to '{output_file}'")

# PART 3: Read from a FASTA file
def read_fasta(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        header = lines[0].strip()
        sequence = "".join(line.strip() for line in lines[1:])
    return header, sequence

# PART 4: Write a sequence to FASTA format
# Write a cleaned and nicely formatted sequence into FASTA format - wrap the sequence every 60 characters (a common formatting rule)
def write_fasta(header, sequence, filename):
    with open(filename, "w") as file:
        file.write(header + "\n")
        for i in range(0, len(sequence), 60):
            file.write(sequence[i:i+60] + "\n")
    print(f"[✔] FASTA format saved to '{filename}'")

# Sample.Fasta
sample_fasta_content = """>sequence_1
ATGCGTACAGT
AACGTAGCTGA
TCGATCGATCG
TAGCTAGCTAGT
"""

with open("sample.fasta", "w") as f:
    f.write(sample_fasta_content)

print("sample.fasta created successfully!")

# Test runner
if __name__ == "__main__":
    # Step 1 & 2
    create_sample_dna_file()
    clean_dna_sequence("dna_sequence.txt", "cleaned_dna.txt")

    # Step 3
    fasta_header, fasta_seq = read_fasta("sample.fasta")
    print("\nFASTA Header:", fasta_header)
    print("FASTA Sequence:", fasta_seq)

    # Step 4
    write_fasta(fasta_header, fasta_seq, "output.fasta")

# Summary:
# Learned how to open, read, and write text and FASTA files.
# Used .strip(), .join(), and slicing to clean and format biological data.
