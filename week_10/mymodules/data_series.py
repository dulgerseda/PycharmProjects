
"""Create a class named DataSeries that takes over a list (data series) and provides two methods:
get_features(dx) which returns a list with the positions of the first of two subsequent elements
that have an absolute nummerical distance (count data) equal or
above (>=) the given distance
dx. count_features() returns the number of features in a series of count data values.

Create a second class MyDataSeries that inherits from DataSeries.
This class overrides the function get_features and allows to set
a range of dx_min and dx_max (boundaries included) for feature detection"""

#%%

class DataSeries:
    def __init__(self, data):
        self.data = data

    def get_features(self, dx):
        features = []
        for i in range(len(self.data) - 1):
            if abs(self.data[i+1] - self.data[i]) >= dx:
                features.append(i)
        return features

    def count_features(self, dx):
        return len(self.get_features(dx))

data = DataSeries([2, 3, 10, 11, 15])
print(data.get_features(5))   # burada dx = 5 → fonksiyona gönderiyoruz
print(data.count_features(5))

# en büyük fark, 1. indexte, 10-3 = 7 5 den büyük farkı yakladık

#%%

class MyDataSeries(DataSeries):
    def __init__(self, data, dx_min, dx_max):
        super().__init__(data)     # DataSeries’in __init__’ini kullan
        self.dx_min = dx_min
        self.dx_max = dx_max

    def get_features(self):
        features = []
        for i in range(len(self.data) - 1):
            diff = abs(self.data[i+1] - self.data[i])
            if self.dx_min <= diff <= self.dx_max:
                features.append(i)
        return features

mds = MyDataSeries([2, 3, 10, 11, 15], 4, 8)
print(mds.get_features())
# [1, 3]
