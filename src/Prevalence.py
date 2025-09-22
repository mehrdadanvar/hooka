import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from tableone import TableOne
import pandas as pd
import io

st.markdown("""
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
        border-top: 2px solid gray;
        }
        

        .MyTable th, .MyTable td {
        border: 1px solid white;
        text-align: left;
        padding: 10px 10px;
        font-size:  11pt;
        font-style: normal;
        font-weight: 20;
        }
        </style>
        """, unsafe_allow_html=True)
df = pd.read_csv("./snapshot_10.csv")


def get_summary(df, variable):
    counts = df[variable].value_counts()

    percentages = (counts / len(df)) * 100

    summary_df = pd.DataFrame(
        {'Frequency': counts, 'Percentage': percentages.round(2)})

    total_row = pd.DataFrame(
        {'Frequency': [len(df)], 'Percentage': [100.00]}, index=['Total'])
    summary_df = pd.concat([summary_df, total_row])
    return summary_df


def cat_sum(series, category):
    # return series.value_counts()/len(series)*100
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

intro_container = st.container(border=False, key="intro")


intro_container.subheader("Introduction")
intro_container.write(
    "Despite an overall decrease in the worldwide smoking prevalence from 1990 to 2020, tobacco consumptions remains a public health concern in many countries contributing to significant burdens [1]. While high income countries have successfully incorporated policies and practices in reducing smoking, tobacco use in low to middle income nations claims significant lives. An analysis of the Global Burden of Disease, revealed an approximate smoking prevalence of 25 and 4.7 percent among Iranian men and women in 2020 ( 2.3% and 8.3% increase compared with 1990). While cigarette smoking has been extensively studied, the prevalence and patterns of other tobacco products, such as hookah (waterpipe) smoking, are gaining increasing attention, particularly in regions of the Middle East and North Africa [Reference 2]. Hookah smoking, often perceived as less harmful than cigarette smoking, presents a unique set of health risks and social contexts that warrant thorough investigation [Reference 3]. Understanding the epidemiology of both cigarette and hookah smoking within specific populations is crucial for developing targeted public health interventions and informing tobacco control policies.")

intro_container.write("In Iran, while national tobacco control programs exist, regional variations in smoking behaviors and attitudes necessitate localized research. Southern Iran, with its distinct cultural and socio-economic characteristics, may exhibit unique patterns of tobacco use that have yet to be comprehensively elucidated. Investigating the prevalence, patterns, and associated factors of both cigarette and hookah smoking in this region is essential for understanding the local burden of tobacco use and informing culturally relevant prevention and cessation strategies. Furthermore, exploring the knowledge, attitudes, and cessation behaviors related to both smoking methods within this population can provide valuable insights for tailoring interventions.")

intro_container.write("To address this gap in knowledge, this descriptive epidemiological study was conducted to investigate the patterns of cigarette and hookah smoking among adult residents of Southern Iran. ")

intro_container.subheader("Materials & Methods")
with open("main.html", "r") as f:
    intro_container.html(f.read())


st.divider()
#

# pop = st.popover("Button label")
# pop.checkbox("Show all")

# You can also use "with" notation:
st.subheader("3. Results")
st.html("<h3>3.1 Demographics & Public Perception of Tobacco Advertisements/Harm</h3>")

desc_col1, desc_col2 = st.columns([3, 2])

desc_col1.write("Over the course of the study period, starting from January 2021 to December 2021 a total number of 2110 individuals completed the questionnaire with a mean age of 39.8 years  (SD=13.3). Females accounted for 976 individuals (46.5%), while 53.5% of the participants were males. The education levels within the study population varied, with a substantial portion having attained a post-secondary degree. The largest group of participants, 756 individuals (36.1%), reported having a bachelor's degree or higher. This was followed by those with a college education, comprising 544 individuals (25.9%). A high school education was held by 490 participants (23.4%), while 307 individuals (14.6%) had limited education. ")
desc_col1.write("The occupational distribution of the study population was diverse. The largest single group was composed of housewifes, representing 516 individuals (24.6%). This was followed by self-employed participants, who accounted for 473 individuals (22.6%). Employees comprised 347 individuals (16.5%), and individuals classified as workers made up 271 (12.9%). The remaining participants were distributed among several other categories: 167 were retired (8.0%), 130 were university students (6.2%), 117 were unemployed (5.6%), and 76 were school students (3.6%).")
desc_col1.write("""A substantial majority of respondents (63%) expressed agreement with the prohibition of smoking in enclosed public spaces,
          while a slightly smaller but still considerable proportion (49%) concurred with similar restrictions in open public areas. 
         Exposure to anti-smoking advertisements in the media was prevalent for slightly under half the respondents (47%),
          contrasting with a significantly lower incidence of exposure to anti-tobacco messaging at sporting events (27%).
         Experiences with being offered complimentary tobacco products were reported by over a quarter of the participants (28%).
         Furthermore, a considerable segment of the surveyed population (56%) perceived quitting hookah or cigarettes as a difficult endeavor, and an overwhelming majority (82%) recognized the harmful nature of these products.
        Misconceptions regarding harm reduction were evident in a small fraction (7%) believing that water filtration renders hookah smoke harmless, and a similarly low percentage (6%) suggesting that flavorings mitigate the potential harm.
          Workplace smoking restrictions were reported by approximately half of the respondents (51%). 
""")

desc_col1.html(
    "<h3>3.2 Prevalence and Predictors of Cigarette and Hookah Smoking</h3>")
desc_col1.write("Among the 2097 participants surveyed, 69% (n=1446) had never smoked, resulting in a 31% point prevalence of current tobacco use. A key finding was that the prevalence of regular hookah smoking (19.8%) was higher than that of regular cigarette smoking (11.2%). Univariate chi-square tests were performed to assess the relationship between various independent variables and current tobacco use. The results indicated a significant difference in smoking prevalence between genders, with men (40.4%) being significantly more likely to smoke than women (20.3%). The prevalence of smoking increased consistently from 19% in individual younger than 25 to 35.6% in the 45-55 year-old age bracket. This was followed by a decrease in the older age groups with participants >65 reaching a 27.8% prevalence of tobacco use. Participants' education level was noticeably associated with smoking status, where individuals with limited education reporting the highest rate of tobacco use (40.7%), while survey respondents with a bachelor's degree or higher reported a lower prevalence (17.3%). Similarly, the respondents' occupation was significantly associated with smoking status, where university and highschool students along with employees had the lowest prevalence () while workers ,self-employed  ,the unemployed and retired individuals reported the highest rates (36.8% respectively).")
desc_col1.write("""
Agreement with the prohibition of smoking in both enclosed and open public spaces was linked to smoking status, with those disagreeing showing a higher likelihood of being smokers. Exposure to anti-smoking advertisements in the past month was reported more often in smokers, whereas non-smokers were more likely to be exposed to such advertisements at sporting events. Tobacco users were more likely to be offered free complimentary products. The perceived harmfulness of smoking was less evident among smokers as was the perceived difficulty of quitting tobacco products. The belief that water carries harm-reduction characteristics could not be linked to smoking status, however the belief that tobacco flavor reduces harm was noticeably more prevalent among smokers. Workplace smoking restrictions
""")


desc_df = df[["age", "gender", "new_education",
              "occupation", "g_q12_final_tobacco_use"]]
labels = {"age": "Age", "gender": "Gender",
          "new_education": "Education", "occupation": "Occupation"}
rename = {"age": "Age", "gender": "Gender", "new_education": "Education",
          "occupation": "Occupation", "g_q12_final_tobacco_use": "Current Tobacco Use"}
desc_table = TableOne(desc_df, dip_test=True, missing=False, continuous=[
                      "age"], labels=labels, htest=True, htest_name=True, rename=rename)
html_table = desc_table.to_html(classes=["MyTable"])
desc_col2.html(html_table)


table_vars = ["age_category", "gender","new_education","occupation",

              'g_q1_public_indoor',
              'g_q2_public_outdoor',
              'g_q3_anti_smoking_ads',
              'g_q4_smoking_public_venues',
              'g_q5_accept_free_hookah',
              'g_q6_quit_difficulty',
              'g_q7_harmful_hookah_cigarettes',
              'g_q8_water_filter_harmless',
              'g_q9_flavor_reduce_harm',
              'g_q10_workplace_smoking_restrictions', 'g_q12_final_tobacco_use']
renaming = {
    'gender': 'Gender',
    'age_category': 'Age',
    'new_education': 'Education',
    'occupation': 'Occupation',
    'g_q1_public_indoor': 'Agreement with Smoking Prohibition in Enclosed Spaces',
    'g_q2_public_outdoor': 'Agreement with Smoking Prohibition in Open Spaces',
    'g_q3_anti_smoking_ads': 'Exposure to Anti-Smoking Advertisements in Media',
    'g_q4_smoking_public_venues': 'Exposure to Anti-Tobacco Messages at Sporting Events',
    'g_q5_accept_free_hookah': 'Experience of Receiving Free Hookah or Cigarette',
    'g_q6_quit_difficulty': 'Perception of Difficulty in Quitting Smoking',
    'g_q7_harmful_hookah_cigarettes': 'Perception of Harm from Hookah or Cigarettes',
    'g_q8_water_filter_harmless': 'Belief in Water-Filtration Reducing Tobacco Harm',
    'g_q9_flavor_reduce_harm': 'Belief in Tobacco Flavor Reducing its Harm',
    'g_q10_workplace_smoking_restrictions': 'Workplace Smoking Restrictions',
    'g_q12_final_tobacco_use': 'Current Tobacco Use'
}

att_df = df[table_vars]
att_table = TableOne(att_df, categorical=table_vars.remove("g_q12_final_tobacco_use"), missing=False,
                     row_percent=True, groupby="g_q12_final_tobacco_use", pval=True, rename=renaming)
att_html_table = att_table.to_html(classes=["MyTable"])
st.html(att_html_table)


st.divider()


st.divider()










# st.write(ThisTable)

st.divider()
st.html("<h2>Discussion & Conclusion</h2>")


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
    # Include NaN as a category if present
    counts = df[column_name].value_counts(dropna=False)
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


gender_table_html = generate_apa_table(
    df, 'new_education', table_number=1, title="Participant Gender Distribution")
# print(gender_table_html)
st.html(gender_table_html)


st.divider()
st.html("<h2>References</h2>")

st.write("1- Dai X, Gakidou E, Lopez AD. Evolution of the global smoking epidemic over the past half century: strengthening the evidence base for policy action. Tob Control. 2022 Mar;31(2):129-137. doi: 10.1136/tobaccocontrol-2021-056535. PMID: 35241576. ")
st.write("2- GBD 2019 Tobacco Collaborators. Spatial, temporal, and demographic patterns in prevalence of smoking tobacco use and attributable disease burden in 204 countries and territories, 1990-2019: a systematic analysis from the Global Burden of Disease Study 2019. Lancet. 2021 Jun 19;397(10292):2337-2360. doi: 10.1016/S0140-6736(21)01169-7. Epub 2021 May 27. Erratum in: Lancet. 2021 Jun 19;397(10292):2336. doi: 10.1016/S0140-6736(21)01282-4. PMID: 34051883; PMCID: PMC8223261.")