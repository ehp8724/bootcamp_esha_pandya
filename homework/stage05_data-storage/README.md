\## Data Storage (Stage 05)

\- \*\*Structure:\*\* `data/raw/` (immutable inputs) and `data/processed/` (derived tables).

\- \*\*Formats:\*\* CSV for small/exchange; Parquet for analysis-ready tables (type-preserving, fast).

\- \*\*Env paths:\*\* `.env` defines `DATA\_DIR\_RAW` and `DATA\_DIR\_PROCESSED`. Code reads these via `dotenv` and `pathlib`.

\- \*\*Utilities:\*\* `src/storage.py` provides `write\_df`/`read\_df` that route by file suffix and create missing folders; Parquet uses `pyarrow`.

\- \*\*Validation:\*\* After reload, we confirm shapes match and critical dtypes (e.g., `date`, `ead`) are correct.



