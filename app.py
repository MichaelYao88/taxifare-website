import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time

- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
import datetime
import requests
import pandas as pd

d = pd.to_datetime(st.date_input(
    "When's your pickupday",
    datetime.date(2019, 7, 6)))

pickup_lat = st.number_input('plat')


pickup_lon = st.number_input('plon')


dropoff_lat = st.number_input('dlat')


dropoff_lon = st.number_input('dlon')


passengers = st.slider('passengers', 1, 8, 1)




'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

X_pred = dict(
        pickup_datetime=d,
        pickup_longitude=[pickup_lon],
        pickup_latitude=[pickup_lat],
        dropoff_longitude=[dropoff_lon],
        dropoff_latitude=[dropoff_lat],
        passenger_count=[passengers],
        )

response = requests.get(url,X_pred).json()

response
