import pandas as pd

def load_stock_data():
    df = pd.read_csv("data/BFS_Share_Price.csv", parse_dates=["Date"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)
    return df
