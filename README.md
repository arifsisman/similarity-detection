## Data Mining Similarity Analysis with Jaccard and Cosine Similarity

### Required python packages
```sh
$ pip install xlrd numpy scipy sklearn
```

- **numpy, scipy, sklearn**  
Required libraries for cosine similarity 
- **xlrd**  
Read data from excel  

### Usage
Help Command:
```sh
$ python Similarity.py -h
```
Output:
```sh
usage: Similarity.py [-h] [-t TYPE] [-f FILE] [-th THRESHOLD] [-p PRINT]

optional arguments:
  -h, --help            show this help message and exit  
  -t TYPE, --type TYPE  cosine or jaccard  
  -f FILE, --file FILE  input excel file  
  -th THRESHOLD, --threshold THRESHOLD
                        threshold value for similarity  
  -p PRINT, --print PRINT
                        print values explicitly
```

### Example
```sh
$ python Similarity.py -f data/hwdata2.xls -th 0.5
```
```sh
Student ID 1 = 2 Student ID 2 = 3 Similarity = 0.5039526306789697
Student ID 1 = 2 Student ID 2 = 33 Similarity = 0.5203039116515846
Student ID 1 = 3 Student ID 2 = 36 Similarity = 0.5443310539518174
Student ID 1 = 3 Student ID 2 = 17 Similarity = 0.5773502691896258
Student ID 1 = 3 Student ID 2 = 8 Similarity = 0.6172133998483676
Student ID 1 = 8 Student ID 2 = 36 Similarity = 0.6299407883487119
Student ID 1 = 10 Student ID 2 = 11 Similarity = 0.6863547206421552
Student ID 1 = 9 Student ID 2 = 12 Similarity = 0.9683759683764526
Namespace(filename='data/hwdata2.xls', printf=0, threshold='0.5', type='cosine')
```