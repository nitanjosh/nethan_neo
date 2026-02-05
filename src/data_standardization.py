# Data Standardization	
# * Converting date formats	
# * Normalizing units and currencies	
# * Standardizing text case	
import pandas as pd
import numpy as np

#Converting date formats
def convert_date_format(df: pd.DataFrame, date_columns: list, date_format: str) -> pd.DataFrame:
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime(date_format)
    return df

#Normalizing units and currencies
def normalize_units(df: pd.DataFrame, unit_mappings: dict) -> pd.DataFrame:
    for col, (from_unit, to_unit, factor) in unit_mappings.items():
        df[col] = df[col].apply(lambda x: x * factor if pd.notnull(x) else x)
    return df

#Standardizing text case
def standardize_text_case(df: pd.DataFrame, text_columns: list, case: str = 'lower') -> pd.DataFrame:
    for col in text_columns:
        if case == 'lower':
            df[col] = df[col].str.lower()
        elif case == 'upper':
            df[col] = df[col].str.upper()
        elif case == 'title':
            df[col] = df[col].str.title()
    return df