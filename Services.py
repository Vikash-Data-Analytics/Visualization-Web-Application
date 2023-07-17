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
    page_title="Venturesathi Business Services LLP",
    page_icon="Logo.jpg",
    # layout = 'wide',
)

# streamlit_style = """
# 			<style>
# 			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

# 			html, body, [class*="css"]  {
# 			font-family: 'Roboto', sans-serif;
# 			}
# 			</style>
# 			"""
# st.markdown(streamlit_style, unsafe_allow_html=True)
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

st.markdown("At Venturesathi, we are more than just a data analytics company – we are a dynamic force revolutionizing the way businesses harness the power of data. We specialize in delivering State-of-the-art data analytics solutions that drive performance and profitability for our esteemed clients. With a proven track record of success, we have honed our expertise in Providing data-driven solutions across diverse industries. Our team of seasoned professionals possesses deep industry knowledge and technical proficiency, enabling us to tailor our Services to meet your unique business needs. Our commitment to quality is unwavering. As an ISO 9001:2015 certified organization, we adhere to stringent standards, Ensuring that every aspect of our service, solutions, and results meets the highest level of excellence. Partner with us to unlock the full potential of your data and gain a competitive edge in Today's data-centric world. Experience a Showcase of Our Data Analytics & visualization Capabilities Here!")

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




with col2:
    st.markdown("<h5>Predictive Analytics:</h5>", unsafe_allow_html=True)
    # st.write("Predictive Analytics")
    
    st.markdown("- Time - Series Forecasting")
    st.markdown("- AI Enabled Analytical Solutions")
    st.markdown("- Solutions Using Powerful Models Like Desicion Tree, Random Forest, Linear Regression, Logistic Regression, Long-short Term Memory(LSTM).")


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)



st.sidebar.subheader("Our In-House Developed Products")

st.sidebar.button('Live Stock Price Analysis', on_click=open_page, args=('https://stock-price-analysis.onrender.com',))
st.sidebar.button('Sales Dashboard', on_click=open_page, args=('https://venturesathi-visualization-web.onrender.com',))
st.sidebar.button('Stock Price Prediction', on_click=open_page, args=('https://venturesathi-stock-price-prediction.onrender.com',))
st.sidebar.button('Manufacturer Sales', on_click=open_page, args=('https://venturesathi-manufacturer-sales-dashboard.onrender.com',))
st.title("")
st.sidebar.subheader("Visualization Tools")

selection = st.sidebar.selectbox("Select the Tool to View the Sample",("Microsoft power BI", "Tableau", "Looker(Google Studio)"))

if selection == "Microsoft power BI":
    st.markdown("<h4>Microsoft Power BI Dashboards Sample:</h4>", unsafe_allow_html=True)
    st.image("sample_a.png")
    st.image("sample_d.png")

if selection == "Tableau":
    st.markdown("<h4>Tableau Dashboards Sample:</h4>", unsafe_allow_html=True)
    st.image("sample_c.png")

if selection == "Looker(Google Studio)":
    st.markdown("<h4>Google Looker Dashboards Sample:</h4>", unsafe_allow_html=True)
    st.image("sample_b.png")
    st.image("sample_f.png", width = 1040)




# st.sidebar.markdown("- Microsoft Power BI")
# st.sidebar.markdown("- Tableau")
# st.sidebar.markdown("- Pentaho")
# st.sidebar.markdown("- Looker(Google Studio)")


# st.sidebar.subheader("Accepted Data Sources")

# st.sidebar.markdown("- Excel, Google Sheets")
# st.sidebar.markdown("- Database(MySQL)")
# st.sidebar.markdown("- Any other Known Sources Of Data")
# # st.sidebar.markdown("- <h4></h4>", unsafe_allow_html=True)
