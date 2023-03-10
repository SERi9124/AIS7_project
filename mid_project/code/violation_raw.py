import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Traffic Accident data analysis",
    page_icon="π",
    layout="wide",
)

st.markdown("# π κ΅ν΅μ¬κ³  μμΈ λΆμ π")
st.sidebar.markdown("# π κ΅ν΅μ¬κ³  μμΈ λΆμ π")

st.sidebar.header('λ²κ·μλ°μΌλ‘ μΈν κ΅ν΅μ¬κ³ ')
st.sidebar.markdown("""
    ### λͺ©μ°¨
    1. κ°μ€ μΈμ°κΈ°
    2. λ°μ΄ν° μκ°ν
    3. μκ°ν ν κ²°κ³Όλ‘ λΆμ
    4. κ°μ€ κ²μ¦
""")

st.markdown("""
    ## λ²κ·μλ°νΈ
    ### κ°μ€   
        1. μ±κ²©μ΄ κΈν νκ΅­μΈμ νΉμ±μ κ³ λ €νμ¬ μ νΈμλ°μ μ¬κ³ κ° κ°μ₯ λ§μ κ²μ΄λ€.       
        2. μΌκ°μλ μ°¨κ° λ§μ§ μμ μ νΈλ₯Ό λ¬΄μνλ μ¬λλ€μ΄ λ§μ κ²μ΄λ€. 
""")

# λ°μ΄ν° λΆλ¬μ€κΈ°
url = "https://github.com/meji9086/Traffic-Accident-Data-Analysis/raw/master/data/violation_raw_data.txt"
@st.cache
def load_data(url):
   df = pd.read_table(url, sep='\t')
   return df

data_load_state = st.text('Loading data...')
df = load_data(url)
data_load_state.text("Success! (using st.cache)")

# μ¬μ©ν  λ°μ΄ν°
## μ νλ³
df_ac = df.loc[df['μ ν']=='μ¬κ³ κ±΄μ']
df_in = df.loc[df['μ ν']=='λΆμμμ']
df_de = df.loc[df['μ ν']=='μ¬λ§μμ']
df_al = df.pivot_table(index='μ', columns='μ ν', values='μ¬κ³ μ')

## λ²κ·μλ°λ³
df_r = df_ac.pivot_table(index='λ²κ·μλ°μ ν', values='μ¬κ³ μ', 
                aggfunc='sum').sort_values(by='μ¬κ³ μ', ascending=False)
df_r2 = df_in.pivot_table(index='λ²κ·μλ°μ ν', values='μ¬κ³ μ',
                aggfunc='sum').sort_values(by='μ¬κ³ μ', ascending=False)
df_r3 = df_de.pivot_table(index='λ²κ·μλ°μ ν', values='μ¬κ³ μ', 
                aggfunc='sum').sort_values(by='μ¬κ³ μ', ascending=False)
df_al2 = df.pivot_table(index='λ²κ·μλ°μ ν', columns='μ ν', values='μ¬κ³ μ')

## μ£ΌμΌλ³
df_d = df.pivot_table(index='μ£ΌμΌ', columns='μ ν', values='μ¬κ³ μ')
df_d1 = df_ac.pivot_table(index='μ£ΌμΌ', columns='λ²κ·μλ°μ ν', values='μ¬κ³ μ')
df_d2 = df_in.pivot_table(index='μ£ΌμΌ', columns='λ²κ·μλ°μ ν', values='μ¬κ³ μ')
df_d3 = df_de.pivot_table(index='μ£ΌμΌ', columns='λ²κ·μλ°μ ν', values='μ¬κ³ μ')

# λ°μ΄ν° μκ°ν
st.markdown("### λ°μ΄ν° μκ°ν")

st.write("- λ²κ·μλ°λ³ μ¬κ³ κ±΄μ")

fig, ax = plt.subplots(figsize=(16,4))
sns.barplot(data=df_r, x=df_r.index, y='μ¬κ³ μ', ci=None)
plt.title("λ²κ·μλ°λ³ μ¬κ³ κ±΄μ")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- λ²κ·μλ°λ³ λΆμ₯μμ")

sns.barplot(data=df_r2, x=df_r.index, y='μ¬κ³ μ', ci=None)
plt.title("λ²κ·μλ°λ³ λΆμμμ")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- λ²κ·μλ°λ³ μ¬λ§μμ")

sns.barplot(data=df_r3, x=df_r3.index, y='μ¬κ³ μ', ci=None)
plt.title("λ²κ·μλ°λ³ μ¬λ§μμ")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- μ£ΌμΌλ³ λ²κ·μλ°λ³ μ¬κ³ κ±΄μ")

fig, ax = plt.subplots(figsize=(16,4))
p2 = px.histogram(df_ac, x='μ£ΌμΌ', y='μ¬κ³ μ', color='λ²κ·μλ°μ ν', barmode="group",
            title='μ£ΌμΌλ³ λ²κ·μλ°λ³ μ¬κ³ κ±΄μ')
p2

st.write("- μ£ΌμΌλ³ λ²κ·μλ°λ³ λΆμμμ")

fig, ax = plt.subplots(figsize=(16,4))
p3 = px.histogram(df_in, x='μ£ΌμΌ', y='μ¬κ³ μ', color='λ²κ·μλ°μ ν', barmode="group",
            title='μ£ΌμΌλ³ λ²κ·μλ°λ³ λΆμμμ')
p3

st.write("- μ£ΌμΌλ³ λ²κ·μλ°λ³ μ¬λ§μμ")

fig, ax = plt.subplots(figsize=(16,4))
p4 = px.histogram(df_de, x='μ£ΌμΌ', y='μ¬κ³ μ', color='λ²κ·μλ°μ ν', barmode="group",
            title='μ£ΌμΌλ³ λ²κ·μλ°λ³ μ¬λ§μμ')
p4

st.markdown("""
    ### λ²κ·μλ°λ³ μκ°νλ₯Ό ν΅ν λΆμ
    1. μ νΈμλ°κ³Ό μμ κ±°λ¦¬λ―Ένλ³΄μ μ¬κ³ κ° κ°μ₯ λ§λ€.
        - λ§€ κ΅ν΅μ¬κ³ μ νν λ°μνλ κ΅ν΅μ¬κ³ μ μμΈμ΄λ―λ‘ λ²μ κ°νν  νμκ° μλ€.
    2. κ³ΌμμΌλ‘ μΈν μ¬λ§μκ° λ§λ€.
        - κ΅ν΅μ¬κ³ μ μ¬λ§μλ₯Ό μ€μ΄κΈ° μν΄μλ κ³Όμνμ λμ μμ μ λ μ μν΄μΌ νλ€.
    3. μΌκ°μλ μ νΈμλ° λ°μ΄ν°κ° μλ±νκ² λλ€.
        - μΌκ°μλ μ νΈλ₯Ό λ¬΄μνλ κ²½ν₯μ΄ λμ κ²μ΄ μμΈμ΄λ―λ‘ μ νΈλ₯Ό μ² μ νκ² μ§μΌμΌ νλ€.

    
    ### κ°μ€ κ²μ¦
    1. μ±κ²©μ΄ κΈν νκ΅­μΈμ νΉμ±μ κ³ λ €νμ¬ μ νΈμλ°μ μ¬κ³ κ° κ°μ₯ λ§μ κ²μ΄λ€.        
        -> μ νΈμλ°μ μ¬κ³ κ° κ°μ₯ λ§μ κ²μ μ μ μμλ€.        
        -> μμ κ±°λ¦¬μ λ―Ένλ³΄μ μ¬κ³ λ λ§μ΄ λ°μνλ€.              
    2. μΌκ°μλ μ°¨κ° λ§μ§ μμ μ νΈλ₯Ό λ¬΄μνλ μ¬λλ€μ΄ λ§μ κ²μ΄λ€.          
        -> μΌκ°μλ μ νΈλ₯Ό λ¬΄μνλ μ¬λλ€μ΄ λ§μλ€.        
        -> κ³ΌμμΌλ‘ μΈν μ¬λ§μλ λ§μ΄ λ°μνλ€.              
""")

