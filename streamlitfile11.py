#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open(r"C:\Users\talha\Downloads\pipe.pkl", 'rb'))

def main():
    st.title("Car Selling Price Prediction")

    name = st.text_input("Car Name")
    year = st.number_input("Year", min_value=1950, max_value=2023)
    km_driven = st.number_input("Kilometers Driven")
    fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer', 'Trustmark Dealer'])
    transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
    owner = st.selectbox("Owner", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])

    user_data = {'name': name,
                 'year': year,
                 'km_driven': km_driven,
                 'fuel': fuel,
                 'seller_type': seller_type,
                 'transmission': transmission,
                 'owner': owner}

    user_df = pd.DataFrame(user_data, index=[0])

    try:
        prediction = model.predict(user_df)
        st.subheader("Predicted Selling Price")
        st.write("The predicted selling price for the car is:", prediction)
    except AttributeError as e:
        st.error("Error: {}".format(e))

if __name__ == "__main__":
    main()


# In[ ]:




