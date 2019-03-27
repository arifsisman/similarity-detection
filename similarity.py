import xlrd

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_jaccard(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


# Jaccard helper

# Cosine helper
def cosine_helper(datas):
    arr_len = len(datas)
    ctr = 0
    result = [[]]
    for i in range(arr_len):
        for j in range(arr_len):
            if i != j & i <= j:
                sparse = cosine_similarity(get_vectors(datas[i], datas[j]))
                result.append((i, j, sparse[1][0]))
                print("\n\ncosine ID:", ctr, "\n")
                print("i =", i, datas[i])
                print("j =", j, datas[j])
                print(sparse[1][0])
                ctr += 1
    return result


# Program extracting first column
def get_data():
    data = []
    loc = "hwdata1.xls"

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        data.append(sheet.cell_value(i, 1))
    return data


def main():
    # x = get_jaccard("hello","hello world!")
    # y = get_cosine_sim("hello","hello world!")
    # print("jaccard similarity is", x)
    # print("cosine similarity is\n", y)

    cosine_helper(get_data())


if __name__ == '__main__':
    main()
