import streamlit as st
import pandas as pd
import yfinance as yf
from pmdarima.arima import auto_arima

st.title("Stock Forcasting Application")
st.caption("Please do not use this application's prediction/forcasting to make your financial investments--- This Application is for Educational purpose only. ")
st.sidebar.caption("Please do not use this application's prediction/forcasting to make your financial investments--- This Application is for Educational purpose only.")

stocks_list = ["AAL","AAPL","ABMD","ABNB","ADBE","ADI","ADP","ADSK","AEP","AKAM","ALGN","ALNY","AMAT","AMD","AMGN","AMZN","ANSS","APA",
               "APP","ARCC","ATVI","AVGO","AZPN","BIIB","BKNG","BKR","BMRN","BSY","CAR","CDNS","CDW","CEG","CERN","CG","CGNX","CHK","CHRW"
    ,"CHTR","CINF","CMCSA","CME","COIN","COST","CPRT","CRWD","CSCO","CSGP","CSX","CTAS","CTSH","CTXS","CZR","DDOG","DISH","DLTR","DOCU"
    ,"DXCM","EA","EBAY","ENPH","ENTG","EQIX","ETSY","EWBC","EXAS","EXC","EXPD","EXPE","FANG","FAST","FB","FCNCA","FFIV","FISV","FITB",
    "FOX","FOXA","FTNT","FWONA","FWONK","GFS","GILD","GLPI","GOOG","GOOGL","HAS","HBAN","HOLX","HON","HSIC","HST","IDXX","IEP","ILMN",
    "INCY","INTC","INTU","ISRG","JBHT","JKHY","KDP","KHC","KLAC","LAMR","LBRDA","LBRDK","LCID","LKQ","LNT","LOGI","LPLA","LRCX","LSXMA"
    ,"LSXMB","LSXMK","LYFT","MAR","MCHP","MDB","MDLZ","MKTX","MNST","MORN","MPWR","MRNA","MSFT","MTCH","MU","NDAQ","NDSN","NFLX","NLOK"
    ,"NTAP","NTRS","NVDA","NWS","NWSA","ODFL","OKTA","ON","ORLY","PANW","PARA","PARAA","PAYX","PCAR","PCTY","PEP","PFG","PLUG","PODD",
    "POOL","PTC","PYPL","QCOM","QRVO","REG","REGN","RIVN","ROKU","ROST","RPRX","SBAC","SBNY","SBUX","SGEN","SIRI","SIVB","SNPS","SPLK"
    ,"SSNC","STLD","SWKS","TECH","TER","TMUS","TRMB","TROW","TSCO","TSLA","TTD","TTWO","TW","TXN","UAL","UHAL","ULTA","VRSK","VRSN","VRTX"
    ,"VTRS","WBA","WBD","WDAY","WDC","WMG","XEL","XM","Z","ZBRA","ZG","ZI","ZM","ZNGA","ZS"]


ticker_sidebar_sel_itm = st.sidebar.selectbox("Choose your company ticker",stocks_list)

ticker_sidebar_sel_itm = str(ticker_sidebar_sel_itm)

raw_data = yf.download(tickers= ticker_sidebar_sel_itm, start='2015-01-01' )

st.write("Historical Raw Data for stocks is as follows:")

st.write(raw_data)

df = raw_data.copy()

df = df.asfreq('b')

df = df.fillna(method = 'bfill')

st.write("The Line Chart for the stock is as follows:")
st.line_chart(df.Close)

if st.button("Show Forcast for closing price of stock for upcoming 5 business days"):
    st.caption("The Model will take some time for computation")
    arima_model = auto_arima(df.Close)
    forcast = pd.DataFrame(arima_model.predict(n_periods = 5))
    forcast.columns = ["Forcast for upcoming 5 business days"]
    forcast.set_index("Forcast for upcoming 5 business days")
    st.write(forcast)


