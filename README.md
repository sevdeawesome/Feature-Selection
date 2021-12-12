## The Problem
This is the second assignment in CS170: Introduction to Artificial Intelligence taught by Dr. Keogh at UC Riverside. In it, we are tasked with filtering out irrelevant features in an arbitrary dataset to find the features that can most accurately make predictions given the data. We use a simple one-out nearest neighbor classifier to measure the accuracy of varying combinations of features. Because there are N! Combinations of features(3*1064 in our case) using breadth first search to test every combination of features is not ideal. We used two simple search techniques to test only accurate features in this project, but they may have shortcomings in certain real world datasets. An example of this is if two features on their own yielded poor accuracy, but using the two together would yield high accuracy, luckily this is usually not the case. We were given 2 datasets, one large (2000 instances and 50 features) and one small (500 instances and 10 features). 

## Forward Selection
The first search method, forward selection, works by seeking out relevant features and adding them to the current subset of best features. In the beginning, it loops through every feature to find the one with the highest accuracy. Next, it attempts to add each other feature to the best subset and adds the one which improves the accuracy the most. It continues until it has found the most accurate subset of features. 


Figure 1. Here is an example of forward selection selecting the best feature after testing each addition to the subset. (4 features) 







Figure 2. The accuracy using forward selection on the small dataset. The peak is using features 5 and 8 yielding 95.8%. Feature 7 may also be a relevant feature, giving an accuracy of 95.2%. The last 4 subsets were omitted for space, but the trend is still visible, with accuracy reaching a maxima with 2 or 3 features, after that there are diminishing returns or just negative returns because the features are irrelevant to the class. 


Figure 3. When plotted, it can be seen that the features 5 and 8 clearly have some inter-feature dependence. As opposed to two irrelevant features that don't correlate with each other. 5 vs 8 is plotted on the left, feature 1 vs feature 2 plotted on the right. 






Figure 4. Features 5,8, and 7 also show feature dependence when plotted in 3-D. But 7 does not prove to be worth adding as it’s only loosely relevant to the classes. 






Figure 5. Forward selection on the large dataset (93). I think that features 10 and 21 produce the highest accuracy, at 97.8%. 46 may also be a relevant feature as [10,21,46] produces an accuracy of 95.5. 




## Backwards Elimination
Backward elimination is the opposite of forward selection. Instead of selecting the feature to add based on which improves the accuracy the most, backwards elimination begins with all the features and gradually removes those that are irrelevant by removing the feature that when removed - improves accuracy the most. Because of feature co-dependence, this doesn’t produce a tree that's exactly symmetrical and opposite to forward selection. A good way to improve your likelihood of finding the best features in a difficult dataset would be to take the subset that produced the maximum accuracy from both forward selection and backward elimination. 

With the small dataset, I find the same subset using backwards elimination. Features 5 and 8, giving an accuracy of 95.8%. 


Figure 6. Accuracy by level during backwards elimination (small dataset). The accuracy slowly trends upwards at the beginning. Where irrelevant features are harder to detect. Note: the 4th from last subset, [4,6,7,8] is different from the 4th subset in forward selection ([4,8,7,3]) This is because different features may be dependent on one another in unpredictable ways. An example of this is if features 4 and 5 alone proved to be irrelevant features, but when taken together in a nearest neighbor classifier, a pattern emerges. This is in fact what happened with our datasets.



Figure 7. Backwards elimination on the large dataset. Backwards elimination worked to my surprise on the large dataset. It would seem that because of the high number of features, backwards elimination may accidentally remove a relevant feature, but in testing it did not. 

## Runtime
I think my runtime could have been improved by removing the pandas library and data frames from my code. I continued to use them because runtime was not a horrible problem for me and using pandas made it easier for me to interpret the data. I also used CUDA to run my script on a Nvidia GTX 2080 Ti. It may have still been running on my cpu though because runtime was only reduced ~30%. 

The runtimes were as follows: to compute 1 feature subset on the small dataset took 13.3 seconds. Computing a feature subset on the large dataset took 208.4 seconds in a test run. This time can be reduced by only looking at a chunk of the data. By taking 1000 instances I got the same accuracy I did with 2000. 


## Code
I used python for my project. I used the time library to calculate runtime, matplotlib for the plots and numpy and pandas to import and manipulate the data. The code is on github at https://github.com/sevdeawesome/Feature-Selection

Here is the output of a sample run: https://pastebin.com/Ey6nGTPa

## Real world dataset
I ran my code on a database of Irises. There were 3 classes of iris and 4 features - sepal length, sepal width, petal length and petal width. I normalized all of these features and then ran it through forward search. The dataset can be found here: https://archive.ics.uci.edu/ml/datasets/Iris
Figure 8. Accuracy by subset on iris data. 

Feature 3 is petal length and feature 4 is petal width. The sepal length (mini green petals under the flower) didn’t seem to be relevant in predicting what type of iris each instance was. Plotting the data shows this as well:

Figure 9. Feature 3 vs Feature 4 on left, feature 1 vs feature 2 on right. This is for the iris data. Purple = Iris Setosa. Yellow = Iris Versicolor and Cyan is Iris Virginica. I apologize for the colors, matplotlib is set to theme the colors to my VSCode theme and it won’t let me change them. 

## Conclusion
In this project, we wrote a simple one-out nearest neighbor classifier to test the accuracy of various subsets of features in datasets. Then we ran two types of search across various subsets of features with 2 search methods. In this project I learned that after a certain point, even relevant features in data begin to have diminishing returns on accuracy, and too many features or irrelevant features can drastically harm the accuracy of a machine learning model. Finding irrelevant data and truncating data can save space and time. 


