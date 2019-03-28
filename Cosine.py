from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


# Cosine helper needs data and print option
def cosine_helper(datas, printf):
    arr_len = len(datas)
    ctr = 0
    result = [[0] * 3 for element in range(arr_len)]
    for i in range(0, arr_len):
        for j in range(i, arr_len):
            if i != j:
                sparse = cosine_similarity(get_vectors(datas[i], datas[j]))
                result.insert(ctr, (i, j, sparse[1][0]))
                if printf == '1':
                    print("\n\ncosine ID:", ctr)
                    print("i =", i, datas[i])
                    print("j =", j, datas[j])
                    print(sparse[1][0])
                ctr += 1
    return result
