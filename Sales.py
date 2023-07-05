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

# hide_streamlit_style = """
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         </style>
#     """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
    st.markdown("<h3 style='text-align: center;'>Manufacturer's Sales Dashboard</h3>", unsafe_allow_html=True)

    chart_data = pd.read_csv(r"C:\Users\VikashKumarChaudhary\Downloads\Sales.csv")
    
    with open("Filter.css")as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    

    col1, col2 = st.columns(2)
    
    with col1:
        selected_Year = st.selectbox("Select Year", chart_data['YEAR'].unique())

        filtered_data = filter_data(chart_data, selected_Year)

        # with st.expander("View Data"):
        #     st.dataframe(filtered_data)

    # st.date_input("Select Date Range",filtered_data['Date'])
    # start_date, end_date = date_range
    # filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (filtered_data['Date'] <= end_date)]
    with col1:
       
        st.subheader("Quaterly Sales")
        with st.expander("View"):
         st.markdown("<h6 style='text-align: center;'>Quaterly Sales</h6>", unsafe_allow_html=True)

         st.bar_chart(filtered_data, x = "QTR", y= "SALES")
        # st.metric(label ="Total Sales in selected Year", value = (filtered_data['SALES']).sum())
    with col1:
        st.subheader("Monthly Sales")
        with st.expander("View The Table"):
            st._arrow_line_chart(filtered_data, x = "MONTH", y =  "SALES")

    with col2:
        # st.metric(label ="Number of Items Sold", value = (filtered_data['QUANTITYORDERED']).sum())
        selected_Year = st.selectbox("Select Year", chart_data['QTR'].unique())

        # filtered_data = filter_data(chart_data, selected_Year)

      
        st.subheader("Status of Orders by Terriotory")
        
        with st.expander("View"):
            # st.metric(label ="Number of Items Sold", value = (filtered_data['QUANTITYORDERED']).sum())
            st.bar_chart(filtered_data, x='QUANTITYORDERED',y='MONTH')
        df1 = filtered_data.CUSTOMERNAME.value_counts()
        st.subheader("Top Revenue Generator Customers")
        with st.expander("See The Chart"):
            st.table(df1.head(9))
    
    with col2:
        st.subheader("Items sold per month")
        with st.expander("View the Table"):
            st.bar_chart(filtered_data, x = 'QUANTITYORDERED', y = 'MONTH')
        st.subheader("Top States Contributing in sales ")
        with st.expander("View"):
            st._arrow_line_chart(filtered_data, x = 'STATE', y = 'SALES')
    with col1:
        st.subheader("Most Saled Items")
        with st.expander("View"):
            st._arrow_bar_chart(filtered_data['PRODUCTLINE'].value_counts())
        st.subheader("Sales by Territory")
        with st.expander("View the chart"):
         st.bar_chart(filtered_data, x = 'TERRITORY', y = 'SALES')
        st.button("Log Out", on_click=logout)

def filter_data(chart_data, selected_Year):
    filtered_data = chart_data[chart_data['YEAR'] == selected_Year]

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
