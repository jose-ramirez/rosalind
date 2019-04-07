def hyp(filename):
	f = open(filename, 'r')
	for line in f.readlines():
		l = map(int, line.rstrip().lstrip().split(" "))
		a, b = l[0], l[1]
		print (a ** 2) + (b ** 2)

def strings(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	text = lines[0]
	ind = map(int, lines[1].rstrip().lstrip().split(" "))
	a, b = ind[0], ind[1] + 1
	c, d = ind[2], ind[3] + 1
	print '{0} {1}'.format(text[a : b], text[c : d])

def sums(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	nums = map(int, lines[0].rstrip().lstrip().split(" "))
	m, n = nums[0], nums[1]
	total = 0
	for r in range(m, n + 1):
		if(r % 2 == 1):
			total += r
	print total

def even_lines(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	for i in range(len(lines)):
		if(i % 2 == 1):
			print lines[i].rstrip()

def dicts(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	word_dict = {}
	for line in lines:
		words = line.rstrip().lstrip().split(" ")
		for word in words:
			if word not in word_dict:
				word_dict[word] = 1
			else:
				total = word_dict[word] + 1
				word_dict[word] = total
	for key in word_dict.keys():
		print '{0} {1}'.format(key, word_dict[key])

#hyp('rosalind_ini2.txt')
#strings('rosalind_ini3.txt')
#sums('rosalind_ini4.txt')
#even_lines('rosalind_ini5.txt')
#dicts('rosalind_ini6.txt')