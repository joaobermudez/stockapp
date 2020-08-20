import yfinance as yf
import streamlit as st
from PIL import Image
st.write("""
# Stock Price App
""")
image = Image.open("C:\\Users\\mars\\Desktop\\stock.jpg")
st.image(image, use_column_width =True)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
stock_sym = st.sidebar.text_input('Enter Stock Symbol/ticker ','GOOGL')
tickerSymbol = stock_sym.upper()
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write("""
## Analysts Recommendations
""")
tickerData.recommendations
st.write("""
## Major Stock holders
""")
tickerData.major_holders
st.write("""
## Next event (earnings, etc)
""")
tickerData.calendar
st.write("""
## Options Expirations
""")
tickerData.options
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.write("""
## Open Price
""")
st.line_chart(tickerDf.Open)
st.write("""
## Low Price
""")
st.line_chart(tickerDf.Low)
st.write("""
## High Price
""")
st.line_chart(tickerDf.High)

