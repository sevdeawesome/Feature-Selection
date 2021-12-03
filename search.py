import crossvalidation
from crossvalidation import random
from crossvalidation import num_features

def accuracy():
    return(random.random())


def feature_search():

    current_set_of_features = []

    for i in range(num_features):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for k in range(num_features):
            # make sure to not consider already added features (i.e. do not add feature 1 if already in current_set_of_features)
            if k not in current_set_of_features:
                acc = accuracy() 
                print("--consider adding the " + str(k) + "th feature with accuracy: " + str(acc))
                
                if acc > best_so_far_accuracy:
                    best_so_far_accuracy = acc
                    feature_to_add_at_this_level = k
        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) + " to current set" )


feature_search()


