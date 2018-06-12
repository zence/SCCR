from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale
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

total_her2_expr = pd.read_csv('../data/all_genes_TPM.tsv', sep='\t')

#total_her2_expr = total_her2_expr['ERBB2', 'MED1', 'FGFR1', 'her2_status_by_ihc', 'Sample']

expr_target = pd.DataFrame(data=total_her2_expr['her2_status_by_ihc'])
expr_target['her2_status_by_ihc'] = (expr_target['her2_status_by_ihc'] == 'Positive').astype(int)
expr_data = total_her2_expr.iloc[:, :-2]


#cv_results = cross_val_predict(clf, expr_data, expr_target.values.ravel(), cv=10)

#print(cv_results)

kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
misclassied_ids = []

for train, test in kf.split(expr_data, expr_target):
    clf = RandomForestClassifier(random_state=0)

    X_train, X_test = scale(expr_data.values[train]), scale(expr_data.values[test])
    y_train, y_test = expr_target.values[train], expr_target.values[test]
    print(y_test.ravel())
    #print(X_train)
    #print(y_train.ravel())
    clf.fit(X_train, y_train.ravel())

    testing_ids = total_her2_expr['Sample'].values[test]

    predictions = clf.predict(X_test)

    misclassied = compare_lists(y_test.ravel(), predictions)

    print(predictions)
    print(roc_auc_score(y_test.ravel(), predictions))
    print(testing_ids[misclassied])

    misclassied_ids.extend(testing_ids[misclassied])

total_her2_expr['RF_classified'] = total_her2_expr.apply(create_miscl_col, misclassied=misclassied_ids, axis=1)

total_her2_expr.iloc[:, :-3] = scale(total_her2_expr.iloc[:, :-3])

total_her2_expr.to_csv('../results/rf_genes_TPM.tsv.gz', sep='\t', index=False, compression='gzip')
