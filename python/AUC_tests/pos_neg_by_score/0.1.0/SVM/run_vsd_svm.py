from sklearn.svm import SVC
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

def run(genes, random_seed, misclassied_samples):

    total_her2_expr = pd.read_csv('../../../../../data/vsd_FeatureCounts_cleanscores.tsv', sep='\t', index_col=0)

    total_her2_expr = total_her2_expr[[*genes, 'her2_status_by_ihc']]
    total_her2_expr = total_her2_expr.loc[(total_her2_expr['her2_status_by_ihc'] == 'Positive') |
                                          (total_her2_expr['her2_status_by_ihc'] == 'Negative')]

    print(total_her2_expr)

    expr_target = pd.DataFrame(data=total_her2_expr['her2_status_by_ihc'])
    expr_target['her2_status_by_ihc'] = (expr_target['her2_status_by_ihc'] == 'Positive').astype(int)
    expr_data = total_her2_expr.iloc[:, :-1]


    #cv_results = cross_val_predict(clf, expr_data, expr_target.values.ravel(), cv=10)

    #print(cv_results)

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_seed)
    auc_vals = []

    for train, test in kf.split(expr_data, expr_target):
        clf = SVC(kernel='rbf', C=1, random_state=random_seed, probability=True)

        # Look at robust_scaler (or however it's spelled)

        X_train, X_test = expr_data.values[train], expr_data.values[test]
        y_train, y_test = expr_target.values[train], expr_target.values[test]
        #print(X_train)
        #print(y_train.ravel())
        clf.fit(X_train, y_train.ravel())

        testing_ids = total_her2_expr.index[test]

        print(testing_ids)

        predictions = clf.predict(X_test)

        misclassied = compare_lists(y_test.ravel(), predictions)

        misclassied_ids = testing_ids[misclassied]

        for mis_id in misclassied_ids:
            if mis_id not in misclassied_samples['Sample'].values:
                print("**	YOU SHOULD BE HERE	**")
                misclassied_samples = misclassied_samples.append({'Sample': mis_id, 'times_misclassified': 1, 'notes': ''}, ignore_index=True)
            else:
                times_misclassified = misclassied_samples.loc[misclassied_samples['Sample'] == mis_id]['times_misclassified']
                cur_ix = misclassied_samples.loc[misclassied_samples['Sample'] == mis_id].index
                misclassied_samples.at[cur_ix, 'times_misclassified'] = times_misclassified + 1

        #auc_vals.append(roc_auc_score(y_test.ravel(), predictions))
        #print(misclassied_samples)

    return misclassied_samples
