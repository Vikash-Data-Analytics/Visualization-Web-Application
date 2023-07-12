# import streamlit as st

# st.button("Stock Analysis",on_click= "https://")
# st.write("check out this [link](https://)")


# import streamlit as st

# with st.echo():
#     st.title("CAT")

#     st.markdown("[![Click me](Logo.png)](https://)")

#Importing the required Libraries.


import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Venturesathi | Data Analytics Products",
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




# col1, col2 = st.columns([3,3])
# with col1:
#     st.write("Stock Price Prediction")
#     st.subheader("Live Stock Price Analysis")
#     st.subheader("Sample Sales Dashboard")
#     st.subheader("Manufacturer's Sales")

with open("Services.css")as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

# with col2:
st.image("Logo.png",width=150)

# st.subheader("Venturesathi Business Services LLP")
st.markdown("<h2 style='text-align: center; color: #2c698d;'>Venturesathi Business Services LLP</h2>", unsafe_allow_html=True)

st.markdown("With a dream of creating revolution in Data Analytics and Management Reporting for small and mid-sized companies, we started our organization Venturesathi Business Services LLP in the year 2022. So far, we have two world class service delivery centres in Rourkela, Odisha, India, where we have more than 100 plus members working in different shifts. We strive to innovate and automate every processes which comes to our way. For that reason we have entered into multiple partnerships with technology providers and industry leaders.")

st.title(" ")

st.markdown("<h3 style = 'color: #ff9400;'>Our Data Analytics Services:</h3>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center;'>Our Data Analytics Services</h4>", unsafe_allow_html=True)
# st.title(" ")

col1, col2 = st.columns([5,5])
with col1:
    st.markdown("<h5>Descriptive Analytics:</h5>", unsafe_allow_html=True)
    # st.write("Descriptive Analytics")
    
    st.markdown("- Hidden Impactful Insights")
    st.markdown("- Historical Pattern Analysis")
    st.markdown("- Data Pre-Processing")
    st.markdown("- Data Visualization")

# st.markdown("<h4 style = 'text-align: center;'>Microsoft Power BI Dashboards Samples:</h4>", unsafe_allow_html=True)
# st.markdown("<h4>Microsoft Power BI Dashboards Samples:</h4>", unsafe_allow_html=True)



with col2:
    st.markdown("<h5>Predictive Analytics:</h5>", unsafe_allow_html=True)
    # st.write("Predictive Analytics")
    
    st.markdown("- Time - Series Forecasting")
    st.markdown("- AI Enabled Analytical Solutions")
    st.markdown("- Solutions Using Powerful Models Like Desicion Tree, Random Forest, Linear Regression, Logistic Regression, Long-short Memory(LSTM).")


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)



st.sidebar.subheader("Our In-House Developed Products")

st.sidebar.button('Live Stock Price Analysis', on_click=open_page, args=('https://stock-analysis-uf1g.onrender.com',))
st.sidebar.button('Stock Price Prediction', on_click=open_page, args=('https://venturesathi-data-analytics.onrender.com/',))
st.sidebar.button('Manufacturer Sales', on_click=open_page, args=('https://venturesathi-manufacturer-sales.onrender.com',))
st.sidebar.button('Sales Dashboard', on_click=open_page, args=('https://venturesathi-visualization-app.onrender.com',))

st.sidebar.subheader("Visualization Tools")

st.sidebar.markdown("- Microsoft Power BI")
st.sidebar.markdown("- Tableau")
st.sidebar.markdown("- Pentaho")
st.sidebar.markdown("- Looker(Google Studio)")


st.sidebar.subheader("Accepted Data Sources")

st.sidebar.markdown("- Excel, Google Sheets")
st.sidebar.markdown("- Database(MySQL)")
st.sidebar.markdown("- Any other Known Sources Of Data")
# st.sidebar.markdown("- <h4></h4>", unsafe_allow_html=True)
