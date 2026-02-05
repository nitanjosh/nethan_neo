import pandas as pd
import numpy as np

def replace_with_none(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace({np.nan: None})
