import pymongo
import numpy
import matplotlib
import pylab as pl
client = pymongo.MongoClient('139.224.2.200',27017)
database = client['log']
collection = database['input_log']
x = []
x_avg = []


def make_x():
    for i in collection.find():
        x.append(i['sum'])


def avg_x():
    return float(sum(x)/len(x))

def make_avg_line():
    while len(x_avg) != len(x):
        x_avg.append(avg_x())


make_x()
make_avg_line()
pl.plot(x)
pl.plot(x_avg)
pl.show()