import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from tableone import TableOne
import pandas as pd
import io

df = pd.read_csv("./snapshot_10.csv")


def get_summary(df,variable):
    counts = df[variable].value_counts()

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



st.html("<h1 >Patterns of Cigaret and Hooka Smoking in Southern Iran a Descriptive Cross-Sectional Study</h1>")
st.write("Authors: Gholamreza Abdollahifard, Mehrdad Anvar , ... ")
st.write("")
st.html("<p style='font-style: oblique;'> Affiliation: Shiraz University of Medical Sciences, Department of Community Medicine, Shiraz, Iran.</p>")


abstract = st.expander("Abstract", icon=":material/info:")
abstract.html("""<p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum magnam neque enim commodi esse atque corrupti,
      necessitatibus cum, voluptas odit inventore nihil autem tempore vero molestiae tenetur labore! Possimus, minima.
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum magnam neque enim commodi esse atque corrupti,
      necessitatibus cum, voluptas odit inventore nihil autem tempore vero molestiae tenetur labore! Possimus, minima.
    </p>""")

intro_container = st.container(border=False,key="intro")


intro_container.subheader("Introduction")
intro_container.write("Tobacco use, in its various forms, remains a significant global public health concern, contributing substantially to morbidity and mortality worldwide [Reference 1]. While cigarette smoking has been extensively studied, the prevalence and patterns of other tobacco products, such as hookah (waterpipe) smoking, are gaining increasing attention, particularly in regions of the Middle East and North Africa [Reference 2]. Hookah smoking, often perceived as less harmful than cigarette smoking, presents a unique set of health risks and social contexts that warrant thorough investigation [Reference 3]. Understanding the epidemiology of both cigarette and hookah smoking within specific populations is crucial for developing targeted public health interventions and informing tobacco control policies.")

intro_container.write("In Iran, while national tobacco control programs exist, regional variations in smoking behaviors and attitudes necessitate localized research. Southern Iran, with its distinct cultural and socio-economic characteristics, may exhibit unique patterns of tobacco use that have yet to be comprehensively elucidated. Investigating the prevalence, patterns, and associated factors of both cigarette and hookah smoking in this region is essential for understanding the local burden of tobacco use and informing culturally relevant prevention and cessation strategies. Furthermore, exploring the knowledge, attitudes, and cessation behaviors related to both smoking methods within this population can provide valuable insights for tailoring interventions.")

intro_container.write("To address this gap in knowledge, this descriptive epidemiological study was conducted to investigate the patterns of cigarette and hookah smoking among adult residents of Southern Iran. By employing a cross-sectional design and a comprehensive data collection strategy, this research aimed to provide a detailed characterization of smoking behaviors, knowledge, and attitudes towards tobacco use in this region. The findings of this study will contribute to a more nuanced understanding of the tobacco epidemic in Southern Iran and provide crucial data for public health planning and intervention development.")

intro_container.subheader("Materials & Methods")
with open("main.html", "r") as f:
    intro_container.html(f.read())




st.divider()
# 

# pop = st.popover("Button label")
# pop.checkbox("Show all")

# You can also use "with" notation:
st.subheader("3. Results")
st.html("<h3>3.1 Demographics</h3>")

desc_col1,desc_col2 = st.columns([2,2])

desc_col1.write("Over the course of the study period, starting from January 2021 to December 2021 a total number of 2110 individuals completed the questionnaire with a mean age of 39.8 years  (SD=13.3). Females accounted for 976 individuals (46.5%), while 53.5% of the participants were males. The education levels within the study population varied, with a substantial portion having attained a post-secondary degree. The largest group of participants, 756 individuals (36.1%), reported having a bachelor's degree or higher. This was followed by those with a college education, comprising 544 individuals (25.9%). A high school education was held by 490 participants (23.4%), while 307 individuals (14.6%) had limited education. ")
desc_col1.write("The occupational distribution of the study population was diverse. The largest single group was composed of housewifes, representing 516 individuals (24.6%). This was followed by self-employed participants, who accounted for 473 individuals (22.6%). Employees comprised 347 individuals (16.5%), and individuals classified as workers made up 271 (12.9%). The remaining participants were distributed among several other categories: 167 were retired (8.0%), 130 were university students (6.2%), 117 were unemployed (5.6%), and 76 were school students (3.6%).")


desc_col1.html("<h3>3.2 Prevalence and Predictors of Cigarette and Hookah Smoking</h3>")
desc_col1.write("Among the 2097 participants surveyed, 69% (n=1446) had never smoked, resulting in a 31% point prevalence of current tobacco use. A key finding was that the prevalence of regular hookah smoking (19.8%) was higher than that of regular cigarette smoking (11.2%). Univariate chi-square tests were performed to assess the relationship between various independent variables and current tobacco use. The results indicated a significant difference in smoking prevalence between genders, with men (40.4%) being significantly more likely to smoke than women (20.3%). The prevalence of smoking increased consistently from 19% in individual younger than 25 to 35.6% in the 45-55 year-old age bracket. This was followed by a decrease in the older age groups with participants >65 reaching a 27.8% prevalence of tobacco use. Participants' education level was noticeably associated with smoking status, where individuals with limited education reporting the highest rate of tobacco use (40.7%), while survey respondents with a bachelor's degree or higher reported a lower prevalence (17.3%). Similarly, the respondents' occupation was significantly associated with smoking status, where university and highschool students along with employees had the lowest prevalence () while workers ,self-employed  ,the unemployed and retired individuals reported the highest rates (36.8% respectively).")





desc_df = df[["age", "gender", "new_education","occupation","g_12_final_tobacco_use"]]
labels={"age":"Age","gender":"Gender","new_education":"Education","occupation":"Occupation"}
rename={"age":"Age","gender":"Gender","new_education":"Education","occupation":"Occupation"}
desc_table = TableOne(desc_df, dip_test=True,missing=False,continuous=["age"],labels=labels,htest=True,htest_name=True,rename=rename)
html_table =desc_table.to_html(classes=["MyTable"])
desc_col2.html(html_table)


    

    
    
table_vars = ['g_q1_public_indoor',
 'g_q2_public_outdoor',
 'g_q3_anti_smoking_ads',
 'g_q4_smoking_public_venues',
 'g_q5_accept_free_hookah',
 'g_q6_quit_difficulty',
 'g_q7_harmful_hookah_cigarettes',
 'g_q8_water_filter_harmless',
 'g_q9_flavor_reduce_harm',
 'g_q10_workplace_smoking_restrictions','g_12_final_tobacco_use']

att_df = df[table_vars]
att_table = TableOne(att_df,categorical=table_vars,missing=False,row_percent=True,groupby="g_12_final_tobacco_use",pval=True)
att_html_table =att_table.to_html(classes=["MyTable"])
desc_col2.html(att_html_table)




st.divider()
   



prev_tab, gender_tab ,age_tab ,edu_tab, occ_tab = st.tabs(["Prevalence by Usage Pattern", "Gender", "Age", "Education", "Occupation"])
with prev_tab:
    

    container = st.container(border=False)
    container.write("Of the 2097 participants surveyed, the majority (n=1121, 53.46%) reported never having smoked. Regular hookah use was the most prevalent pattern (n=416, 19.84%), followed by regular cigarette use (n=235, 11.21%). Occasional hookah use was observed in 219 participants (10.44%), while occasional cigarette use was reported by 106 individuals (5.05%). Overall, 46.54% of the respondents reported some form of current tobacco use.")
    labels={"g_12_final_tobacco_use":"Current Tobacco Use"}
    prev_table = TableOne(df,["g_12_final_tobacco_use"],categorical=["g_12_final_tobacco_use"],missing=False,labels=labels)
    html_table =prev_table.to_html(classes=["MyTable"])
    container.markdown("""
        <style>
        .MyTable {
        font-size: 12pt;
                       
        }

        .MyTable {
        border-top: 2px solid gray;
        border-bottom: 2px solid gray;
        border-left: 2px solid transparent;
        border-right: 2px solid transparent;
        }
        .MyTable thead {
        border-bottom: 2px solid gray;
        }
        

        .MyTable th, .MyTable td {
        border: 1px solid white;
        text-align: center;
        padding: 10px 10px;
        font-size: 12pt;
        font-style: normal;
        fot-weight: 20;
        }
        </style>
        """, unsafe_allow_html=True)
    container.html("<caption> Table 4-1 Prevalence of Current Tobacco Use</caption>")
    container.markdown(html_table, unsafe_allow_html=True)

with gender_tab:
    container = st.container(border=False)
    container.html("<p style='padding:20px 20px;'> Further analysis, as presented in Table 4-2, explored the prevalence of cigarette and hookah smoking by gender. Occasional and regular cigarette use was significantly more prevalent among men (8.7% and 19.1%, respectively) than women (0.9% and 2.2%). In contrast, the prevalence of occasional and regular hookah smoking was similar for both genders. Overall, men demonstrated a significantly higher likelihood of reporting current tobacco use compared to women.</p>")
    order = {"g_12_final_tobacco_use":["Occasional cigarette","Regular cigarette","Occasional hookah","Regular hookah"]}
    gender_table = TableOne(df,["gender"],categorical=["gender"], groupby="g_12_final_tobacco_use",missing=False,row_percent=True)
    container.markdown(gender_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)

with age_tab:
    container = st.container(border=False)
    # start = 9
    # max_age = df['age'].max()
    # end = int(np.ceil(max_age / 10.0) * 10) + 10  # ensure upper edge covers all ages
    # # bins = list(range(10, 70, 10)) + [70, df['age'].max() + 1]  # e.g., [10,20,30,...,70, max+1]
    # # labels = [f"{i}-{i+9}" for i in bins[:-1]]
    # # df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    # bins = [9, 20, 30, 65, np.inf]  # upper bounds are exclusive unless right=True
    # labels = ['9-19', '20-29', '30-64', '65+']
    # df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    # #order = {"g_q11_current_tobacco_use":["Occasional cigarette","Regular cigarette","Occasional hookah","Regular hookah"]}

    # age_table = TableOne(df,["age_group"],categorical=["age_group"], groupby="g_q11_current_tobacco_use",missing=False,row_percent=True)
    # container.markdown(age_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)

with edu_tab:
    container = st.container(border=False)

    order = {"g_q11_current_tobacco_use":["Occasional cigarette","Regular cigarette","Occasional hookah","Regular hookah"],"new_education":["Limited Education","High School", "College", "Bachelor's Degree and Higher"]}
    education_map = {
    "No Education": "Limited Education",
    "Literacy Movement": "Limited Education",
    "Elementary School": "Limited Education",
    "Middle School": "High School",
    "High School": "High School",
    "Technical School": "High School",  # optionally keep in High School
    
    "Pre-University": "College",
    "Diploma": "College",
    
    "Bachelor's Degree": "Bachelor's Degree and Higher",
    "Master's Degree": "Bachelor's Degree and Higher",
    "PhD and Higher": "Bachelor's Degree and Higher"
    }
    df['new_education'] = df['education'].map(education_map)
    labels={"new_education":"Education","g_q11_current_tobacco_use":"Current Tobacco Use"}


    edu_table = TableOne(df,["new_education"],categorical=["new_education"], groupby="g_12_final_tobacco_use",missing=False,row_percent=True,labels=labels,pval=True)
    container.markdown(edu_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)


with occ_tab:
    container = st.container(border=False)
    order = {"g_q11_current_tobacco_use":["Occasional cigarette","Regular cigarette","Occasional hookah","Regular hookah"],
             "occupation":["Worker","Unemployed","Self-Employed","Retired","Housewife","Employee","School Student","University Student"]}
    occ_table = TableOne(df,["occupation"],categorical=["occupation"], groupby="g_12_final_tobacco_use",missing=False,row_percent=True,labels=labels,pval=True)
    container.markdown(occ_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)

  















st.divider()

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


#st.markdown(att_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)
    # Rename the index
new_table = summary_table.rename(label_map,axis="index")
# st.html(new_table.to_html(classes=["myta"]))
st.table(new_table.style.set_table_styles([{"selector": "th", "props": [("max-width", "200px"), ("padding", "10px 15px")]},
                                           {"selector":"tbody", "props":[("max-width", "50%")]}]))
st.divider()














st.html("<h3>Associations Between Sociodemographic Factors, Attitudes, and Smoking Status</h3>")
st.write("The majority of the sample (53.5%) reported never having smoked, while regular hookah use (19.8%) was more prevalent than regular cigarette use (11.2%), and occasional hookah use (10.4%) was more common than occasional cigarette use (5.1%). Overall, nearly half of the respondents reported some form of current tobacco use.")
st.write("""
 Agreement with the prohibition of hookah smoking in both enclosed (χ 
2
 <0.001) and open public spaces (χ 
2
 <0.001) was significantly linked to smoking status, with those disagreeing showing a higher likelihood of being smokers. Exposure to anti-smoking advertisements in the past month was significantly associated with smoking status (χ 
2
 <0.001), as was the history of being offered free tobacco samples (χ 
2
 <0.001). The perceived difficulty of quitting tobacco use also showed a significant association with current smoking status (χ 
2
 <0.001), as did the perceived harmfulness of smoking (χ 
2
 <0.001). Furthermore, the belief that hookah flavor reduces harm was significantly associated with smoking status (χ 
2
 <0.001), and the presence of workplace smoking restrictions also demonstrated a significant association (χ 
2
 <0.001).The belief that water filtration makes hookah harmless (χ 
2
 =0.203) and whether smoking was allowed in public venues (χ 
2
 =0.566) did not show a statistically significant association with smoking status in this sample.
""")

formats = ["plain",'simple','github','grid','fancy_grid','pipe',
'orgtbl','jira','presto','psql','rst','mediawiki','moinmoin',
'youtrack','html','latex','latex_raw','latex_booktabs', 'textile']

labels={"gender":"Gender",
        "education":"Education",
        "occupation":"Occupation",
        "g_q1_public_indoor":"Public Indoor",
        "g_q2_public_outdoor":"Public Outdoor",
        "g_q3_anti_smoking_ads":"Anti-Smoking Ads Socail",
        "g_q4_smoking_public_venues":"Anti-Smoking Ads Sports",
        "g_q5_accept_free_hookah":"Accept Free Hookah",
        "g_q6_quit_difficulty":"Quit Difficulty",
        "g_q7_harmful_hookah_cigarettes":"Harmful Smoking",
        "g_q8_water_filter_harmless":"Water Filter Harmless",
        "g_q9_flavor_reduce_harm":"Flavor Reduces Harm",
        "g_q10_workplace_smoking_restrictions":"Workplace Smoking Restrictions",
        "g_q12_current_tobacco_use":"Current Tobacco Use",
        }
categorical =  g_cols
ThisTable = TableOne(df,categorical,categorical=categorical,groupby="g_q12_current_tobacco_use",rename=labels,dip_test=True,pval=True,row_percent=True,missing=False)





st.write(ThisTable)

st.divider()
st.subheader("Cigarette & Hooka Smoking Prevalence in Southern Iran")
st.subheader("Discussion & Conclusion")
st.html("<h2>Discussion & Conclusion</h2>")
mine = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})
mine.style \
  .format(precision=3, thousands=".", decimal=",") \
  .format_index(str.upper, axis=1) \
  .relabel_index(["row 1", "row 2"], axis=0)

st.table(mine)


def generate_apa_table(df: pd.DataFrame, column_name: str, table_number: int = 1, title: str = None) -> str:
    """
    Generates an APA style HTML table for a categorical variable in a pandas DataFrame,
    displaying frequencies and percentages.

    Args:
        df (pd.DataFrame): The input pandas DataFrame.
        column_name (str): The name of the categorical column to analyze.
        table_number (int): The table number for the APA style table. Defaults to 1.
        title (str, optional): The title of the table. If None, a default title is generated.

    Returns:
        str: An HTML string containing the APA formatted table.
    """
    if column_name not in df.columns:
        return f"<p style='color: red;'>Error: Column '{column_name}' not found in the DataFrame.</p>"

    # Ensure the column is treated as categorical for accurate counts
    # Convert to category type if it's not already, to handle potential mixed types gracefully
    try:
        df[column_name] = df[column_name].astype('category')
    except TypeError:
        # If conversion fails (e.g., column contains unhashable types), treat as object
        pass

    # Calculate frequencies and percentages
    counts = df[column_name].value_counts(dropna=False) # Include NaN as a category if present
    percentages = (counts / counts.sum() * 100).round(2)

    # Combine into a temporary DataFrame for easier formatting
    table_df = pd.DataFrame({
        'Frequency': counts,
        'Percentage': percentages
    })
    table_df.index.name = 'Category'

    # Add a total row
    total_frequency = table_df['Frequency'].sum()
    total_percentage = table_df['Percentage'].sum()
    # Adjust total percentage to 100.00 if rounding caused it to be slightly off
    if abs(total_percentage - 100.00) < 0.01:
        total_percentage = 100.00

    total_row = pd.DataFrame({
        'Frequency': [total_frequency],
        'Percentage': [total_percentage]
    }, index=['Total'])
    table_df = pd.concat([table_df, total_row])

    # --- HTML Table Formatting ---
    html_output = io.StringIO()

    # Overall container for APA style (font, margin)
    html_output.write(f"""
    <div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin-bottom: 1em;">
        <p style="margin: 0; font-weight: bold;">Table {table_number}</p>
        <p style="font-style: italic; margin: 0;">{title if title else f"Frequencies and Percentages for {column_name.replace('_', ' ').title()}"}</p>
        <table style="border-collapse: collapse; width: 50%; margin-top: 0.5em; border-bottom: 1px solid black;">
            <thead>
                <tr>
                    <th style="border-bottom: 1px solid black; padding: 8px; text-align: left;">Category</th>
                    <th style="border-bottom: 1px solid black; padding: 8px; text-align: right;">Frequency</th>
                    <th style="border-bottom: 1px solid black; padding: 8px; text-align: right;">Percentage</th>
                </tr>
            </thead>
            <tbody>
    """)

    # Data rows
    for index, row in table_df.iterrows():
        category_display = str(index) if pd.notna(index) else "Missing"
        freq_display = int(row['Frequency'])
        percent_display = f"{row['Percentage']:.2f}%"

        if index == 'Total':
            html_output.write(f"""
                <tr>
                    <td style="border-top: 1px solid black; padding: 8px; text-align: left; font-weight: bold;">{category_display}</td>
                    <td style="border-top: 1px solid black; padding: 8px; text-align: right; font-weight: bold;">{freq_display}</td>
                    <td style="border-top: 1px solid black; padding: 8px; text-align: right; font-weight: bold;">{percent_display}</td>
                </tr>
            """)
        else:
            html_output.write(f"""
                <tr>
                    <td style="padding: 8px; text-align: left;">{category_display}</td>
                    <td style="padding: 8px; text-align: right;">{freq_display}</td>
                    <td style="padding: 8px; text-align: right;">{percent_display}</td>
                </tr>
            """)

    html_output.write("""
            </tbody>
        </table>
    </div>
    """)

    return html_output.getvalue()

gender_table_html = generate_apa_table(df, 'new_education', table_number=1, title="Participant Gender Distribution")
# print(gender_table_html)
st.html(gender_table_html)