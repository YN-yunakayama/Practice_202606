import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('売上ダッシュボード練習')

df = pd.read_csv("streamlit_dashboard_sample.csv")

st.sidebar.header("表示設定")

metric = st.sidebar.selectbox("グラフに表示する項目",["売上","利益","注文数","顧客数"])

region = st.sidebar.multiselect("地域",df["地域"].unique(),default=df["地域"].unique())

category = st.sidebar.multiselect("カテゴリ",df["カテゴリ"].unique(),default=df["カテゴリ"].unique())

filtered_df = df[(df["地域"].isin(region)) & (df["カテゴリ"].isin(category))]

chart_df = (filtered_df.groupby("年月",as_index=False)[metric].sum())

st.subheader(f"{metric}の推移")

fig, ax = plt.subplots()
ax.plot(chart_df["年月"],chart_df[metric], marker="o")
ax.set_xlabel("年月")
ax.set_ylabel(metric)
ax.tick_params(axis="x",rotation=45)

st.pyplot(fig)

st.subheader("データ")
st.dataframe(filtered_df)



