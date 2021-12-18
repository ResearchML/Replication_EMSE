import pandas as pd
import numpy as np
import os

path_root = os.path.dirname(os.getcwd())

if __name__ == '__main__':
    data_path = os.path.join(path_root,'data', 'breast-cancer-wisconsin.data')
    # or data_path = 'c:/yourfolder/breast-cancer-wisconsin.data' should aslo work

    # Note: the data file is without header
    data_df = pd.read_csv(data_path, header =None)
    no_cols = len(data_df.columns)
    # new_cols = ['col0','col1', 'col2','col3','col4','col5','col6','col7','col8','col9','col10']
    new_cols = ['col'+str(i) for i in range (no_cols)]
    print(new_cols)

    data_df.columns = new_cols
    print(data_df.head(5))

    print(set(data_df['col6'].values)) # unique values in col pos 6

    for col in new_cols[1:]: # excluding the first column as it is id
        df_null = data_df[data_df[col]=='?']
        print('Number of rows with null in col {} ={}'.format(col,df_null.shape[0]))

    data_df = data_df.replace(to_replace = '?', value = np.nan) # or ''
    print(data_df.head(30))

    for col in new_cols[1:]:
        data_df[col] = data_df[col].astype(float)
    print(data_df.head(25))


    for col in new_cols[1:]:
        data_df[col] = data_df[col].fillna(data_df[col].mean())
    print(data_df[20:25])


    #if you need to convert all columns back to int, else skip the following
    for col in new_cols[1:]:
        data_df[col] = data_df[col].astype(int)

    print(data_df[20:25])

    # check the col6 again
    col ='col6'
    df_null = data_df[data_df[col]=='?']
    print('Number of rows with null in {} = {}'.format(col,df_null.shape[0]))

    # save cleaned data
    cleaned_data_path = os.path.join(path_root,'data', 'breast-cancer-wisconsin-cleaned.data')
    data_df.to_csv(cleaned_data_path, index = False, header = False)


