from __future__ import annotations
from pathlib import Path
from typing import Optional
import pandas as pd

def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def write_df(df: pd.DataFrame, path: Path) -> Path:
    _ensure_parent(path)
    suf = path.suffix.lower()
    if suf == ".csv":
        df.to_csv(path, index=False)
        return path
    elif suf == ".parquet":
        try:
            df.to_parquet(path)  # engine inferred (pyarrow installed per setup)
        except Exception as e:
            raise RuntimeError(
                "Failed to write Parquet. Ensure 'pyarrow' is installed."
            ) from e
        return path
    else:
        raise ValueError(f"Unsupported file suffix: {suf}. Use .csv or .parquet")

def read_df(path: Path, parse_dates: Optional[list[str]] = None) -> pd.DataFrame:
    suf = path.suffix.lower()
    if suf == ".csv":
        return pd.read_csv(path, parse_dates=parse_dates or [])
    elif suf == ".parquet":
        try:
            return pd.read_parquet(path)
        except Exception as e:
            raise RuntimeError(
                "Failed to read Parquet. Ensure 'pyarrow' is installed."
            ) from e
    else:
        raise ValueError(f"Unsupported file suffix: {suf}. Use .csv or .parquet")
