import streamlit as st
import yfinance as yf

# 🏷️ App title and disclaimer
st.title("📈 Stock Forecasting Application")
st.caption("⚠️ This app is for educational purposes only. Do not use its forecasts for financial investments.")
st.sidebar.caption("⚠️ This app is for educational purposes only. Do not use its forecasts for financial investments.")

# 📌 List of tickers for selection
stocks_list = [
    "AAL", "AAPL", "ABMD", "ABNB", "ADBE", "ADI", "ADP", "ADSK", "AEP", "AKAM", "ALGN", "ALNY", "AMAT", "AMD", "AMGN", "AMZN", "ANSS", "APA",
    "APP", "ARCC", "ATVI", "AVGO", "AZPN", "BIIB", "BKNG", "BKR", "BMRN", "BSY", "CAR", "CDNS", "CDW", "CEG", "CERN", "CG", "CGNX", "CHK", "CHRW",
    "CHTR", "CINF", "CMCSA", "CME", "COIN", "COST", "CPRT", "CRWD", "CSCO", "CSGP", "CSX", "CTAS", "CTSH", "CTXS", "CZR", "DDOG", "DISH", "DLTR", "DOCU",
    "DXCM", "EA", "EBAY", "ENPH", "ENTG", "EQIX", "ETSY", "EWBC", "EXAS", "EXC", "EXPD", "EXPE", "FANG", "FAST", "META", "FCNCA", "FFIV", "FISV", "FITB",
    "FOX", "FOXA", "FTNT", "FWONA", "FWONK", "GFS", "GILD", "GLPI", "GOOG", "GOOGL", "HAS", "HBAN", "HOLX", "HON", "HSIC", "HST", "IDXX", "IEP", "ILMN",
    "INCY", "INTC", "INTU", "ISRG", "JBHT", "JKHY", "KDP", "KHC", "KLAC", "LAMR", "LBRDA", "LBRDK", "LCID", "LKQ", "LNT", "LOGI", "LPLA", "LRCX", "LSXMA",
    "LSXMB", "LSXMK", "LYFT", "MAR", "MCHP", "MDB", "MDLZ", "MKTX", "MNST", "MORN", "MPWR", "MRNA", "MSFT", "MTCH", "MU", "NDAQ", "NDSN", "NFLX", "NLOK",
    "NTAP", "NTRS", "NVDA", "NWS", "NWSA", "ODFL", "OKTA", "ON", "ORLY", "PANW", "PARA", "PARAA", "PAYX", "PCAR", "PCTY", "PEP", "PFG", "PLUG", "PODD",
    "POOL", "PTC", "PYPL", "QCOM", "QRVO", "REG", "REGN", "RIVN", "ROKU", "ROST", "RPRX", "SBAC", "SBNY", "SBUX", "SGEN", "SIRI", "SNPS", "SPLK",
    "SSNC", "STLD", "SWKS", "TECH", "TER", "TMUS", "TRMB", "TROW", "TSCO", "TSLA", "TTD", "TTWO", "TW", "TXN", "UAL", "UHAL", "ULTA", "VRSK", "VRSN", "VRTX",
    "VTRS", "WBA", "WBD", "WDAY", "WDC", "WMG", "XEL", "XM", "Z", "ZBRA", "ZG", "ZI", "ZM", "ZNGA", "ZS"
]

# 🎯 Ticker selection
selected_ticker = st.sidebar.selectbox("Choose your company ticker", stocks_list)

# 📥 Download historical stock data
st.write(f"📦 Downloading data for: {selected_ticker}")
data = yf.download(tickers=selected_ticker, start='2024-01-01')

# ❌ Handle empty data
if data.empty:
    st.error("No data found for the selected ticker. It may be inactive, delisted, or rate-limited. Please try another.")
    st.stop()

# 📊 Display raw data
st.subheader("📄 Historical Raw Data")
st.write(data)

# 📈 Show closing price chart
st.subheader("📉 Closing Price Trend")
st.line_chart(data["Close"])

