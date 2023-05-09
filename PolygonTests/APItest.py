import pandas as pd
import plotly.graph_objects as go
import requests

# Get data from polygon API
api_key = "ST9vA1GYk8pSmFUQaFBQBPM2armBdsnm"
symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"
url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}?unadjusted=true&sort=asc&limit=5000&apiKey={api_key}"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["results"])

# Convert timestamps to datetime objects // This was missing, this formatting is crucial
df["t"] = pd.to_datetime(df["t"], unit="ms")

# Rename columns
df.rename(columns={"t": "Date", "o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"}, inplace=True)

# Create OHLC chart
fig = go.Figure()

# Add OHLC trace
fig.add_trace(go.Ohlc(x=df["Date"], open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"], name="OHLC"))

# Add volume trace
fig.add_trace(go.Bar(x=df["Date"], y=df["Volume"], name="Volume", marker_color="rgba(100, 100, 100, 0.5)", yaxis="y2"))

# Update layout
fig.update_layout(title=f"OHLC Chart for {symbol}", yaxis_title="Price ($)", yaxis2=dict(title="Volume", overlaying="y", side="right"))

# Customize appearance
fig.update_xaxes(type="category")
fig.update_yaxes(showgrid=True, gridcolor="rgba(200, 200, 200, 0.2)")

fig.show()
