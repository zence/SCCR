from sklearn import model_selection, svm, datasets, metrics, preprocessing
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.axes as axes

import pandas as pd

import lime
import lime.lime_tabular

import sys

total_her2_expr = pd.read_csv("../data/all_genes_TPM.tsv", sep="\t")

print(total_her2_expr)

expr_target = pd.DataFrame(data=total_her2_expr['her2_status_by_ihc'])
expr_target['her2_status_by_ihc'] = (expr_target['her2_status_by_ihc'] == 'Positive').astype(int)

print(expr_target)

expr_data = total_her2_expr.iloc[:, :-2]

print(expr_data)

clf = svm.SVC(kernel="linear", C=1, random_state=0)

predicted = model_selection.cross_val_predict(clf, expr_data, expr_target.values.ravel(), cv=10)

print(predicted)

print(metrics.accuracy_score(expr_target, predicted))
sys.stdout.flush()

clf = svm.SVC(kernel="linear", C=(10^8), random_state=531, probability=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(preprocessing.scale(expr_data.values), expr_target, test_size=0.33)

clf.fit(X_train, y_train.values.ravel())

explainer = lime.lime_tabular.LimeTabularExplainer(X_train, feature_names=list(expr_data),
                                                   class_names=['Negative', 'Positive'],
                                                   discretize_continuous=True)
for i in range(0, len(X_test)):
    exp = explainer.explain_instance(X_test[i],
                                clf.predict_proba)

    print(exp.as_list())
    print('Actual: ' + str(y_test.values[i]))
    print('Progress: ' + str(i + 1) + '/' + str(len(X_test)))
    sys.stdout.flush()

#kf = model_selection.KFold(n_splits=10)
#clf = svm.SVC(kernel="linear", C=1, random_state=0, probability=True)
#for train, test in kf.split(expr_data):
    
    #X_train, X_test = preprocessing.scale(expr_data.values[train]), preprocessing.scale(expr_data.values[test])
    #y_train, y_test = expr_target.values[train], expr_target.values[test]
    
    #clf.fit(X_train, y_train.ravel())
    
    #explainer = lime.lime_tabular.LimeTabularExplainer(X_train, feature_names=list(expr_data), 
                                                       #class_names=['Negative', 'Positive'],
                                                       #discretize_continuous=True)
    #exp = explainer.explain_instance(X_test[60], clf.predict_proba)
    
    #print(exp.as_list())
