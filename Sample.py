import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from streamlit_card import card
st.set_page_config(
    page_title="Venturesathi | Analytical Solutions",
    page_icon="Logo.jpg",
    # layout="wide",
)
    # st.markdown("<h1 style='text-align: center; color: #000080;'>ABC Enterprises Sales Dashboard</h1>", unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center; color: #402090;'>Venturesathi Analytical Solutions</h1>", unsafe_allow_html=True)
# st.image('Logo.jpg',width=300)
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

USERNAME = 'admin'
PASSWORD = 'password'

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
    password = st.text_input("Password",type="password")
    login_button = st.button("Login")

    if login_button:
      
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            show_login_popup()
            st.experimental_rerun()  
        else:
            st.error("Invalid username or password")
            st.image("images.jpg")

def render_authorized_content():
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        title {visibility: hidden}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #000080;'>ABC Enterprises Sales Dashboard</h1>", unsafe_allow_html=True)

    col1, col2, col3  = st.columns([5,5,5])
    chart_data = pd.read_csv(r"C:\\Users\\VikashKumarChaudhary\Downloads\\US  E-commerce records 2020.csv",encoding= 'unicode_escape')

    with open("Vis.css")as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    col1.metric(label ="Total Sales", value = (chart_data['Sales']).sum())

    col2.metric(label ="Total Discount", value = (chart_data['Discount']).sum())

    col3.metric(label ="Total Profit", value = (chart_data['Profit'].sum()))

# col3.metric(label = "Total Quantity Sold", value = (chart_data['Quantity'].sum()))

# col2.metric(label= "Shipping Modes", value = (chart_data['Ship Mode'].value_counts()))


    with col1:
        st.markdown("<h6 style='text-align: center;'>Profit Day wise</h6>", unsafe_allow_html=True)

        st.line_chart(chart_data, x = 'Order Date', y ='Profit', width = 600, height= 300)

   
        st.markdown("<h6 style='text-align: center;'>Category Wise Sales</h6>", unsafe_allow_html=True)

        st.bar_chart(chart_data, x = "Category", y= "Sales")

        st.markdown("<h6 style='text-align: center;'>Summary</h6>", unsafe_allow_html=True)
        st.table(chart_data[['Sales','Quantity','Discount','Profit']].describe())

    with col2:
            st.markdown("<h6 style='text-align: center; color: #000000;'>Sample Data[Day,Sales]</h6>", unsafe_allow_html=True)
            st.table(chart_data[['Day','Sales']].head(32))

       
    with col3: 
        st.markdown("<h6 style='text-align: center;'>Discounts Based On Quantity</h6>", unsafe_allow_html=True)
        st.bar_chart(chart_data, x= 'Quantity', y= 'Discount', width = 600, height= 300)


        st.markdown("<h6 style='text-align: center;'>State wise Sales</h6>", unsafe_allow_html=True)
        st.line_chart(chart_data, x = "State", y = "Sales")

        st.markdown("<h6 style='text-align: center;'>Sales and Quantity Trend</h6>", unsafe_allow_html=True)
        st.line_chart(chart_data[['Sales','Quantity']].describe())
        # st.write("Welcome to the authorized area!")

    logout_button = st.button("Log Out")

    if logout_button:
        show_logout_popup()
        del st.session_state.logged_in  
        st.experimental_rerun()  
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

def show_logout_popup():
    popu_html = """
    <script>
    function showPopup() {
    alert("Logged out successfully!");
     }
    window.onload = showPopup;
    </script>
    """
    st.components.v1.html(popu_html)
if __name__ == '__main__':
    main()
