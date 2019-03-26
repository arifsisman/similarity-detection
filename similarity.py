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
def cosine_helper(datas, index):
    arr_len = len(datas)
    for i in range(arr_len - 1):
        for j in range(arr_len-1):
            print(datas[i])
            print(datas[j])
            print("\n\ncosine ID:", i*j, "\n", cosine_similarity(get_vectors(datas[i], datas[j])))


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

    cosine_helper(get_data(), 0)


if __name__ == '__main__':
    main()
