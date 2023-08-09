import pandas as pd


def rename_columns(df, names):
    new_df = pd.DataFrame(df)
    for cont, new_name in enumerate(names):
        new_df.rename(columns={new_df.columns[cont]: new_name})
    return new_df
