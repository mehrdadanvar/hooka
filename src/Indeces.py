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

df = pd.DataFrame(questions_1, columns=["Questions On Cigarette and Hooka Smoking"])
df