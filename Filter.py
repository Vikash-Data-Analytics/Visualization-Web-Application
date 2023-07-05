import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(
    page_title="Venturesathi | Data Analytics Solutions",
    page_icon="Logo.jpg",
    # layout = 'wide',
)

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

USERNAME = 'vikash'
PASSWORD = 'vikash'

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
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            show_login_popup()
        else:
            st.error("Invalid username or password")

def render_authorized_content():
    st.markdown("<h3 style='text-align: center;'>Machine Utilization Dashboard</h3>", unsafe_allow_html=True)

    chart_data = pd.read_csv(r"C:\Users\VikashKumarChaudhary\Downloads\Machine_Data.csv", encoding='unicode_escape')
    
    with open("Filter.css")as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    

    col1, col2 = st.columns(2)
    
    with col1:
        selected_machine = st.selectbox("Select Machine", chart_data['ï»¿Machine'].unique())

        filtered_data = filter_data(chart_data, selected_machine)

        with st.expander("View Data"):
            st.dataframe(filtered_data)

    # st.date_input("Select Date Range",filtered_data['Date'])
    # start_date, end_date = date_range
    # filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (filtered_data['Date'] <= end_date)]
    with col1:
       
        st.subheader("Hours Run & Their Cost")
        with st.expander("View Chart"):
            st.bar_chart(filtered_data[['RunTime', 'Total_Expenses']])
        
      
        st.subheader("Summary")
        with st.expander("View The Summary"):
            st.bar_chart(filtered_data.describe())

        st.subheader("Summary of Runtime and Total Cost")
        with st.expander("See The Chart"):
            st.line_chart(filtered_data[['RunTime', 'Total_Expenses']])
    
    with col2:
        st.subheader("Day Wise Run Time of Machines")
        with st.expander("View the Table"):
            st.table(filtered_data[['Date', 'RunTime','Hourly_Cost']])
        st.subheader("Maintenance")
        with st.expander("View the chart"):
            st._arrow_bar_chart(filtered_data[['RunTime','Total_Lub']])
    st.button("Log Out", on_click=logout)

def filter_data(chart_data, selected_machine):
    filtered_data = chart_data[chart_data['ï»¿Machine'] == selected_machine]

    return filtered_data

def show_login_popup():
    st.write("Logged in successfully!")

def show_logout_popup():
    st.write("Logged out successfully!")

def logout():
    del st.session_state.logged_in
    show_logout_popup()

if __name__ == '__main__':
    main()
