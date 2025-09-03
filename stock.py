import streamlit as st
import pandas as pd
import yfinance as yf
from pmdarima.arima import auto_arima

# Title and disclaimer
st.title("📈 Stock Forecasting Application")
st.caption("⚠️ This application is for educational purposes only. Do not use its predictions for financial investments.")
st.sidebar.caption("⚠️ This application is for educational purposes only. Do not use its predictions for financial investments.")

# Full Fortune 500 ticker list
stocks_list = ["AAL","AAPL","ABMD","ABNB","ADBE","ADI","ADP","ADSK","AEP","AKAM","ALGN","ALNY","AMAT","AMD","AMGN","AMZN","ANSS","APA",
               "APP","ARCC","ATVI","AVGO","AZPN","BIIB","BKNG","BKR","BMRN","BSY","CAR","CDNS","CDW","CEG","CERN","CG","CGNX","CHK","CHRW",
               "CHTR","CINF","CMCSA","CME","COIN","COST","CPRT","CRWD","CSCO","CSGP","CSX","CTAS","CTSH","CTXS","CZR","DDOG","DISH","DLTR",
               "DOCU","DXCM","EA","EBAY","ENPH","ENTG","EQIX","ETSY","EWBC","EXAS","EXC","EXPD","EXPE","FANG","FAST","FB","FCNCA","FFIV",
               "FISV","FITB","FOX","FOXA","FTNT","FWONA","FWONK","GFS","GILD","GLPI","GOOG","GOOGL","HAS","HBAN","HOLX","HON","HSIC","HST",
               "IDXX","IEP","ILMN","INCY","INTC","INTU","ISRG","JBHT","JKHY","KDP","KHC","KLAC","LAMR","LBRDA","LBRDK","LCID","LKQ","LNT",
               "LOGI","LPLA","LRCX","LSXMA","LSXMB","LSXMK","LYFT","MAR","MCHP","MDB","MDLZ","MKTX","MNST","MORN","MPWR","MRNA","MSFT",
               "MTCH","MU","NDAQ","NDSN","NFLX","NLOK","NTAP","NTRS","NVDA","NWS","NWSA","ODFL","OKTA","ON","ORLY","PANW","PARA","PARAA",
               "PAYX","PCAR","PCTY","PEP","PFG","PLUG","PODD","POOL","PTC","PYPL","QCOM","QRVO","REG","REGN","RIVN","ROKU","ROST","RPRX",
               "SBAC","SBNY","SBUX","SGEN","SIRI","SIVB","SNPS","SPLK","SSNC","STLD","SWKS","TECH","TER","TMUS","TRMB","TROW","TSCO","TSLA",
               "TTD","TTWO","TW","TXN","UAL","UHAL","ULTA","VRSK","VRSN","VRTX","VTRS","WBA","WBD","WDAY","WDC","WMG","XEL","XM","Z","ZBRA",
               "ZG","ZI","ZM","ZNGA","ZS"]

# Sidebar selection
ticker = st.sidebar.selectbox("Choose a company ticker:", stocks_list)

# Function to fetch and validate stock data
@st.cache_data
def get_valid_stock_data(ticker):
    try:
        data = yf.download(ticker, start='2022-01-01')
        if data.empty or "Close" not in data.columns:
            return None
        return data
    except Exception:
        return None

# Fetch data
raw_data = get_valid_stock_data(ticker)

# Validate data
if raw_data is None:
    st.error(f"No data found for ticker '{ticker}'. It may be delisted or unavailable.")
    st.stop()

# Display raw data
st.subheader("📊 Historical Stock Data")
st.write(raw_data.tail())

# Prepare data
df = raw_data.copy()
df = df.asfreq('B')  # Business day frequency
df = df.fillna(method='bfill').fillna(method='ffill')  # Fill missing values

# Line chart
st.subheader("📉 Closing Price Over Time")
st.line_chart(df['Close'])

# Forecasting
if st.button("🔮 Forecast Closing Price for Next 5 Business Days"):
    st.caption("⏳ Please wait while the model computes the forecast...")

    # Clean series
    series = df['Close'].dropna().astype(float)

    if series.empty:
        st.error("No valid closing price data available for forecasting.")
        st.stop()

    # Fit ARIMA model
    arima_model = auto_arima(series, error_action='ignore', suppress_warnings=True)

    # Predict next 5 business days
    forecast_values = arima_model.predict(n_periods=5)
    future_dates = pd.date_range(start=series.index[-1], periods=6, freq='B')[1:]

    forecast_df = pd.DataFrame({
        "Forecasted Close Price": forecast_values
    }, index=future_dates)

    st.subheader("📅 Forecast for Next 5 Business Days")
    st.write(forecast_df)
