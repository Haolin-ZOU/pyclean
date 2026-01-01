import pandas as pd

def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize column names of a DataFrame.

    Args:
        df: The input pandas DataFrame.

    Returns:
        A pandas DataFrame with standardized column names.
    """
    new_df = df.copy()
    new_cols = {col: col.lower().replace(" ", "_").replace(".", "_") for col in new_df.columns}
    new_df = new_df.rename(columns=new_cols)
    return new_df
