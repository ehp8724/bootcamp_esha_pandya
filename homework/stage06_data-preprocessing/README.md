\## Stage 06 — Data Preprocessing

\*\*Functions (src/cleaning.py):\*\*

\- `fill\_missing\_median(df, columns=None)`: median-impute numeric columns.

\- `drop\_missing(df, subset=None, how="any")`: drop rows with NA in subset (or any).

\- `normalize\_data(df, columns=None, method="standard"|"minmax")`: scale numeric features.



\*\*Workflow:\*\*

1\) Load raw from `/data/raw/`

2\) Type fixes (parse dates, numeric coercion)

3\) Fill → Drop → Normalize

4\) Save cleaned to `/data/processed/` with timestamp

5\) Compare before vs after (rows, NA totals, summary stats)



\*\*Assumptions:\*\* median imputation (MCAR/MAR), dropping rows not critical, StandardScaler assumes ~normal; document decisions and tradeoffs.



