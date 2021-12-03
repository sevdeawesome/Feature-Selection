# k fold with k = # of rows in dataset
import random
import numpy
import pandas 

# load data into a dataframe
data = pandas.read_fwf("small.txt",header=None) 
# number of features
num_features = data.iloc[0,1:].size
num_instances = data.iloc[0:,0].size

for i in range(num_instances):
    class_type = data.iloc[i, 0]
    print("THE " + str(i) + "th object is in class: " + str(class_type))

