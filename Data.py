import xlrd
import numpy as np


# Program extracting data from excel file
def get_data(loc):
    data = []

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        data.append(sheet.cell_value(i, 1))
    return data


def filter_data(data, threshold):
    threshold = np.float(threshold)
    return [item for item in data if np.greater(item[2], threshold)]


def sort_data(data):
    return sorted(data, key=lambda tup: float(tup[2]), reverse=False)


def print_data(data):
    for i in range(len(data)):
        print('Student ID 1 =', data[i][0], 'Student ID 2 =', data[i][1], 'Similarity =', data[i][2])
