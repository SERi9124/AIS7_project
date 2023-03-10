import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="Aanlysis of traffic accident",
    page_icon="đ",
    layout="wide",
)

st.title("âą ě/ěěź/ěę°ëëł")

url = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/time_zones.csv"

@st.cache
def load_data():
    df = pd.read_csv(url, encoding="utf-8", index_col=0)
    return df


st.markdown("")
st.markdown("")

df = load_data()



# <sidebar>

# ě
st.sidebar.header('đ User Input Features')
selected_month = st.sidebar.multiselect("â ě", df["ě"].unique(), df["ě"].unique())

# ěěź
selected_day = st.sidebar.multiselect("â ěěź", df["ěěź"].unique(), df["ěěź"].unique())

# ěę°ë
selected_time1 = st.sidebar.multiselect("â ěę°ë", df["ěę°ë"].unique(), df["ěę°ë"].unique())


# ě
if len(selected_month) > 0:
    df = df[df["ě"].isin(selected_month)]

# ěěź
if len(selected_day) > 0:
    df = df[df["ěěź"].isin(selected_day)]

# ěę°ë
if len(selected_time1) > 0:
    df = df[df["ěę°ë"].isin(selected_time1)]


st.subheader("đ 2021ë ęľíľěŹęł  ë°ě´í° đ")
st.markdown("")

st.subheader("đ DataFrame")
st.dataframe(df)

st.markdown("---")
st.markdown("")




# <ěëł>
st.subheader("â ěëł")

st.markdown("")
st.markdown('''**đ ę°ě¤**
- **ěŹëŚ í´ę°ě˛ , `07ě` ~ `08ě`ęłź ę°ě íë˝ě˛ , `10ě` ~ `11ě`ě ěŹęł  ęą´ěę° ë§ě ę˛ě´ë¤.**''')

df1 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["ě", "ęą´ě"]].groupby("ě").sum()

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df1, x=df1.index, y="ęą´ě", ci=None)
sns.pointplot(data=df1, x=df1.index, y="ęą´ě", ci=None)
plt.axhline(df1["ęą´ě"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**ěëł ěŹęł  ęą´ě**")
tab1.pyplot(plt)

tab2.markdown("**ěëł ěŹęł  ęą´ě**")
tab2.dataframe(df1.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 08ěě íęˇ  ěŹęł  ęą´ěěë ëŻ¸ěšě§ ëŞťíęł  ěë¤.   
- ę°ěĽ ë§ě´ ë°ěí ëŹě 10ěě´ęł , 11ě, 07ě ęˇ¸ ë¤ëĽź ěëŹęł  ěë¤.
- ę°ěĽ ě ę˛ ë°ěí ëŹě 02ěëĄ ëíëŹë¤.''')

st.markdown("")
st.markdown("---")
st.markdown("")


# <ěěźëł>
st.subheader("â ěěźëł")

st.markdown("")
st.markdown('''**đ ę°ě¤**
- **ěśí´ęˇźě íë `íěź`ě´ ěŁźë§ëł´ë¤ ěŹęł ę° ë§ě´ ë°ěí  ę˛ě´ë¤.**
- **íěź ě¤ěěë `ę¸ěěź`ě ěŹęł ę° ę°ěĽ ë§ě´ ë°ěí  ę˛ě´ë¤.**''')

day_of_week = list("ěíěëŞŠę¸í ěź")
df2 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["ěěź", "ęą´ě"]].groupby("ěěź").sum().reindex(day_of_week)

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df2, x=df2.index, y="ęą´ě", palette="husl", ci=None)
sns.pointplot(data=df2, x=df2.index, y="ęą´ě", ci=None)
plt.axhline(df2["ęą´ě"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**ěěźëł ěŹęł  ęą´ě**")
tab1.pyplot(plt)

tab2.markdown("**ěěźëł ěŹęł  ęą´ě**")
tab2.dataframe(df2.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - í ěěźęłź ěźěěźě íęˇ ě ë°ëë ę˛ěźëĄ ëíëŹë¤.  
- ę¸ěěźě ę°ěĽ ë§ě´ ë°ěíęł , ěźěěźě ę°ěĽ ě ę˛ ë°ěíë ę˛ěźëĄ ëíëŹë¤.''')

st.markdown("")
st.markdown("")

df3 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["íěź/ěŁźë§", "ęą´ě"]].groupby("íěź/ěŁźë§").mean().reindex(["íěź", "ěŁźë§"])

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df3, x=df3.index, y="ęą´ě", palette="husl", order=["íěź", "ěŁźë§"], ci=None)
plt.axhline(df3["ęą´ě"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**íěź/ěŁźë§ ěŹęł  ë°ě íęˇ **")
tab1.pyplot(plt)

tab2.markdown("**íěź/ěŁźë§ ěŹęł  ë°ě íęˇ **")
tab2.dataframe(df3.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - íěźě´ ěŁźë§ëł´ë¤ ë ë§ě´ ë°ěí ę˛ěźëĄ ëíëŹë¤.''')


st.markdown("")
st.markdown("---")
st.markdown("")


# <ěę°ëëł>
st.subheader("â ěę°ëëł")

st.markdown("")
st.markdown('''**đ ę°ě¤**
- **í´ęˇź ěę°ě¸ `18 ~ 20ě`ě ěŹęł  ęą´ěę° ę°ěĽ ë§ě ę˛ě´ë¤.**
- **ě¤ě ëł´ë¤ ě´ëëě´ ë§ě `ě¤í`ě ěŹęł  ęą´ěę° ë ë§ě ę˛ě´ë¤.**
- **ěŁźę°ëł´ë¤ `ěźę°`ě ěŹęł  ęą´ěę° ë ë§ě ę˛ě´ë¤.**''')
st.caption('''- ěŁźę° : 08 ~ 18ě
- ěźę° : 18 ~ 08ě''')
st.markdown("")

df4 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["ěę°ë", "ęą´ě"]].groupby("ěę°ë").sum()

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df4, x=df4.index, y="ęą´ě", ci=None)
sns.pointplot(data=df4, x=df4.index, y="ęą´ě", ci=None)
plt.axhline(df4["ęą´ě"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**ěę°ëëł ěŹęł  ęą´ě**")
tab1.pyplot(plt)

tab2.markdown("**ěę°ëëł ěŹęł  ęą´ě**")
tab2.dataframe(df4.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 02 ~ 04ěě ěŹęł  ęą´ěę° ę°ěĽ ě ęł , 18 ~ 20ě ěŹęł  ęą´ěę° ę°ěĽ ë§ě ę˛ěźëĄ ëíëŹë¤.
- 02ěëśí° 20ěęšě§ ěŹęł  ęą´ěę° ě ě°¨ ěŚę°íęł  ěë ę˛ěźëĄ ëíëŹë¤.
- 22ěëśí° 08ěęšě§ ěŹęł  ęą´ěę° íęˇ ě ë°ëë ę˛ěźëĄ ëíëŹë¤.''')

st.markdown("")
st.markdown("")

df5 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["ě¤ě /ě¤í", "ęą´ě"]].groupby("ě¤ě /ě¤í").sum()

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df5, x=df5.index, y="ęą´ě", palette="husl", ci=None)
plt.axhline(df5["ęą´ě"].mean(), c="r", lw=1, ls="--");
tab1.markdown("**ě¤ě /ě¤í ěŹęł  ë°ě ęą´ě**")
tab1.pyplot(plt)

tab2.markdown("**ě¤ě /ě¤í ěŹęł  ë°ě ęą´ě**")
tab2.dataframe(df5.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - ě¤ě ëł´ë¤ ě¤íě ë ë§ě´ ë°ěí ę˛ěźëĄ ëíëŹë¤.''')



st.markdown("")
st.markdown("")

df6 = df.loc[df["ěŹęł ě í"] == "ěŹęł ęą´ě", ["ěŁźę°/ěźę°", "ęą´ě"]].groupby("ěŁźę°/ěźę°").mean().reindex(["ěŁźę°", 'ěźę°'])

tab1, tab2 = st.tabs(["đ Chart", "đ Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df6, x=df6.index, y="ęą´ě", palette="husl", ci=None)
plt.axhline(df6["ęą´ě"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**ěŁźę°/ěźę° ěŹęł  ë°ě íęˇ **")
tab1.pyplot(plt)

tab2.markdown("**ěŁźę°/ěźę° ěŹęł  ë°ě íęˇ **")
tab2.dataframe(df6.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - ěźę°ëł´ë¤ ěŁźę°ě ë ë§ě´ ë°ěí ę˛ěźëĄ ëíëŹë¤.''')

st.markdown("")
st.markdown("---")
st.markdown("")


# <ë˛ěŁźëł ěíĽ>
st.subheader("â ë˛ěŁźëł ěíĽ")
st.markdown("")
tab1, tab2, tab3 = st.tabs(["đ Chart1", "đ Chart2", "đ Chart3"])

pv1 = df.pivot_table(index="ěěź", columns="ě", values="ęą´ě")
pv1 = pv1.reindex(index=list("ěíěëŞŠę¸í ěź"))

plt.figure(figsize=(15, 10))
sns.heatmap(pv1, annot=True, fmt=".2f", cmap="flare")
tab1.markdown("**ě/ěěźě ë°ëĽ¸ ěŹęł  ë°ě íęˇ **")
tab1.pyplot(plt)


pv2 = df.pivot_table(index="ěę°ë", columns="ěěź", values="ęą´ě")
pv2 = pv2.reindex(columns=list("ěíěëŞŠę¸í ěź"))

plt.figure(figsize=(15, 10))
sns.heatmap(pv2, annot=True, fmt=".2f", cmap="flare")
tab2.markdown("**ěěź/ěę°ëě ë°ëĽ¸ ěŹęł  ë°ě íęˇ **")
tab2.pyplot(plt)


pv3 = df.pivot_table(index="ěę°ë", columns="ě", values="ęą´ě")

plt.figure(figsize=(15, 10))
sns.heatmap(pv3, annot=True, fmt=".2f", cmap="flare");
tab3.markdown("**ě/ěę°ëě ë°ëĽ¸ ěŹęł  ë°ě íęˇ **")
tab3.pyplot(plt)




st.markdown("")
st.markdown("---")
st.markdown("")


# <ę˛°ëĄ >
st.subheader("â ę˛°ëĄ ")

st.markdown("")
st.success(''' - ęľíľěŹęł ë **ę°ě íë˝ě˛ **ě ę°ěĽ ë§ě´ ë°ěíë¤.
- ěěźě ę¸°ě¤ěźëĄ **íěź**, ęˇ¸ě¤ěěë **ę¸ěěź**ě ěŹęł ę° ë§ě´ ë°ěíë¤.
- ěę°ě ę¸°ě¤ěźëĄ **ě¤í**, ęˇ¸ě¤ěěë í´ęˇźěę°ě¸ **18ě-20ě**ě ěŹęł ę° ë§ě´ ë°ěíë¤.
- ě°¨ë ě´ëě´ ë§ě ěě ęłź ěŹęł  ęą´ěę° ëšëĄí ę˛ě íěí  ě ěë¤.''')

st.markdown("")
st.markdown("")
st.caption("ěŹěŠí ë°ě´í° : [ëëĄęľíľęłľë¨_TAAS] - ěěźëł ěę°ëëł ęľíľěŹęł  (http://taas.koroad.or.kr/)")

st.markdown("")
st.markdown("")
st.caption(''' <ě°¸ěĄ° ę¸°ěŹ>
- http://www.wonjutoday.co.kr/news/articleView.html?idxno=127301
- https://m.khan.co.kr/national/national-general/article/202110011213001#c2b
- http://www.nspna.com/news/?mode=view&newsid=598721
- https://www.safetynews.co.kr/news/articleView.html?idxno=213458''')
