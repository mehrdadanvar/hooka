import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
df = pd.read_csv("snapshot_7.csv")
st.html("<h1>Patterns of Cigaret and Hooka Smoking in Southern Iran a Descriptive Cross-Sectional Study</h1>")
st.write("Authors: Gholamreza Abdollahifar, Mehrdad Anvar , ... ")
st.write("")
st.html("<p style='font-style: oblique;'> Affiliation: Shiraz University of Medical Sciences, Department of Community Medicine, Shiraz, Iran.</p>")


abstract = st.expander("Abstract", icon=":material/info:")
abstract.subheader("Abstract")
abstract.write("Inside the expander.")


st.subheader("Introduction")
st.write("Tobacco use, in its various forms, remains a significant global public health concern, contributing substantially to morbidity and mortality worldwide [Reference 1]. While cigarette smoking has been extensively studied, the prevalence and patterns of other tobacco products, such as hookah (waterpipe) smoking, are gaining increasing attention, particularly in regions of the Middle East and North Africa [Reference 2]. Hookah smoking, often perceived as less harmful than cigarette smoking, presents a unique set of health risks and social contexts that warrant thorough investigation [Reference 3]. Understanding the epidemiology of both cigarette and hookah smoking within specific populations is crucial for developing targeted public health interventions and informing tobacco control policies.")

st.write("In Iran, while national tobacco control programs exist, regional variations in smoking behaviors and attitudes necessitate localized research. Southern Iran, with its distinct cultural and socio-economic characteristics, may exhibit unique patterns of tobacco use that have yet to be comprehensively elucidated. Investigating the prevalence, patterns, and associated factors of both cigarette and hookah smoking in this region is essential for understanding the local burden of tobacco use and informing culturally relevant prevention and cessation strategies. Furthermore, exploring the knowledge, attitudes, and cessation behaviors related to both smoking methods within this population can provide valuable insights for tailoring interventions.")

st.write("To address this gap in knowledge, this descriptive epidemiological study was conducted to investigate the patterns of cigarette and hookah smoking among adult residents of Southern Iran. By employing a cross-sectional design and a comprehensive data collection strategy, this research aimed to provide a detailed characterization of smoking behaviors, knowledge, and attitudes towards tobacco use in this region. The findings of this study will contribute to a more nuanced understanding of the tobacco epidemic in Southern Iran and provide crucial data for public health planning and intervention development.")


st.divider()
st.subheader("Materials & Methods")
with open("sample.html", "r") as f:
    st.html(f.read())
# st.header("Materials & Methods")
# st.subheader("Study Design and Population")
# st.write("This descriptive epidemiological study employed a cross-sectional design to investigate the patterns of cigarette and hookah smoking within the population of Southern Iran. Data were collected using a combination of in-person surveys and an online questionnaire distribution strategy. The target population included adult residents of Southern Iran.")
# st.subheader("Data Collection")
# st.html("<p>here is th link <a href='/page_2'>another page</a> </p>")
# st.html("<ol> <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</li> <li>Ut enim ad minim veniam, quis nostrud exercitation ollamco laboris nisi ut aliquip ex ea commodo consequat.</li> </ol>")
# st.write("This study was conducted in 2019 in Southern Iran")
# st.html("<h1>title</h1>")
# st.html("<h2 style='background-color: gray ; border-radius: 10px; '>title</h2>")
# st.html("<h3>title</h3>")
# st.html("<h4>title</h4>")
# st.html("<h5>title</h5>")
# st.html("<h6>title</h6>")



st.divider()
# 

# pop = st.popover("Button label")
# pop.checkbox("Show all")

# You can also use "with" notation:
st.subheader("Results")
st.html("<h3>Descriptive Statistics</h3>")
st.write("Over the course of the study period, starting from January 2021 to December 2021 a total number of 2110 individuals completed the questionnair ")


# st.table(df["res_time_sec"].quantile([0.5,0.10,0.25, 0.5, 0.75,0.90, 0.95,0.99]))
# arr = df["age"]
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20,   alpha=0.50,range=(0,80), color="green",density=True)
# ax.set_xlabel("Response Time (sec)")
# ax.set_ylabel("Count")
# st.pyplot(fig)
# st.table(df["age"].describe())
# st.table(pd.DataFrame(df["age"].describe().apply(lambda x: f"{x:.1f}")).transpose())

# st.table(df.groupby("surveyor")["res_time_sec"].describe())
# st.write("lorem 100 ipsum ")
# st.subheader("lorem 100 ipsum ")
# st.header("lorem 100 ipsum ")
# st.caption("lorem 100 ipsum ")
tab1, tab2, tab3 = st.tabs(["Age", "Gender", "Occupation"])

with tab1:
    st.html("<h4>Age Chracterisitcs of the Study Population</h4>")
    st.write("The age distribution of the dataset, comprising 2,110 individuals, reveals a mean age of approximately 39.8 years with a standard deviation of 13.3 years, indicating a moderate spread around the average. Ages range from a minimum of 9 to a maximum of 80 years. The interquartile range (IQR), spanning from 30 to 49 years, contains the middle 50% of the ages, with the median age (50th percentile) being 38 years, slightly lower than the mean, suggesting a mild skew towards younger ages.")
    col1, col2 = st.columns(2)
    col1.table(df.age.describe())
    

    fig, ax = plt.subplots()
    ax.boxplot(df['age'])
    ax.set_title('Boxplot of Age')
    ax.set_ylabel('Age')

    col2.pyplot(fig)
    # arr = df["age"]
    # fig, ax = plt.subplots()
    # ax.hist(arr, bins=20,   alpha=0.50,range=(0,80), color="green",density=True)
    # ax.set_xlabel("Age (years)")
    # ax.set_ylabel("Count")
    # st.pyplot(fig)
    # ax.set_ylabel("Count")
    # st.pyplot(fig)
    
with tab2:
    st.html("<h4>Gender Chracterisitcs of the Study Population</h4>")
    st.write("The gender distribution within the dataset shows a slightly higher representation of males (مرد) with a count of 1,129 (53.5%), compared to females (زن) who account for 981(46.5%) individuals.")
    col3, col4 = st.columns(2)
    col3.table(df.gender.value_counts())
    

    gender_counts = df['gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Distribution of Gender')
    col4.pyplot(fig)
with tab3:
    st.html("<h4>Occupation Chracterisitcs of the Study Population</h4>")
    col5, col6 = st.columns(2)
    counts = df['occupation'].value_counts()

# Calculate percentages
    percentages = (counts / len(df)) * 100

# Create a summary DataFrame
    summary_df = pd.DataFrame({'Frequency': counts, 'Percentage': percentages.round(2)})

# Add a total row
    total_row = pd.DataFrame({'Frequency': [len(df)], 'Percentage': [100.00]}, index=['Total'])
    summary_df = pd.concat([summary_df, total_row])

# Display the table in Streamlit
    col5.table(summary_df)
    

    occupation_counts = df['occupation'].value_counts()
    fig, ax = plt.subplots()
    colors = ['#333333', '#4D4D4D', '#666666', '#808080', '#999999', '#B3B3B3', '#CCCCCC', '#E6E6E6']
    ax.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Distribution of Occupation')
    col6.pyplot(fig)
st.divider()
st.subheader("Discussion & Conclusion")
st.write("To be written")