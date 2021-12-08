import crossvalidation
import random


def accuracy():
    return(random.random())


def feature_search():

    current_set_of_features = []

    for i in range(1, crossvalidation.num_features + 1):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for k in range(1, crossvalidation.num_features + 1):
            # make sure to not consider already added features (i.e. do not add feature 1 if already in current_set_of_features)
            if k not in current_set_of_features:
                # print(current_set_of_features)
                # print("RUNNING CROSS VALIDATION W " + str(current_set_of_features) + " AND K " + str(k))
                acc = crossvalidation.cross_validation_accuracy(crossvalidation.dataframe.copy(), current_set_of_features, k)
                # acc = accuracy()
                print("--consider adding the " + str(k) + "th feature with accuracy: " + str(acc))
                # print(current_set_of_features)
                
                if acc > best_so_far_accuracy:
                    best_so_far_accuracy = acc
                    feature_to_add_at_this_level = k



        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) + " to current set WITH accuracy " + str(best_so_far_accuracy) )
        print(current_set_of_features)


def backwards_elimination():

    current_set_of_features = []
    for i in range(crossvalidation.num_features):
        current_set_of_features.append(i+1)

    print(current_set_of_features)


    for i in range(1, crossvalidation.num_features + 1):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_remove_at_this_level = []
        best_so_far_accuracy = 0
        for k in range(1, crossvalidation.num_features + 1):
            if k in current_set_of_features:
                acc = crossvalidation.cross_validation_accuracy_remove(crossvalidation.dataframe.copy(), current_set_of_features, k)
                # acc = accuracy()
                print("--consider removing the " + str(k) + "th feature with accuracy: " + str(acc))
                if acc > best_so_far_accuracy:
                    best_so_far_accuracy = acc
                    feature_to_remove_at_this_level = k
                    # print(k)
        current_set_of_features.remove(feature_to_remove_at_this_level)
        print("On level " + str(i) + " I removed feature " + str(feature_to_remove_at_this_level) + " to current set WITH accuracy " + str(best_so_far_accuracy) )
        print(current_set_of_features)
    

    

# feature_search()

backwards_elimination()
