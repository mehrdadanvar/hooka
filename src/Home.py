import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
df = pd.read_csv("snapshot_8.csv")


def get_summary(df,varaible):
    counts = df[varaible].value_counts()

    percentages = (counts / len(df)) * 100

    summary_df = pd.DataFrame({'Frequency': counts, 'Percentage': percentages.round(2)})

    total_row = pd.DataFrame({'Frequency': [len(df)], 'Percentage': [100.00]}, index=['Total'])
    summary_df = pd.concat([summary_df, total_row])
    return summary_df

def cat_sum(series,category):
    #return series.value_counts()/len(series)*100
    count = series[series == category].count()
    total = len(series)
    if total > 0:
        percentage = (count / total) * 100
        return f"{count} ({percentage:.0f}%)"
    else:
        return "0(0%)"


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
st.html("<h3>Demographics</h3>")
st.write("Over the course of the study period, starting from January 2021 to December 2021 a total number of 2110 individuals completed the questionnair ")



tab1, tab2, tab3 ,tab4,tab5 = st.tabs(["Age", "Gender", "Occupation","Education","Province"])

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
    
    col5.table(get_summary(df,"occupation"))
    

    occupation_counts = df['occupation'].value_counts()
    fig, ax = plt.subplots()
    colors = ['#333333', '#4D4D4D', '#666666', '#808080', '#999999', '#B3B3B3', '#CCCCCC', '#E6E6E6']
    ax.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Distribution of Occupation')
    col6.pyplot(fig)
with tab4:
    st.html("<h4>Education Chracterisitcs of the Study Population</h4>")
    col7, col8 = st.columns(2)
    mine = get_summary(df,"education")
    col7.table(mine.style.format(precision=1).format_index(str.lower,axis=0)\
               .set_caption("Distribution of Education")\
               .set_table_styles([{"selector": "th", "props": "text-align: center"},
                                  {"selector": "td", "props": "text-align: center"},
                                  ]))
with tab5:
    st.html("<h4>Province Chracterisitcs of the Study Population</h4>")
    col9, col10 = st.columns(2)
    mine = get_summary(df,"province")
    col9.table(mine.style.format(precision=1).format_index(str.lower,axis=0)\
               .set_caption("Distribution of Province")\
               .set_table_styles([{"selector": "th", "props": "text-align: center"},
                                  {"selector": "td", "props": "text-align: center"},
                                  ]))

st.html("<h3>Descriptive Statistics of Public Perceptions and Attitudes Towards Tobacco and Hookah Use</h3>")

st.write("""A substantial majority of respondents (63%) expressed agreement with the prohibition of hookah smoking in enclosed public spaces,
          while a slightly smaller but still considerable proportion (49%) concurred with similar restrictions in open public areas. 
         Exposure to anti-smoking advertisements in the media was prevalent for slightly under half the respondents (47%),
          contrasting with a significantly lower incidence of exposure to anti-tobacco messaging at sporting events (27%).
         Experiences with being offered complimentary tobacco products were reported by over a quarter of the participants (28%).
         Furthermore, a considerable segment of the surveyed population (56%) perceived quitting hookah or cigarettes as a difficult endeavor, and an overwhelming majority (82%) recognized the harmful nature of these products.
        Misconceptions regarding harm reduction were evident in a small fraction (7%) believing that water filtration renders hookah smoke harmless, and a similarly low percentage (6%) suggesting that flavorings mitigate the potential harm.
          Workplace smoking restrictions were reported by approximately half of the respondents (51%). 
         Of the totall particiapants, 47 % responded with use of tobacco products either regularly or occasionally.""")
g_cols = [col for col in df.columns if col.startswith("g_") and "g_q11" not in col]
yes = df[g_cols].apply(lambda x:cat_sum(x, "Yes"))
no = df[g_cols].apply(lambda x:cat_sum(x, "No"))
null = df[g_cols].apply(lambda x:cat_sum(x, "Null"))
summary_table = pd.concat([yes, no, null], axis=1)  # axis=1 for column-wise concatenation
summary_table.columns = ['Yes', 'No', 'Null']

row_labels = ["Do you agree with the law prohibiting hookah smoking in public places ('served' in enclosed spaces like cafes, restaurants, etc.)?",
"Do you agree with the law prohibiting hookah smoking in public places ('served' in open spaces like parks, beaches, etc.)?",
"In the past month, have you seen or heard any anti-smoking advertisements in the media (television, radio, social networks, etc.)?",
"Over the past month, have you seen or heard any anti-tobacco messages at sporting events?",
"Have you ever been offered a free hookah or cigarette by someone working in a tobacco shop or distribution center??",
"Do you think it will be difficult for someone to quit if they start using hookah or cigarettes?",
"Do you think using hookah or cigarettes is harmful?",
"Do you think that passing hookah smoke through water makes it harmless?",
"In your opinion, does the flavor or type of hookah (e.g., fruit flavors) reduce its harm if any?",
"Are there any restrictions on smoking in your workplace?",
"Do you currently use any tobacco products (cigarettes or hookah)?"]

    # Create a dictionary to map old index to new labels
label_map = dict(zip(g_cols, row_labels))

    # Rename the index
new_table = summary_table.rename(label_map,axis="index")
st.table(new_table.style.set_table_styles([{"selector":"th","props":"max-width: 150px"}]))
st.divider()
st.subheader("Discussion & Conclusion")
st.write("To be written")