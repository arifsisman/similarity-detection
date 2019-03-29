from Cosine import cosine_helper
from Data import get_data, filter_data, sort_data, print_data
from Jaccard import jaccard_helper
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--type", dest="type", default='cosine',
                        help="cosine or jaccard", metavar="TYPE")
    parser.add_argument("-f", "--file", dest="filename", default='data/hwdata1.xls',
                        help="input excel file", metavar="FILE")
    parser.add_argument("-th", "--threshold", dest="threshold", default=.25,
                        help="threshold value for similarity", metavar="THRESHOLD")
    parser.add_argument("-p", "--print", dest="printf", default=0,
                        help="print values explicitly", metavar="PRINT")

    # parse args
    args = parser.parse_args()
    sim_type = args.type
    file_path = args.filename
    threshold = float(args.threshold)
    print_id = args.printf

    # run program with args
    if sim_type == 'cosine':
        my_data = cosine_helper(get_data(file_path), print_id)
    elif sim_type == 'jaccard':
        my_data = jaccard_helper(get_data(file_path), print_id)
    else:
        sim_type = "cosine"  # default
        my_data = cosine_helper(get_data(file_path), print_id)

    # data post-processing
    my_data = filter_data(my_data, threshold)
    my_data = sort_data(my_data)
    print_data(my_data)

    # print args for inform
    print(args)


if __name__ == '__main__':
    main()
