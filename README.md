# 🧬 DNA Sequence Analyzer

A beginner-friendly bioinformatics project written in Python that:
- Reads a DNA sequence from a FASTA-style `.txt` file
- Validates the DNA sequence
- Counts nucleotide frequencies (A, T, G, C)
- Calculates GC and AT content
- Visualizes nucleotide counts using a bar chart

---

## 📖 Overview

This project was created as part of my journey to improve programming skills in Python and apply them to real-world bioinformatics tasks. The DNA Sequence Analyzer helps automate the process of reading and analyzing DNA sequences, a common task in genetic research. It includes essential bioinformatics operations such as validation, GC content calculation, and visualization — serving as a solid foundation for more advanced biological data processing.

---

## 🚀 Features

- ✅ Reads DNA sequences from a file
- ✅ Ignores FASTA headers (e.g., `>sequence`)
- ✅ Validates for only A, T, G, C characters
- ✅ Computes GC and AT content
- ✅ Plots nucleotide frequencies
- ✅ Generates the reverse complement struture of the DNA sequence


---

## 📂 Input Format

A `.txt` or `.fasta` file containing a DNA sequence:
```text
>Example DNA Sequence
ATGCGTACGTAGCTAGCTAGCTAGCTA
