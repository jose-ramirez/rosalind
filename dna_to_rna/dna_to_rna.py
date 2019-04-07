def dna_to_rna(dna_string):
	print dna_string.replace("T", "U")

dna_to_rna(open('rosalind_rna.txt', 'r').readlines()[0])