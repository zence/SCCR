import pandas as pd
import numpy as np

def std_calculator(x, std, mean):
    return ((x - mean) / std)

def flag_column_continuous(in_df, clinical_data, dist_std, col_name):
    outlier_ids = clinical_data.loc[(dist_std > 1) | (dist_std < -1)]
    print(outlier_ids)
    print(in_df)
    common_df = pd.merge(in_df, outlier_ids, left_index=True, right_index=True)
    print(common_df)
    for index, row in common_df.iterrows():
        notes = row['notes']
        print('** 	YOU SHOULD BE IN LOVE	**')
        if notes != 'nan':
            print(notes)
            in_df.at[index, 'notes'] = ';'.join([notes, col_name])
        else:
            in_df.at[index, 'notes'] = col_name
    return in_df

def flag_column_discrete(in_df, clinical_data, minor_val, col_name):
    outlier_ids = clinical_data.loc[clinical_data[col_name] == minor_val]
    common_df = pd.merge(in_df, outlier_ids, left_index=True, right_index=True)
    print(common_df)

def make_notes(in_df):
    clinical_data = pd.read_csv('../../../../../data/all_clinical_data.tsv', sep='\t', index_col=0)
    clinical_data = clinical_data.replace('[Not Available]', np.NaN)
    clinical_data.fillna(0)

    std = clinical_data.age_at_diagnosis.astype(float).std(0)
    mean = clinical_data.age_at_diagnosis.astype(float).mean(0)

    dist_std = clinical_data.age_at_diagnosis.astype(float).apply(std_calculator, args=(std, mean))

    print(clinical_data.age_at_diagnosis.astype(float).unique())
    print(clinical_data.loc[(dist_std > 1) |
                            (dist_std < -1), 'age_at_diagnosis'])

    print((dist_std > 2) | (dist_std < -2))
    #print(flag_column_cont(in_df, clinical_data, dist_std, 'age_at_diagnosis'))

    #print(pd.merge(in_df, clinical_data, left_index=True, right_index=True))
    flag_column_discrete(in_df, clinical_data, 'MALE', 'gender')

if __name__ == '__main__':
    in_df = pd.read_csv('../results/misclassified_samples.tsv', sep='\t', index_col=0)
    in_df['notes'] = in_df['notes'].astype(str)
    make_notes(in_df)
