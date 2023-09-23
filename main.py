import streamlit as st 
import pandas as pd

import data 

def main(): 
    st.markdown('<h1 style="color:#4B7CA7;font-size:24px;">Coin Collection of Firuz</h1>', unsafe_allow_html=True) 
    st.write("")
    
    coin_data_new, coin_data_old, short_list_data = data.load_data()

    total_number = coin_data_new['Count'].sum() + coin_data_old['Count'].sum() + short_list_data['Count'].sum()
    total_types  = coin_data_new['Type'].sum()  + coin_data_old['Type'].sum() + short_list_data['Type'].sum()

    st.info("Total number of coins: **{}**".format(total_number), icon='💰')
    st.info("Total number of coin types: **{}**".format(total_types))

    st.write("List of top countries and number of coins")
    st.dataframe(coin_data_new)

    st.write("List of old countries and number of coins")
    st.dataframe(coin_data_old)

    st.write("List of countries and number of coins")
    st.dataframe(short_list_data)


if __name__ == '__main__':
    main() 
