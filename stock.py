import streamlit as st
import pandas as pd
import yfinance as yf
from pmdarima.arima import auto_arima

# Title and disclaimer
st.title("Stock Forecasting Application")
st.caption("Please do not use this application's prediction/forecasting to make your financial investments — This application is for educational purposes only.")
st.sidebar.caption("Please do not use this application's prediction/forecasting to make your financial investments — This application is for educational purposes only.")

# Ticker selection
stocks_list = [
    "AAL", "AAPL", "ABMD", "ABNB", "ADBE", "ADI", "ADP", "ADSK", "AEP", "AKAM", "ALGN", "ALNY", "AMAT", "AMD", "AMGN", "AMZN", "ANSS", "APA",
    "APP", "ARCC", "ATVI", "AVGO", "AZPN", "BIIB", "BKNG", "BKR", "BMRN", "BSY", "CAR", "CDNS", "CDW", "CEG", "CERN", "CG", "CGNX", "CHK", "CHRW",
    "CHTR", "CINF", "CMCSA", "CME", "COIN", "COST", "CPRT", "CRWD", "CSCO", "CSGP", "CSX", "CTAS", "CTSH", "CTXS", "CZR", "DDOG", "DISH", "DLTR", "DOCU",
    "DXCM", "EA", "EBAY", "ENPH", "ENTG", "EQIX", "ETSY", "EWBC", "EXAS", "EXC", "EXPD", "EXPE", "FANG", "FAST", "FB", "FCNCA", "FFIV", "FISV", "FITB",
    "FOX", "FOXA", "FTNT", "FWONA", "FWONK", "GFS", "GILD", "GLPI", "GOOG", "GOOGL", "HAS", "HBAN", "HOLX", "HON", "HSIC", "HST", "IDXX", "IEP", "ILMN",
    "INCY", "INTC", "INTU", "ISRG", "JBHT", "JKHY", "KDP", "KHC", "KLAC", "LAMR", "LBRDA", "LBRDK", "LCID", "LKQ", "LNT", "LOGI", "LPLA", "LRCX", "LSXMA",
    "LSXMB", "LSXMK", "LYFT", "MAR", "MCHP", "MDB", "MDLZ", "MKTX", "MNST", "MORN", "MPWR", "MRNA", "MSFT", "MTCH", "MU", "NDAQ", "NDSN", "NFLX", "NLOK",
    "NTAP", "NTRS", "NVDA", "NWS", "NWSA", "ODFL", "OKTA", "ON", "ORLY", "PANW", "PARA", "PARAA", "PAYX", "PCAR", "PCTY", "PEP", "PFG", "PLUG", "PODD",
    "POOL", "PTC", "PYPL", "QCOM", "QRVO", "REG", "REGN", "RIVN", "ROKU", "ROST", "RPRX", "SBAC", "SBNY", "SBUX", "SGEN", "SIRI", "SIVB", "SNPS", "SPLK",
    "SSNC", "STLD", "SWKS", "TECH", "TER", "TMUS", "TRMB", "TROW", "TSCO", "TSLA", "TTD", "TTWO", "TW", "TXN", "UAL", "UHAL", "ULTA", "VRSK", "VRSN", "VRTX",
    "VTRS", "WBA", "WBD", "WDAY", "WDC", "WMG", "XEL", "XM", "Z", "ZBRA", "ZG", "ZI", "ZM", "ZNGA", "ZS"
]

ticker_sidebar_sel_itm = st.sidebar.selectbox("Choose your company ticker", stocks_list)

# Download historical data
raw_data = yf.download(tickers=ticker_sidebar_sel_itm, start='2023-01-01')
st.write("Historical Raw Data for stocks is as follows:")
st.write(raw_data)

# Prepare data
df = raw_data.copy()
df = df.asfreq('b')  # Business day frequency
df = df.fillna(method='bfill')  # Backfill missing values

# Show line chart
st.write("The Line Chart for the stock is as follows:")
st.line_chart(df.Close)

# Forecasting
if st.button("Show Forecast for closing price of stock for upcoming 5 business days"):
    st.caption("The model will take a few seconds to compute...")
    try:
        arima_model = auto_arima(df.Close, seasonal=False, suppress_warnings=True)
        forecast = pd.DataFrame(arima_model.predict(n_periods=5), columns=["Forecasted Close Price"])
        forecast.index = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=5, freq='B')
        st.write(forecast)
    except Exception as e:
        st.error(f"Forecasting failed: {e}")
