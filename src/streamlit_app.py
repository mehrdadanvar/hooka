

import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import datetime
st.set_page_config(layout="wide")
def page_2():
    st.title("sample")



pg = st.navigation(["Prevalence.py", "Cigarette_Smokers.py", "Hookah_Smokers.py","Indices.py"])
pg.run()