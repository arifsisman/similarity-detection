import xlrd
import numpy as np

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


# Jaccard helper needs data and print option
def jaccard_helper(datas, print):
    arr_len = len(datas)
    ctr = 0
    result = [[0] * 3 for element in range(arr_len)]
    for i in range(0, arr_len):
        for j in range(i, arr_len):
            if i != j:
                ratio = get_jaccard(datas[i], datas[j])
                result.insert(ctr, (i, j, ratio))
                if print:
                    print("\n\njaccard ID:", ctr)
                    print("i =", i, datas[i])
                    print("j =", j, datas[j])
                    print(ratio)
                ctr += 1
    return result


# Cosine helper needs data and print option
def cosine_helper(datas, print):
    arr_len = len(datas)
    ctr = 0
    result = [[0] * 3 for element in range(arr_len)]
    for i in range(0, arr_len):
        for j in range(i, arr_len):
            if i != j:
                sparse = cosine_similarity(get_vectors(datas[i], datas[j]))
                # if np.greater(sparse[1][0], .5):
                result.insert(ctr, (i, j, sparse[1][0]))
                if print:
                    print("\n\ncosine ID:", ctr)
                    print("i =", i, datas[i])
                    print("j =", j, datas[j])
                    print(sparse[1][0])
                ctr += 1
    return result


# Program extracting data from excel file
def get_data():
    data = []
    loc = "hwdata2.xls"

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        data.append(sheet.cell_value(i, 1))
    return data


def filter_data(data, threshold):
    # np.greater(sparse[1][0], .5):
    return [item for item in data if np.greater(item[2], threshold)]


def sort_data(data):
    return sorted(data, key=lambda tup: float(tup[2]), reverse=False)


def print_data(data):
    for i in range(len(data)):
            print(data[i])


def main():
    data = cosine_helper(get_data(), 0)
    data = filter_data(data, .25)
    data = sort_data(data)

    print_data(data)

    # print(cosine_helper(get_data(), 0))
    # print(jaccard_helper(get_data(), 0))


if __name__ == '__main__':
    main()
