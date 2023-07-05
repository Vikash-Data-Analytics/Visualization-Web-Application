import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Venturesathi | Data Analytics Solutions",
    page_icon="Logo.jpg",
    layout='wide',
)

# with open("Filter.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
logo_image = "Logo.png"

col1, col2 = st.columns([1, 3])

with col1:
    st.image(logo_image, width=200)

with col2:
    st.subheader("VentureSathi Insights - Driving Growth through Data Analytics")
    # st.markdown("<h1 color: #000080;'>Stock Price Analysis</h1>", unsafe_allow_html=True)


USER_CREDENTIALS = {
    'vikash': 'vikash@44',
    'venture': 'venture',
    'user': 'password'
}

stocks = {
    'Reliance': 'RELIANCE.NS',
    'Zomato': 'ZOMATO.NS',
    'Nifty': '^NSEI'
}

def main():
    if is_user_logged_in():
        render_authorized_content()
    else:
        render_login_form()

def is_user_logged_in():
    return 'logged_in' in st.session_state and st.session_state.logged_in

def render_login_form():
    st.markdown("<h3 style='text-align: center; color: #000000;'>LogIn</h3>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in USER_CREDENTIALS and password == USER_CREDENTIALS[username]:
            st.session_state.logged_in = True
            show_login_popup()
        else:
            st.error("Invalid username or password")

def render_authorized_content():
    st.markdown("<h1 style='text-align: center; color: #000080;'>Stock Price Analysis</h1>", unsafe_allow_html=True)

    selected_stock = st.selectbox('Select a stock', list(stocks.keys()))
    stock_data = yf.download(tickers=stocks[selected_stock], period='1d', interval='1m')

    st.markdown("<h3 style='text-align: center;'>Open And Lowest Price</h3>", unsafe_allow_html=True)
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig1.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], name='Open', line=dict(color='blue')), secondary_y=False)
    fig1.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Low'], name='Low', line=dict(color='green')), secondary_y=False)
    fig1.update_layout(title_text='Open and Lowest Price')
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>Opening and Closing</h3>", unsafe_allow_html=True)
    fig2 = go.Figure(data=[
        go.Bar(x=stock_data['Open'], y=stock_data['Close'], name='Open And Close', marker_color='blue'),
        # go.Bar(x=stock_data.index, y=stock_data['Close'], name='Close', marker_color='orange')
    ])
    fig2.update_layout(barmode='group', title_text='Opening and Closing')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>Summary</h3>", unsafe_allow_html=True)
    st.table(stock_data[['Open', 'Low', 'High', 'Close']].describe())

    st.markdown("<h3 style='text-align: center;'>Daily Lowest Price</h3>", unsafe_allow_html=True)
    fig3 = go.Figure(data=[
        go.Bar(x=stock_data['Low'], y=stock_data['Volume'], name='Low', marker_color='green')
    ])
    fig3.update_layout(title_text='Volume And Lowest Price')
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>Lowest And Closing Price</h3>", unsafe_allow_html=True)
    fig4 = make_subplots(specs=[[{"secondary_y": True}]])
    fig4.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Low'], name='Low', line=dict(color='green')), secondary_y=False)
    fig4.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Close', line=dict(color='orange')), secondary_y=False)
    fig4.update_layout(title_text='Lowest and Closing Price')
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>Open, High, Low, And Close Price</h3>", unsafe_allow_html=True)
    fig5 = make_subplots(specs=[[{"secondary_y": True}]])
    fig5.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], name='Open', line=dict(color='blue')), secondary_y=False)
    fig5.add_trace(go.Scatter(x=stock_data.index, y=stock_data['High'], name='High', line=dict(color='red')), secondary_y=False)
    fig5.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Low'], name='Low', line=dict(color='green')), secondary_y=False)
    fig5.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Close', line=dict(color='orange')), secondary_y=False)
    fig5.update_layout(title_text='Open, High, Low, and Close Price')
    st.plotly_chart(fig5, use_container_width=True)
    # st.experimental_rerun()
def show_login_popup():
    popup_html = """
    <script>
    function showPopup() {
        alert("Logged in successfully!");
    }
    window.onload = showPopup;
    </script>
    """
    st.components.v1.html(popup_html)

if __name__ == '__main__':
    main()
