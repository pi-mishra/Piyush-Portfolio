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

# Reading the content of the PDF file
with open("assets/Piyush Mishra Data Analyst.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Creating a download button with the fetched content
st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Piyush Mishra Resume.pdf",
        mime="application/pdf",
    )

st.write("""
        Dear Recruiter,
         """)
st.write("""
        
Greetings! Explore my portfolio to delve into the world of Piyush Mishra, a devoted data enthusiast fueled by a profound interest in the realms of data analysis and reporting. 
Let me share a brief narrative explaining why, as a BBA finance graduate, I've set my sights on the dynamic field of data analytics. During my tenure at a previous organization, I was tasked with analyzing my colleagues' performance and conducting an overall assessment of customer tickets.
Presenting these findings to my seniors sparked a genuine fascination for the field of data analytics. 
         
         """)

st.write("---")

st.markdown(
    """
    <div style="text-align:center;">
        <h3>Connect with me:</h3>
        <a href="https://www.linkedin.com/in/pi-mishra/" target="_blank">LinkedIn</a> |
        <span>piyushmishra898@gmail.com</span> |
        <span>6206224930</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

with st.container():
    selected = option_menu(
    menu_title = None,
    options = ['About','Projects'],
    icons= ['person','code-slash'],
    orientation= 'horizontal'
    )
if selected == 'About':
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.write('##')
            st.title("Experience")

            st.subheader("""
            Process Manager Data Analyst (Indiafilings)
            (Feb 2024 - Present, Navi-Mumbai)
                         
            • Data-Driven Process Optimization: Leveraged data analysis to identify and implement process improvements, leading to increased sales and improved customer service. Collaborated with cross-functional teams to streamline workflows and enhance operational efficiency.
                         
            • Actionable Insights: Analyzed sales, churn, and credit data to provide the CEO and business head with actionable insights. Developed data-driven recommendations to optimize sales strategies and improve customer retention.
                         
            •Technical Expertise: Proficient in SQL, Excel, and Tableau for data querying, manipulation, and visualization. Possesses a strong understanding of statistical analysis and data cleaning techniques.
                         
            • Effective Communication: Regularly presented data-driven reports and insights to the CEO and business head. Effectively communicated complex data findings to both technical and non-technical audiences.
            """)

            st.subheader("""
            Customer Success Associate (magicpin)
            (August 2021 - June 2022, Remote)
                         
             • Managed and coordinated a team of 40 members, achieving a notable 62.5% reduction in average ticket resolution time from 40 minutes to 15 minutes, leading to a substantial increase in customer satisfaction.
             
             • Utilized SQL and Excel to perform ACPT analysis, uncovering actionable insights that played a pivotal role in enhancing team productivity and efficiency.
             
             • Contributed actively to the creation of workflow and standard operating procedures for a newly established fashion department, resulting in streamlined operations and a 30% improvement in task completion time.
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
            
            Soft Skills: Leadership, Problem Solving, Effective Communication, Teamwork, Conict Resolution
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
                - Full Stack Data Science (Almabetter), Coursework completed certification pending
            """)
            st.write("---")


if selected == 'Projects':

    page_names = ["Sales Dashboard (PowerBi)", "Nike Sales Analysis (PowerBi)", "Real State Analysis (PowerBi)", "Rossmann Sales Prediction (Python)","HEALTH INSURANCE CROSS SELL PREDICTION (Python)" ,
                  "Netflix Dashboard (Tableau)"]

    st.sidebar.title("Projects")

    # Initialize session state if not already done
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = page_names[0]

    # Create buttons in the sidebar
    for page in page_names:
        if st.sidebar.button(page):
            st.session_state.selected_page = page

    # Display the selected page
    if st.session_state.selected_page:
        
        
        if st.session_state.selected_page == "Sales Dashboard (PowerBi)":
            power_bi_embed_code = """
            <iframe width="1024" height="612" 
            src="https://app.powerbi.com/view?r=eyJrIjoiM2I5MWFjYWUtZTk2My00YTI2LTg1YzktMjMzODE0MWFmZDZhIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
            frameborder="0" 
            allowFullScreen="true"></iframe>
            """
            st.markdown(power_bi_embed_code, unsafe_allow_html=True)

        elif st.session_state.selected_page == "Nike Sales Analysis (PowerBi)":
            power_bi_embed_code = """
            <iframe width="1024" height="612" 
            src="https://app.powerbi.com/view?r=eyJrIjoiMmVjYzhhNGQtODJlNi00MzlkLTgyMGQtOWFkZGRlNmRlYTFjIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
            frameborder="0" 
            allowFullScreen="true"></iframe>
            """
            st.markdown(power_bi_embed_code, unsafe_allow_html=True)

        elif st.session_state.selected_page == "Real State Analysis (PowerBi)":
            power_bi_embed_code = """
            <iframe width="1024" height="612" 
            src="https://app.powerbi.com/view?r=eyJrIjoiYWQ4ZDNhMjUtNzAyMy00YmQ1LWE5NjUtNGFmMzAzMzRmYWJlIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" 
            frameborder="0" allowFullScreen="true"></iframe>
            """
            st.markdown(power_bi_embed_code, unsafe_allow_html=True)

        elif st.session_state.selected_page == "Rossmann Sales Prediction (Python)":
            st.subheader("""Rossmann-Sales-Prediction (Python)""")
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
        
        elif st.session_state.selected_page == "HEALTH INSURANCE CROSS SELL PREDICTION (Python)":
            st.subheader("""HEALTH INSURANCE CROSS SELL PREDICTION (Python)""")
            st.markdown("[Link to HEALTH INSURANCE CROSS SELL PREDICTION Classification GitHub Repo](https://github.com/pi-mishra/HEALTH-INSURANCE-CROSS-SELL-PREDICTION)")
            st.write("""
                    Summary
                    The dataset used for this analysis contains 381109 rows and 12 columns, consisting of 6 integer, 3 object, and 3 float columns. The data has no null or duplicate values. The mean age of the individuals in the dataset is approximately 38 years, the average annual premium is around 30564, and the average vintage (i.e., number of days that the customer has been associated with the company) is around 154 days. There is a significant amount of variation in the data, as indicated by the standard deviation. The age of the individuals ranges from 20 to 85 years, the annual premium ranges from 2630 to 540165, and the vintage ranges from 10 to 299 days.
                    The maximum age of the individuals surveyed was 85 years old, and all of these respondents indicated that they were not interested in purchasing health insurance. As the age of the respondents increased, their level of interest in purchasing health insurance decreased. Both male and female respondents had the same minimum and maximum age ranges. However, there were more females with driving licenses compared to males. There are more male customers than female customers who have health insurance, indicating that males are more likely to purchase health insurance. Customers with a driving license are more inclined to consider purchasing health insurance, while those who were previously insured may not necessarily do so. Customers with vehicles aged between 1-2 years are more likely to buy health insurance, while those who have experienced vehicle damage are also more inclined to purchase insurance due to the associated maintenance costs.
                    Channel 152.0 appears to outperform other channels in terms of policy sales, although the meaning of policy channel codes is unknown. Customers aged between 38 to 50 are more likely to respond to insurance sales, while those aged between 20 to 30 are less likely to do so. 45.8% of customers have been previously insured, and only 12.3% of customers have shown interest in purchasing health insurance. Age and policy sales channels appear to be highly correlated, and there are outliers in the annual premium data.
                    After addressing the presence of outliers using the interquartile range method and multicollinearity using the variance inflation factor method, the data was split into training and testing sets. The Synthetic Minority Over-sampling Technique (SMOTE) was used to balance the dataset. A decision tree model performed the best out of all the models evaluated, with a training accuracy of 0.986 and a validation accuracy of 0.876, indicating that it is able to generalize well to unseen data. Logistic regression also performed well, with a validation accuracy of around 0.80, but not as well as the decision tree model. Hyperparameter tuning using random search and grid search did not lead to significant improvements in performance for any of the models.
                    In conclusion, based on the evaluation of the models, the decision tree model may be recommended for this project as it provides a high level of accuracy and is able to generalize well. However, further analysis and evaluation may be necessary to determine the best model for this specific project.
                    """)
            
        elif st.session_state.selected_page == "Netflix Dashboard (Tableau)":
            tableau_embed_code = """
            <div class='tableauPlaceholder' id='viz1718117309958' style='position: relative'>
                <noscript>
                    <a href='#'>
                        <img alt='Netflix ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;NetflixmovieandTVseriesdashboard&#47;Netflix&#47;1_rss.png' style='border: none' />
                    </a>
                </noscript>
                <object class='tableauViz' style='display:none;'>
                    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                    <param name='embed_code_version' value='3' />
                    <param name='site_root' value='' />
                    <param name='name' value='NetflixmovieandTVseriesdashboard&#47;Netflix' />
                    <param name='tabs' value='no' />
                    <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;NetflixmovieandTVseriesdashboard&#47;Netflix&#47;1.png' />
                    <param name='animate_transition' value='yes' />
                    <param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' />
                    <param name='display_overlay' value='yes' />
                    <param name='display_count' value='yes' />
                    <param name='language' value='en-US' />
                </object>
            </div>
            <script type='text/javascript'>
                var divElement = document.getElementById('viz1718117309958');
                var vizElement = divElement.getElementsByTagName('object')[0];
                if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1400px';vizElement.style.height='827px';} 
                else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1400px';vizElement.style.height='827px';} 
                else { vizElement.style.width='100%';vizElement.style.height='2277px';} 
                var scriptElement = document.createElement('script');
                scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
                vizElement.parentNode.insertBefore(scriptElement, vizElement);
            </script>
            """

            st.components.v1.html(tableau_embed_code, height=850, scrolling=True)

        else:
            st.write("No page selected")
