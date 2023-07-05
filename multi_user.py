import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="Venturesathi | Data Analytics Solutions",
    page_icon="Logo.jpg",
)

with open("Auth.css")as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

USER_CREDENTIALS = {
    'vikash': 'vikash@44',
    'venture': 'ventur!',
    'user': 'password'
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
    st.markdown("<h1 style='text-align: center; color: #000080;'>Reliance Stock Price Analysis</h1>", unsafe_allow_html=True)

    chart_data = yf.download(tickers='RELIANCE.NS', period='1d', interval='1m')

    col1, col2, col3 = st.columns([5, 5, 5])

    with col1:
        st.markdown("<h6 style='text-align: center;'>Open And Lowest Price</h6>", unsafe_allow_html=True)
        chart1 = st.line_chart(chart_data, x='Open', y='Low', width=600, height=300)

        st.markdown("<h6 style='text-align: center;'>Opening and Closing</h6>", unsafe_allow_html=True)
        chart2 = st.bar_chart(chart_data, x="Open", y="Close")

        st.markdown("<h6 style='text-align: center;'>Summary</h6>", unsafe_allow_html=True)
        st.table(chart_data[['Open', 'Low', 'High', 'Close']].describe())

    with col2:
        st.button("Refresh",on_click=refresh())
        st.markdown("<h6 style='text-align: center; color: #000000;'>Sample Data</h6>", unsafe_allow_html=True)
        st.table(chart_data[['Open', 'High', 'Adj Close', 'Low']].tail(18))

    with col3:
        st.markdown("<h6 style='text-align: center;'>Daily Lowest Price</h6>", unsafe_allow_html=True)
        chart3 = st.bar_chart(chart_data, x='High', y='Low', width=600, height=300)

        st.markdown("<h6 style='text-align: center;'>Lowest And Closing Price</h6>", unsafe_allow_html=True)
        chart4 = st.line_chart(chart_data, x="Low", y="Close")

        st.markdown("<h6 style='text-align: center;'>Open, High, Low, And Adj Close Price</h6>", unsafe_allow_html=True)
        chart5 = st.line_chart(chart_data[['Open', 'High', 'Low', 'Adj Close']].describe())

    st.button("Log Out", on_click=logout)

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

def logout():
    del st.session_state.logged_in
    show_logout_popup()

def show_logout_popup():
    popup_html = """
    <script>
    function showPopup() {
        alert("Logged out successfully!");
    }
    window.onload = showPopup;
    </script>
    """
    st.components.v1.html(popup_html)

def refresh():
    a = st.experimental_rerun
    return a

if __name__ == '__main__':
    main()
