def load_data(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    lines = filter(lambda l: l[0] != '%', lines)
    lines = [l[:-1].split(" ") for l in lines][1:]
    lines = [[l for l in line if l != ''] for line in lines]
    return lines

def convert_to_data_point(line):
    year = int(line[0])
    month = int(line[1])
    data_point = DataPoint(float(line[2]), float(line[3]))
    return year, month, data_point

class DataPoint:

    # 95% of samples lie in data +- uncertainty
    def __init__(self, data, uncertainty):
        super().__init__()
        self.data = data
        self.uncertainty = uncertainty

