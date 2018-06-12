from sklearn import model_selection, preprocessing
from rpy2.robjects import pandas2ri

import rpy2.robjects.packages as rpackages
import pandas as pd
import time

#clf = tree.DecisionTreeClassifier()
#iris = load_iris()

#clf = clf.fit(iris.data, iris.target)
#tree.export_graphviz(clf,
#        out_file='tree.dot')
pandas2ri.activate()
x = time.time()

total_her2_expr = pd.read_csv("../data/all_genes_TPM.tsv", sep="\t")

expr_target = pd.DataFrame(data=total_her2_expr['her2_status_by_ihc'])
expr_target['her2_status_by_ihc'] = (expr_target['her2_status_by_ihc'] == 'Positive').astype(int)

#print(expr_target)

expr_data = total_her2_expr.iloc[:, :-2]

#print(expr_data)

sub_expr_data = expr_data[['ERBB2', 'MED1', 'FGFR1']]

#clf = ensemble.RandomForestClassifier(n_estimators=2500, random_state=0)
c50 = rpackages.importr('C50')
rbase = rpackages.importr('base')

X_train, X_test, y_train, y_test = model_selection.train_test_split(
        preprocessing.scale(expr_data.values), expr_target, test_size=0.25 
)

treeModel = c50.C5_0(x=X_train, y=rbase.as_factor(y_train.values.ravel()))
print(rbase.summary(treeModel))


#for i in range(20):
#        tree.export_graphviz(clf.estimators_[i],
#                out_file='../graphs/classif_' + str(i) + '.dot',
#                feature_names=list(expr_data),
#                class_names=["Negative", "Positive"])

#print("Number of estimators: " + str(len(clf.estimators_)))
#print(clf.predict(X_test))
#print(y_test.values.ravel())
#print("AUC score: " + str(metrics.roc_auc_score(y_test, clf.predict(X_test))))
#print("Run time: " + str(time.time() - x) + " seconds")
