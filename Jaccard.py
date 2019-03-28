def get_jaccard(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


# Jaccard helper needs data and print option
def jaccard_helper(datas, printf):
    arr_len = len(datas)
    ctr = 0
    result = [[0] * 3 for element in range(arr_len)]
    for i in range(0, arr_len):
        for j in range(i, arr_len):
            if i != j:
                ratio = get_jaccard(datas[i], datas[j])
                result.insert(ctr, (i, j, ratio))
                if printf == '1':
                    print("\n\njaccard ID:", ctr)
                    print("i =", i, datas[i])
                    print("j =", j, datas[j])
                    print(ratio)
                ctr += 1
    return result
