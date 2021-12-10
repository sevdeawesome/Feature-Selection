# k fold with k = # of rows in dataset

import numpy
import math
import pandas
import time


# from numba import jit
print("Welcome to Sevi's feature detection")
print("Please enter the name of the text file you'd like to use")
name = input("ENTER: ")


# load data into a dataframe
dataframe = pandas.read_csv(name,header=None) 


# number of features
num_features = dataframe.iloc[0,1:].size
num_instances = dataframe.iloc[0:,0].size


# @jit
def cross_validation_accuracy(data, current_set, feature_to_add):
    this_set = current_set
    # this_set.append(feature_to_add)
    
    # start = time.time()



    for x in range(num_features):
        y = x + 1
        if y not in this_set and y != feature_to_add:
            # data[y].values[:] = 0
            data = data.drop(columns=[y])
    
    # print(data)
  
    num_correctly_classified = 0
    for i in range(num_instances):
        #label of curr instance
        label_object_to_classify = data.iloc[i, 0]
        #features of curr instance
        object_to_classify = data.iloc[i, 1:]
        
        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = 0

        for k in range(num_instances):
            if k != i:
                #find euclidian distance to object at k, k cannot be i
                object_to_compare = data.iloc[k,1:]
                # summation = 0
                # for a in range(object_to_classify.size):
                #     b = a+1
                #     summation += ((object_to_classify.at[b] - object_to_compare.at[b]) **2)
                # distance = math.sqrt(summation)
                distance = numpy.sqrt(numpy.sum([(a-b)*(a-b) for a, b in zip(object_to_classify, object_to_compare)])) 
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data.iloc[k,0]
                # print(" ask if " + str(i) + " is nearest neighbor w/ " + str(k))
        
        
        # print(data)
        # print("Object " + str(i)  + " is class " + str(label_object_to_classify) + " and its nearest neighbor is " + str(nearest_neighbor_location) + " which is in class " + str(nearest_neighbor_label))
        if(label_object_to_classify == nearest_neighbor_label): 
            num_correctly_classified += 1
    # milliseconds = time.time() - start
    # print(" time 3 " + str(milliseconds))
    accuracy = num_correctly_classified / num_instances
    return accuracy







def cross_validation_accuracy_remove(data, current_set, feature_to_remove):
    this_set = current_set
    # this_set.append(feature_to_remove)
    
    for x in range(num_features):
        y = x + 1
        if y not in this_set or y == feature_to_remove:
            data[y].values[:] = 0

    num_correctly_classified = 0
    for i in range(num_instances):
        #label of curr instance
        label_object_to_classify = data.iloc[i, 0]
        #features of curr instance
        object_to_classify = data.iloc[i, 1:]
        
        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = 0

        for k in range(num_instances):
            if k != i:
                #find euclidian distance to object at k, k cannot be i
                object_to_compare = data.iloc[k,1:]
                distance = numpy.sqrt(numpy.sum([(a-b)*(a-b) for a, b in zip(object_to_classify, object_to_compare)])) 
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data.iloc[k,0]
                # print(" ask if " + str(i) + " is nearest neighbor w/ " + str(k))
        
        
        # print(data)
        # print("Object " + str(i)  + " is class " + str(label_object_to_classify) + " and its nearest neighbor is " + str(nearest_neighbor_location) + " which is in class " + str(nearest_neighbor_label))
        if(label_object_to_classify == nearest_neighbor_label): 
            num_correctly_classified += 1
    accuracy = num_correctly_classified / num_instances
    return accuracy




  


# # test function
# print(cross_validation_accuracy(dataframe.copy(), [10,21], 1))
# print(validator(dataframe, [5], 8))

# validator(dataframe.copy(), [5], 8))
# print(cross_validation_accuracy_remove(dataframe.copy(), [1,2,3,10], 10))
# print(dataframe)
# print(cross_validation_accuracy(dataframe.copy(), [], 5))
# # print(dataframe)
# print(cross_validation_accuracy(dataframe.copy(), [], 4))
# # for i in range(num_features):
# #     print(i + 1)









    

