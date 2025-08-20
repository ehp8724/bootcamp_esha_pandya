# src/cleaning.py
from __future__ import annotations
from typing import Iterable, Literal, Optional
import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, columns: Optional[Iterable[str]] = None) -> pd.DataFrame:
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    for col in columns:
        if col in out.columns:
            median_val = out[col].median(skipna=True)
            out[col] = out[col].fillna(median_val)
    return out

def drop_missing(
    df: pd.DataFrame, 
    subset: Optional[Iterable[str]] = None, 
    how: Literal["any","all"] = "any"
) -> pd.DataFrame:
    out = df.copy()
    return out.dropna(subset=list(subset) if subset is not None else None, how=how)

def normalize_data(
    df: pd.DataFrame, 
    columns: Optional[Iterable[str]] = None, 
    method: Literal["standard","minmax"] = "standard"
) -> pd.DataFrame:
    from sklearn.preprocessing import StandardScaler, MinMaxScaler

    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    cols = [c for c in columns if c in out.columns]

    if not cols:
        return out

    scaler = StandardScaler() if method == "standard" else MinMaxScaler()
    out[cols] = scaler.fit_transform(out[cols].astype(float))
    return out
