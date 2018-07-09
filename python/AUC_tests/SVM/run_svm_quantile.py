from sklearn.svm import SVC
from sklearn.preprocessing import quantile_transform
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold

import pandas as pd

def create_miscl_col(row, misclassied):
    if row['Sample'] in misclassied:
        val = 'Misclassified'
    else:
        val = 'Correct'
    return val

def compare_lists(x, y):
    discrepancies = []
    for i in range(len(x)):
        if x[i] != y[i]:
            discrepancies.append(i)
    return discrepancies

def run(genes):

    total_her2_expr = pd.read_csv('../../../data/all_genes_TPM.tsv', sep='\t')

    total_her2_expr = total_her2_expr[[*genes, 'her2_status_by_ihc', 'Sample']]

    expr_target = pd.DataFrame(data=total_her2_expr['her2_status_by_ihc'])
    expr_target['her2_status_by_ihc'] = (expr_target['her2_status_by_ihc'] == 'Positive').astype(int)
    expr_data = quantile_transform(total_her2_expr.iloc[:, :-2])


    #cv_results = cross_val_predict(clf, expr_data, expr_target.values.ravel(), cv=10)

    #print(cv_results)

    kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
    auc_vals = []

    for train, test in kf.split(expr_data, expr_target):
        clf = SVC(kernel='rbf', C=1, random_state=0, probability=True)

        # Look at robust_scaler (or however it's spelled)

        X_train, X_test = expr_data[train], expr_data[test]
        y_train, y_test = expr_target.values[train], expr_target.values[test]
        #print(X_train)
        #print(y_train.ravel())
        clf.fit(X_train, y_train.ravel())

        testing_ids = total_her2_expr['Sample'].values[test]

        predictions = clf.predict(X_test)

        misclassied = compare_lists(y_test.ravel(), predictions)

        auc_vals.append(roc_auc_score(y_test.ravel(), predictions))

    return (sum(auc_vals) / len(auc_vals))
