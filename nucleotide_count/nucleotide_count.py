def nucleotide_count(dna_string):
	counts = {}
	for n in dna_string:
		if n not in counts:
			counts[n] = 1
		else:
			counts[n] += 1
	print '{0} {1} {2} {3}'.format(counts['A'], counts['C'], counts['G'], counts['T'])

nucleotide_count(open('rosalind_dna.txt', 'r').readlines()[0])