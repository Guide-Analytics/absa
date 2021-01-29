# Binary Classifier for Author Verification

## Summary

A binary classifier was implemented using sklearn’s implementation of SVM classifier to differentiate between reliable and unreliable reviewers.

## Directory Structure

1) *Binary_Classification.ipynb* contains the code to train and create a binary classifier model.
2) *author_label_data.csv* contains the dataset for training and validation testing.
3) *Results.pdf* contain some analysis of the results of the classification model.

## How To Run?

#### Binary_Classification.ipynb
This notebook contains the code for testing different SVM models on the data. In all, 4 types of models were trained and compared:<br>
1) SVM with RBF Kernel on input data.<br>
2) SVM with Linear Kernel on input data.<br>
3) SVM with RBF Kernel on PCA modified data.<br>
4) SVM with Linear Kernel on PCA modified data.<br>

For each of these cases, model was trained for multiple values of Regularization Parameter (C) and prediction accuracies were compared on the test data.<br>
In case of generating the model for prediction, only sections *1)* and *6)* need to be executed which will create a *pickle* object titled *binary_classifier.pkl* in the present directory. This model can be used later to make predictions on new data.


#### Loading Saved Model
In order to load a saved model, execute the following code:<br>
```
import cPickle
with open('binary_classifier.pkl', 'rb') as fid:
    model_loaded = cPickle.load(fid)
```
Now, this model can be used to make predictions for data in following the format of *author_label_data.csv*.


## References
1) [SKLearn Documentation on SVM Classifier.](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)<br>
2) [Saving and Loading SKLearn Models.](https://stackoverflow.com/questions/10592605/save-classifier-to-disk-in-scikit-learn)<br>
3) [StackOverflow article on Regularization Parameter.](https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel)<br>
4) [Medium Article on Regularization Parameter.](https://medium.com/@pushkarmandot/what-is-the-significance-of-c-value-in-support-vector-machine-28224e852c5a)
5) [StatQuest's video on SVM.](https://www.youtube.com/watch?v=efR1C6CvhmE)



## Author

Rishabh Karwayun.
