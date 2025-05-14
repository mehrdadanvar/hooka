

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
st.set_page_config(layout="wide")
def page_2():
    st.title("Page 2")



pg = st.navigation(["Home.py", "page_2.py","Data Preparation.py"])
pg.run()