def get_summary_stats(df: pd.DataFrame):
    stats = df.describe()
    return stats