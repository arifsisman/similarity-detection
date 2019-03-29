# Data Mining Similarity Analysis

## Required python packages
```sh
$ pip install xlrd numpy scipy sklearn
```

**xlrd** Read data from excel  
**numpy, scipy, sklearn** Required libraries for cosine similarity 

## Usage
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