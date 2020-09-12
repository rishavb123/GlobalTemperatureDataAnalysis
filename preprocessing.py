import numpy as np

def load_data(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    lines = filter(lambda l: l[0] != '%', lines)
    lines = [l[:-1].split(" ") for l in lines][1:]
    lines = [[l for l in line if l != ''] for line in lines]

    new_lines = []
    for line in lines:
        if line == []: break
        new_lines.append(line)
    lines = new_lines

    data = None
    uncertainty = None

    base_year = 0

    for line in lines:
        year, month, data_point, uncertainty_point = convert_to_data_point(line)
        if base_year == 0:
            base_year = year
            data = np.zeros((2021 - base_year, 12))
            uncertainty = np.zeros_like(data)
        shifted_year = year - base_year
        shifted_month = month - 1
        data[shifted_year][shifted_month] = data_point
        uncertainty[shifted_year][shifted_month] = uncertainty_point

    return DataWrapper(data, uncertainty, base_year)

def convert_to_data_point(line):
    year = int(line[0])
    month = int(line[1])
    data_point = float(line[2])
    uncertainty_point = float(line[3])
    return year, month, data_point, uncertainty_point

class DataWrapper:

    def __init__(self, data, uncertainty, base_year):
        self.data = data
        self.uncertainty = uncertainty
        self.base_year = base_year

    def get_data_matrix(self):
        return self.data

    def get_uncertainty_matrix(self):
        return self.uncertainty

    def get(self, year, month):
        return self.data[year - self.base_year][month - 1]

    def get_uncertainty(self, year, month):
        return self.uncertainty[year - self.base_year][month - 1]
