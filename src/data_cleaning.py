import pandas as pd
import numpy as np

#replace null values with None
def replace_with_none(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace({np.nan: None})

#trim whitespace from string columns
def trim_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df

#remove duplicates
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()