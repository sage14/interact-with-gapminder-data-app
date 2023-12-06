import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

df = pd.read_csv("Data/gapminder_tidy.csv")

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())
metric_labels={"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

def format_metric(metric_raw): 
    return metric_labels[metric_raw]

# choose continent and metric using selectboxes
with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options=metric_list, format_func=format_metric)

query = f"continent=='{continent}' & metric=='{metric}'"

df_filtered = df.query(query)

title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x="year", y="value", color="country", title=title,
              labels={"value": f"{metric_labels[metric]}"})
fig.update_traces(mode='markers+lines')

st.plotly_chart(fig, use_container_width=True)

st.markdown(F"This plot shows the {metric_labels[metric]} for countries in {continent}.")

show_data = True
if show_data:
    st.dataframe(df_filtered)
