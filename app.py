import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('Housing')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
population_filter = st.slider('Minimal Median Housing Value', 0.0, 50001.0, 600)  # min, max, default

# create a multi select
location_type = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
form = st.sidebar.form("income level")
country_filter = form.text_input('Choose income level', 'ALL')
form.form_submit_button("Apply")


# filter by population
df = df[df.population >= population_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_type)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)


# show the plot
st.subheader(' histogram of the median house value')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)