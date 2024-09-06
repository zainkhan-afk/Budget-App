from data import get_user_data
import streamlit as st

def tap_populator(tab, username):
    with tab:
        user_info = get_user_data(username)

        account_cols = st.columns([1 / len(user_info["accounts"]) for _ in range(len(user_info["accounts"]))], gap="medium")

        for i in range(len(account_cols)):
            with account_cols[i]:
                account_name = list(user_info["accounts"].keys())[i]
                account_amount = user_info["accounts"][account_name]
                
                st.metric(account_name, account_amount)

