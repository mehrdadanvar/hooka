import streamlit as st
import pandas as pd
st.title("this is he mappingps page")
st.write("lorem 100 ipsum ")
st.code("console.log('hello world')```")
questions_1 = ["Do you agree with the law prohibiting hookah smoking in public places ('served' in enclosed spaces like cafes, restaurants, etc.)?",
"Do you agree with the law prohibiting hookah smoking in public places ('served' in open spaces like parks, beaches, etc.)?",
"In the past month, have you seen or heard any anti-smoking advertisements in the media (television, radio, social networks, etc.)?",
"In the past month, on how many days did you see people smoking in public or sports venues?",
"If someone you know offers you a free hookah, would you accept it?",
"Do you think it will be difficult for someone to quit if they start using hookah or cigarettes?",
"Do you think using hookah or cigarettes is harmful?",
"Do you think that passing hookah smoke through water makes it harmless?",
"In your opinion, does the flavor or type of hookah (e.g., fruit flavors) reduce its harm if any?",
"Are there any restrictions on smoking in your workplace?",
"What type of tobacco product do you currently use?"]

df = pd.DataFrame(questions_1, columns=["Questions On Cigarette and Hooka Smoking"])
df