import pandas as pd
import numpy as np

def std_calculator(x, std, mean):
    if std != 0:
        return ((x - mean) / std)
    else:
        return 0

def flag_column_continuous(in_data, clinical_data, dist_std, col_name, threshold):
    '''
        Flags all samples that fall outside of given threshold
    '''
    outlier_ids = clinical_data.loc[(dist_std > threshold) | (dist_std < -threshold)]
    print(outlier_ids[col_name])
    print(in_data)
    common_df = pd.merge(in_data, outlier_ids, left_index=True, right_index=True)
    print(common_df)
    for index, row in common_df.iterrows():
        notes = row['notes']
        print('** 	YOU SHOULD BE HERE	**')
        if notes != 'nan':
            print(notes)
            in_data.at[index, 'notes'] = ';'.join([notes, col_name])
        else:
            in_data.at[index, 'notes'] = col_name
    return in_data

def flag_column_discrete(in_data, clinical_data, col_name):
    minor_vals = []

    column = clinical_data[col_name].astype(str)
    column = column[column != 'nan']
    possible_vals = column.unique()
    if len(possible_vals) > 5:
        return in_data
    for pos_val in possible_vals:
        percent_val = len(column[column == pos_val]) / len(column)
        print(str(pos_val) + ' ' + str(percent_val))
        if percent_val <= 0.05:
            minor_vals.append(pos_val)
    outlier_ids = clinical_data.loc[clinical_data[col_name].astype(str).isin(list(minor_vals))]
    common_df = pd.merge(in_data, outlier_ids, left_index=True, right_index=True)
    print(common_df)
    for index, row in common_df.iterrows():
        notes = row['notes']
        grouping = col_name + ' (' + row[col_name] + ')'
        if notes != 'nan':
            in_data.at[index, 'notes'] = '; '.join([notes, grouping])
        else:
            in_data.at[index, 'notes'] = grouping
    return in_data

def make_notes(in_data, threshold=2, cols=['age_at_diagnosis', 'gender']):
    clinical_data = pd.read_csv('../../../../../data/all_clinical_data.tsv', sep='\t', index_col=0)
    clinical_data = clinical_data.replace('[Not Available]', np.NaN)
    clinical_data.fillna(0)

    for col_n in cols:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" + col_n + "\n\n\n")
        try:
            clinical_data[col_n].astype(float)
            in_data = make_continuous(in_data, clinical_data, threshold, col_n)
        except ValueError:
            in_data = make_discrete(in_data, clinical_data, col_n)
    print("FINAL:\n")
    print(in_data)
    in_data = pd.merge(in_data, pd.DataFrame(clinical_data.her2_status_by_ihc), left_index=True, right_index=True)
    in_data.to_csv('../results/notes_and_stuff.tsv', sep='\t')

def make_continuous(in_data, clinical_data, threshold, col_name):
    std = clinical_data[col_name].astype(float).std(0)
    mean = clinical_data[col_name].astype(float).mean(0)

    dist_std = clinical_data[col_name].astype(float).apply(std_calculator, args=(std, mean))

    print(clinical_data[col_name].astype(float).unique())
    #print(clinical_data.loc[(dist_std > 1) |
                            #(dist_std < -1), 'age_at_diagnosis'])

    #print((dist_std > 2) | (dist_std < -2))
    in_data = flag_column_continuous(in_data.copy(), clinical_data, dist_std, col_name, threshold)
    print(in_data)

    #print(pd.merge(in_df, clinical_data, left_index=True, right_index=True))
    return in_data

def make_discrete(in_data, clinical_data, col_name):    
    in_data = flag_column_discrete(in_data.copy(), clinical_data, col_name)
    return in_data

if __name__ == '__main__':
    in_df = pd.read_csv('../results/misclassified_samples.tsv', sep='\t', index_col=0)
    in_df['notes'] = in_df['notes'].astype(str)
    header = ''
    with open('../../../../../data/all_clinical_data.tsv', 'r') as in_f:
        header = in_f.readline().strip().split('\t')
    #print(header)
    #make_notes(in_df, cols=['age_at_diagnosis', 'gender', 
               #'ethnicity', 'history_other_malignancy', 'history_neoadjuvant_treatment', 
               #'tumor_status', 'vital_status'])
    make_notes(in_df, threshold=1, cols=header)
