#install matplotlib in your terminal first
#pip install matplotlib
import matplotlib.pyplot as plt

# Define a function to read and clean the DNA sequence from a FASTA file
def read_fasta(filename):
    sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(">"):  # skip header lines
                continue
            sequence += line.strip().upper()  # remove newline, make uppercase
    return sequence

# Read the file
content = read_fasta('FASTA file example.txt')
print("DNA Sequence:")
print(content)

#deploy funtion to read DNA sequences
def count_nucleotides(sequence):
    counts = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in sequence:
        if base in counts:
            counts[base] += 1
    return counts

print("\nThe total number of individual nucleotides are:")
#now call the funtion to analyse the nuceotides from the uploaded file
print(count_nucleotides(content))

#add a new funtion to calulate the perentage of Guanine and ytosine from the DNA sequence
#define new funtion called gc_content
def gc_content(sequence):
     g = sequence.count('G')
     c =sequence.count('C')
     gc_count = g + c
     total = sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')
     gc_percentage = (gc_count / total)*100
     return gc_percentage

print("\nPercentage of Guanine and Cytosine:")

print("GC Content: {:.2f}%".format(gc_content(content)))

#percentage of A and T nucleotides?
#at_percentage = 100 - gc_content(content)
#print("\nPercentage of Adenine and Thymine:")

#print("AT Content: {:.2f}%".format(at_percentage))

#the code above is not advised to find the percentage of A and T as they may include blanks and etc
#instead, create another function for A and T

def at_content(sequence):
    a = sequence.count('A')
    t = sequence.count('T')
    at_count = a + t
    total = sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')
    at_percentage = (at_count / total) * 100
    return at_percentage

print("\nPercentage of Adenine and Thymine:")
print("AT Content: {:.2f}%\n".format(at_content(content)))

#Do a validation of the DNA sequence to make sure only DNA nucleotides are persent
def validate_dna_seq(sequence):
    valid_bases = {'A','T','G','C'}
    invalid_bases = set()

    for bases in sequence:
        if bases not in valid_bases:
            invalid_bases.add(bases)
    
    if invalid_bases:
        print("⚠️ Invalid characters found in sequence:", invalid_bases)
        return False
    else:
        print("✅ Sequence is valid (A, T, G, C only).")
        return True

print("Validation of DNA Sequence: ")    
validate_dna_seq(content)


#Generate the reverse complement of the DNA Sequence
def reverse_complement_dna(sequence):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    reversed_dna_seq = sequence[::-1]
    reverse_comp = ""

    for base in reversed_dna_seq:
        if base in complement:
            reverse_comp += complement[base]
        else:
            reverse_comp += "N"
    return reverse_comp

reversed_complement_dna_seq = reverse_complement_dna(content)
print("\nReverse Cmplement Sequence: ")
print (reversed_complement_dna_seq)

#Create a visualization of the nucleotides

#get counts of each nucleotides from the count_nucleotides function
counts = count_nucleotides(content)

#assign the keys and values for plotting
bases = list(counts.keys())
values = list(counts.values())

#generate the visualization plot
plt.figure(figsize = (6,4))
bars = plt.bar(bases, values, color = ['green', 'blue', 'red', 'yellow'])

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height +0.3, str(height), ha='center', va='bottom', fontsize=10, fontweight = 'bold')

plt.title('Nucleotide Count')
plt.xlabel('Nucleotides')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
