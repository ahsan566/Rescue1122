import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

st.title('Rescue 1122 data explorer')
st.header('From 2004 to 2018')
st.write('Source: ' + 'http://www.datastories.pk/download/rescue-data-1122-10-10-2004-07-11-2018/' )
# st.text('_______________________________________________________')
'''
___
'''

@st.cache
def load_rescue_data():
    data = pd.read_csv('data/data.csv')
    return data

@st.cache
def load_punjab_data():
    data = gpd.read_file('data/punjab_data_final.geojson')
    return data

@st.cache
def load_punjab_data_csv():
    data = pd.read_csv('data/punjab_data_final.csv')
    return data

# data_load = st.text("Loading data...")
df = load_punjab_data()
df2 = load_punjab_data_csv()
# data_load.text("Loading data... done!")

st.sidebar.text("Created by: Ahsan Fayyaz")
st.sidebar.text("")
st.sidebar.title('Options')

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")

if st.sidebar.checkbox('Show raw data'):
    st.subheader("Raw data")
    st.write(df2)

st.sidebar.text("")

if st.sidebar.checkbox('Show full map'):
    df['geometry'].plot()
    plt.title("Punjab")
    plt.axis('off')
    st.pyplot(plt)

st.sidebar.text("")
st.sidebar.text("")

division = st.sidebar.selectbox(
    'Select a division',
    df['division'].unique()
)

st.sidebar.text("")
st.sidebar.text("")

if division:
    l = list(df[df['division']==division]['district'])
    district = st.sidebar.selectbox(
        'Select a district',
        [x.title() for x in l]
    )

district = district.lower()

df[df['district'].str.contains(district)]['geometry'].plot(color='#FB5455')
plt.title(district.title())
# plt.figure(figsize=(30,20))
plt.axis('off')
st.pyplot(plt)


st.subheader(district.title())
value = df[df['district']==district].index
val = df.loc[value]
x = val.drop('geometry', axis=1)
st.table(x.T.squeeze())

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("Created by: Ahsan Fayyaz")
