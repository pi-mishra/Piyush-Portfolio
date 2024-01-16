import streamlit as st 
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(layout='wide') # setting the page layout
#funtion to get the image using url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json
lottie_coder = load_lottieurl("https://lottie.host/9727f156-7507-47cf-b17d-0685fa50ad0e/UbL6kaZfMT.json") #code returns a image
st.write("##") #gives space
#align the heading to center
st.markdown(
    """
    <div style="text-align:center;">
        <h1>PIYUSH MISHRA</h1>
    </div>
    """,
    unsafe_allow_html=True
)
# creating a button in center to download resume
st.markdown("""
<style>
.stDownloadButton button {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)
# GitHub URL of the PDF file
#github_pdf_url = "https://github.com/pi-mishra/portfolio/raw/main/Piyush%20Mishra%20Resume.pdf"
# Fetching the content of the PDF file
#pdf_content = requests.get(github_pdf_url).content
# Creating a download button with the fetched content
# st.download_button('Download Resume', pdf_content, key='resume_download')
# Local path to the PDF file
local_pdf_path = "E:/Portfolio Website/Piyush Mishra Resume.pdf"
# Reading the content of the PDF file
with open(local_pdf_path, "rb") as pdf_file:
    pdf_content = pdf_file.read()
# Creating a download button with the fetched content
st.download_button('Download Resume', pdf_content, key='resume_download',file_name='Piyush_Mishra_Resume.pdf')
st.write("""
        Dear Requiter,
         """)
st.write("""
        Welcome to my portfolio! I am Piyush Mishra, a passionate data enthusiast with a keen interest in the field of data analysis and reporting. Below, you'll find additional information crucial for understanding my capabilities as a data analyst.
        """)
st.write("---")
with st.container():
    selected = option_menu(
    menu_title = None,
    options = ['About','Projects','Powerbi','Contact'],
    icons= ['person','code-slash','chat-left-text-fill'],
    orientation= 'horizontal'
    )
if selected == 'About':
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.write('##')
            st.title("Experience")
            st.subheader("""
            Customer Success Associate (magicpin)
            (August 2021 - June 2022, Remote)
                         
             • Managed and coordinated a team of 40 members, achieving a notable 62.5% reduction in average ticket resolution time from 40 minutes to 15 minutes, leading to a substantial increase in customer satisfaction.
             
             • Utilized SQL and Excel to perform ACPT analysis, uncovering actionable insights that played a pivotal role in enhancing team productivity and efficiency.
             
             • Contributed actively to the creation of workow and standard operating procedures for a newly established fashion department, resulting in streamlined operations and a 30% improvement in task completion time.
            """)
            st.subheader("""
            Business Development Associate (Inpravia Global)
            (November 2020 - July 2021, Remote)
                         
            • Client relationship development and management, resulting in increased sales up to 6%.
                         
            • Strategic formulation of online marketing approaches for product and service promotions.
                         
            • Proven track record of fostering client connections to drive successful business outcome.
            """)
        with col2:
            st_lottie(lottie_coder())
        st.write("---")
    with st.container():
        st.subheader(
            """
            Skills -

            Areas of Interest: Data Cleaning, Data Visualization, Business Analysis, Forcasting

            Technical Skills: Python, SQL, Power Bi, DAX, Google Sheets, Excel, Tableau, Scikit-Learn, NumPy, Pandas, Matplotlib, Seaborn
            
            Soft Skills: Leadership, Problem Solving, E|ective Communication, Teamwork, Conict Resolution
            """
        )
        st.write("---")
    with st.container():
        col3 = st.columns(1)
        with col3[0]:
            st.subheader("""
            Education and Certification
                - B.B.A. Finance (Ranchi college)
                - Predictive analytics IIM Banglore
                - Analyzing and Visualizing Data with Microsoft Power BI (PWC)
                - Data Analytics Consulting (KPMG)
                - Full Stack Data Science (Almabetter)
            """)
if selected == 'Powerbi':
    with st.container():
        col7 =st.columns(1)
        with col7[0]:
            power_bi_embed_code = """
            <iframe width="1024" height="612" 
            src="https://app.powerbi.com/view?r=eyJrIjoiM2I5MWFjYWUtZTk2My00YTI2LTg1YzktMjMzODE0MWFmZDZhIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
            frameborder="0" 
            allowFullScreen="true"></iframe>
            """
            st.markdown(power_bi_embed_code, unsafe_allow_html=True)
    with st.container():
        col8 =st.columns(1)       
        with col8[0]:
            power_bi_embed_code = """
            <iframe width="1024" height="612" 
            src="https://app.powerbi.com/view?r=eyJrIjoiMmVjYzhhNGQtODJlNi00MzlkLTgyMGQtOWFkZGRlNmRlYTFjIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
            frameborder="0" 
            allowFullScreen="true"></iframe>
            """
            st.markdown(power_bi_embed_code, unsafe_allow_html=True)
if selected == "Projects":
    st.subheader("""Rossmann-Sales-Prediction (Capstone project)""")
    st.markdown("[Link to Rossmann Sales Prediction Regression GitHub Repo](https://github.com/pi-mishra/Rossmann-Sales-Prediction-Regression-)")
    st.write("""
Summary
This project involved merging two datasets into one dataframe called all_store, which had 1017209 rows and 18 columns. The dataframe consisted of int, object, and float datatypes, and object datatypes were later converted to int. There were no duplicate values, but six columns had null values that needed to be treated.
To better understand the data the year, month, and day from the "date" column were extracted and then dropped. The "Open" column was also dropped since no sales occurred when stores were closed. Furthermore, 49% of data was missing from columns "Promo2SinceWeek," "Promo2SinceYear," and "PromoInterval," so they were dropped. Considering date as categories we have filled ‘CompetitionOpenSinceMonth’ and 'CompetitionOpenSinceYear' with mode. Considering there is no competition or the competion is so far that there is no account of the data, so filling null values with 0.
The most common type of store was "a" with 551,627, followed by "d" with 312,912, "c" with 136,840, and "b" with 15,830. It was discovered that store type and sales were correlated, with more stores leading to more sales. Monday had the highest number of sales, followed by Tuesday, Friday, Wednesday, Thursday, Saturday, and Sunday. Similarly, average sales for different days of the week followed the same trend. Store B had higher average sales than other stores C, A, and D, respectively. Monthly sales over the year increased, with an increase in the number of stores leading to more customers' visits and higher sales. Sales data were right-skewed, and 17% of stores were affected by the closure of public schools. No promos were run on Saturday and Sunday, and sales increased when the promo was used.
It was observed that the "CompetitionDistance" column had a large positive skewness of 2.93, indicating a heavily skewed right-tailed distribution. On the other hand, "Sales" had a small positive skewness of 0.64, indicating a slightly skewed right-tailed distribution, while "Customers" had a moderate positive skewness of 1.60, indicating a skewed right-tailed distribution.
To remove outliers the IQR method was used and then one-hot encoding was performed. The data were then scaled using MinMaxScaler.
Conclusion was made that the decision tree and XG boost models outperformed linear, ridge, and lasso regression models in predicting sales of Rossman stores. The decision tree model achieved an R2 score of 0.973 and a low RMSE of 538, while the XG boost model achieved an R2 score of 0.926 and a relatively low RMSE of 849. In contrast, the linear, ridge, and lasso regression models achieved similar R2 scores of around 0.893, with higher RMSE values ranging from 1021 to 1022. The decision tree and XG boost models are more accurate and may be more robust to non-linear relationships in the data, making them the preferred models for predicting sales of Rossman stores.

                 """)
    st.subheader("""HEALTH INSURANCE CROSS SELL PREDICTION""")
    st.markdown("[Link to HEALTH INSURANCE CROSS SELL PREDICTION Classification GitHub Repo](https://github.com/pi-mishra/HEALTH-INSURANCE-CROSS-SELL-PREDICTION)")
    st.write("""
Summary
The dataset used for this analysis contains 381109 rows and 12 columns, consisting of 6 integer, 3 object, and 3 float columns. The data has no null or duplicate values. The mean age of the individuals in the dataset is approximately 38 years, the average annual premium is around 30564, and the average vintage (i.e., number of days that the customer has been associated with the company) is around 154 days. There is a significant amount of variation in the data, as indicated by the standard deviation. The age of the individuals ranges from 20 to 85 years, the annual premium ranges from 2630 to 540165, and the vintage ranges from 10 to 299 days.
The maximum age of the individuals surveyed was 85 years old, and all of these respondents indicated that they were not interested in purchasing health insurance. As the age of the respondents increased, their level of interest in purchasing health insurance decreased. Both male and female respondents had the same minimum and maximum age ranges. However, there were more females with driving licenses compared to males. There are more male customers than female customers who have health insurance, indicating that males are more likely to purchase health insurance. Customers with a driving license are more inclined to consider purchasing health insurance, while those who were previously insured may not necessarily do so. Customers with vehicles aged between 1-2 years are more likely to buy health insurance, while those who have experienced vehicle damage are also more inclined to purchase insurance due to the associated maintenance costs.
Channel 152.0 appears to outperform other channels in terms of policy sales, although the meaning of policy channel codes is unknown. Customers aged between 38 to 50 are more likely to respond to insurance sales, while those aged between 20 to 30 are less likely to do so. 45.8% of customers have been previously insured, and only 12.3% of customers have shown interest in purchasing health insurance. Age and policy sales channels appear to be highly correlated, and there are outliers in the annual premium data.
After addressing the presence of outliers using the interquartile range method and multicollinearity using the variance inflation factor method, the data was split into training and testing sets. The Synthetic Minority Over-sampling Technique (SMOTE) was used to balance the dataset. A decision tree model performed the best out of all the models evaluated, with a training accuracy of 0.986 and a validation accuracy of 0.876, indicating that it is able to generalize well to unseen data. Logistic regression also performed well, with a validation accuracy of around 0.80, but not as well as the decision tree model. Hyperparameter tuning using random search and grid search did not lead to significant improvements in performance for any of the models.
In conclusion, based on the evaluation of the models, the decision tree model may be recommended for this project as it provides a high level of accuracy and is able to generalize well. However, further analysis and evaluation may be necessary to determine the best model for this specific project.
                 """)
if selected == "Contact":
    st.subheader("""Contacts""")
    st.write("Email ID - piyushmishra898@gmail.com")
    st.write("Connect on call or whatsapp - 6206224930")
    st.markdown("[Click to connect on LinkedIn](https://www.linkedin.com/in/pi-mishra/)")