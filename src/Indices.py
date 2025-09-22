from Prevalence import att_table
import streamlit as st
import pandas as pd
st.title("Indeces")


questions_1 = ["Do you agree with the law prohibiting hookah smoking in public places ('served' in enclosed spaces like cafes, restaurants, etc.)?",
               "Do you agree with the law prohibiting hookah smoking in public places ('served' in open spaces like parks, beaches, etc.)?",
               "In the past month, have you seen or heard any anti-smoking advertisements in the media (television, radio, social networks, etc.)?",
               "Over the past month, have you seen or heard any anti-tobacco messages at sporting events?",
               "Have you ever been offered a free hookah or cigarette by someone working in a tobacco shop or distribution center??",
               "Do you think it will be difficult for someone to quit if they start using hookah or cigarettes?",
               "Do you think using hookah or cigarettes is harmful?",
               "Do you think that passing hookah smoke through water makes it harmless?",
               "In your opinion, does the flavor or type of hookah (e.g., fruit flavors) reduce its harm if any?",
               "Are there any restrictions on smoking in your workplace?",
               "What best describes your current use of tobacco?"]

df = pd.DataFrame(questions_1, columns=[
                  "Questions On Cigarette and Hooka Smoking"])
df
att_html_table = att_table.to_html(classes=["MyTable"])

st.html(att_html_table)


st.divider()
g_cols = [col for col in df.columns if col.startswith(
    "g_") and "g_q11" not in col]
yes = df[g_cols].apply(lambda x: cat_sum(x, "Yes"))
no = df[g_cols].apply(lambda x: cat_sum(x, "No"))
null = df[g_cols].apply(lambda x: cat_sum(x, "Null"))
# axis=1 for column-wise concatenation
summary_table = pd.concat([yes, no, null], axis=1)
summary_table.columns = ['Yes', 'No', 'Null']

row_labels = ["Do you agree with the law prohibiting smoking in public places ('served' in enclosed spaces like cafes, restaurants, etc.)?",
              "Do you agree with the law prohibiting smoking in public places ('served' in open spaces like parks, beaches, etc.)?",
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


# st.markdown(att_table.to_html(classes=["MyTable"]), unsafe_allow_html=True)
# Rename the index
new_table = summary_table.rename(label_map, axis="index")
# st.html(new_table.to_html(classes=["myta"]))
st.table(new_table.style.set_table_styles([{"selector": "th", "props": [("max-width", "200px"), ("padding", "10px 15px")]},
                                           {"selector": "tbody", "props": [("max-width", "50%")]}]))







formats = ["plain", 'simple', 'github', 'grid', 'fancy_grid', 'pipe',
           'orgtbl', 'jira', 'presto', 'psql', 'rst', 'mediawiki', 'moinmoin',
           'youtrack', 'html', 'latex', 'latex_raw', 'latex_booktabs', 'textile']

labels = {"gender": "Gender",
          "education": "Education",
          "occupation": "Occupation",
          "g_q1_public_indoor": "Public Indoor",
          "g_q2_public_outdoor": "Public Outdoor",
          "g_q3_anti_smoking_ads": "Anti-Smoking Ads Socail",
          "g_q4_smoking_public_venues": "Anti-Smoking Ads Sports",
          "g_q5_accept_free_hookah": "Accept Free Hookah",
          "g_q6_quit_difficulty": "Quit Difficulty",
          "g_q7_harmful_hookah_cigarettes": "Harmful Smoking",
          "g_q8_water_filter_harmless": "Water Filter Harmless",
          "g_q9_flavor_reduce_harm": "Flavor Reduces Harm",
          "g_q10_workplace_smoking_restrictions": "Workplace Smoking Restrictions",
          "g_q12_current_tobacco_use": "Current Tobacco Use",
          }
categorical = g_cols
ThisTable = TableOne(df, categorical, categorical=categorical, groupby="g_q12_current_tobacco_use",
                     rename=labels, dip_test=True, pval=True, row_percent=True, missing=False)                                           
st.divider()