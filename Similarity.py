from Cosine import cosine_helper
from Data import get_data, filter_data, sort_data, print_data
from Jaccard import jaccard_helper
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--type", dest="type", default='cosine',
                        help="cosine or jaccard", metavar="TYPE")
    parser.add_argument("-f", "--file", dest="filename", default='hwdata1.xls',
                        help="input excel file", metavar="FILE")
    parser.add_argument("-th", "--threshold", dest="threshold", default=.25,
                        help="threshold value for similarity", metavar="THRESHOLD")
    parser.add_argument("-p", "--print", dest="printf", default=0,
                        help="print values explicitly", metavar="PRINT")

    # parse args
    args = parser.parse_args()
    type = args.type
    file_path = args.filename
    threshold = float(args.threshold)
    printf = args.printf

    # run program with args
    if type == 'cosine':
        data = cosine_helper(get_data(file_path), printf)
    elif type == 'jaccard':
        data = jaccard_helper(get_data(file_path), printf)
    else:
        type = "cosine"  # default
        data = cosine_helper(get_data(file_path), printf)

    # data post-processing
    data = filter_data(data, threshold)
    data = sort_data(data)
    print_data(data)

    # print args for inform
    print(args)


if __name__ == '__main__':
    main()
