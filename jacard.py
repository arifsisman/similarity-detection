def main():
	print('hello')
	x = get_jaccard_sim("merhaba","merhaba dunya")
	print(x)


def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))