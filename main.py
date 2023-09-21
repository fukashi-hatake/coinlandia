import streamlit as st 
import pandas as pd

import data 

def main(): 
    st.markdown('<h1 style="color:#4B7CA7;font-size:24px;">Coin Collection of Firuz</h1>', unsafe_allow_html=True) 

    coin_data = data.load_data()

    st.dataframe(coin_data)


if __name__ == '__main__':
    main() 