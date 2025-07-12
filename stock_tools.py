import pandas as pd

df = pd.read_csv("data/BFS_Share_Price.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors='coerce')
df.dropna(subset=["Date"], inplace=True)

def get_stock_price_on_date(date_str: str) -> str:
    try:
        date_obj = pd.to_datetime(date_str, dayfirst=True)
        row = df[df["Date"] == date_obj]
        if row.empty:
            return f"No stock data for {date_str}"
        close_price = row.iloc[0]["Close"]
        return f"The closing stock price on {date_str} was ₹{close_price:.2f}."
    except Exception as e:
        return f"Error: {str(e)}"

def _filter_by_month_year(month_year: str):
    try:
        date = pd.to_datetime("01-" + month_year, dayfirst=True)
        return df[(df["Date"].dt.month == date.month) & (df["Date"].dt.year == date.year)]
    except:
        return pd.DataFrame()

def get_highest_price(month_year: str) -> str:
    subset = _filter_by_month_year(month_year)
    if subset.empty:
        return f"No data found for {month_year}"
    return f"Highest stock price in {month_year} was ₹{subset['Close'].max():.2f}"

def get_lowest_price(month_year: str) -> str:
    subset = _filter_by_month_year(month_year)
    if subset.empty:
        return f"No data found for {month_year}"
    return f"Lowest stock price in {month_year} was ₹{subset['Close'].min():.2f}"

def get_average_price(month_year: str) -> str:
    subset = _filter_by_month_year(month_year)
    if subset.empty:
        return f"No data found for {month_year}"
    return f"Average stock price in {month_year} was ₹{subset['Close'].mean():.2f}"
