def dna_complement(dna_string):
	f = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	print ''.join(map(lambda ch: f[ch], dna_string[::-1]))

dna_complement(open('rosalind_revc.txt', 'r').readlines()[0].rstrip())