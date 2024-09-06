import streamlit as st
from helper_functions import tap_populator
import data
from db_interface import DBInterface


db_interface = DBInterface()

if 'user' not in st.session_state:
    st.session_state['user'] = None

if 'user_logged_int' not in st.session_state:
    st.session_state['user_logged_int'] = None

st.set_page_config(
    page_title="App",
    layout="wide",
    # initial_sidebar_state="expanded"
    )

st.markdown("### App")


form = st.form("my_form")
user_email = form.text_input("Email")
user_password = form.text_input("Password")
login_pressed = form.form_submit_button("Login")

if login_pressed:
    successful = db_interface.authenticate_user(user_email)

# with st.sidebar:
#     st.markdown("### Sidebar")


# tabs = st.tabs(list(data.data.keys()))

# i = 0
# for tab in tabs:
#     tap_populator(tab, list(data.data.keys())[i])
#     i += 1

# container = st.container(border = True)
# cols = container.columns([0.1, 0.15, 0.25, 0.3, 0.2])
# print(list(data.data.keys()))
# with cols[0]:
#     st.selectbox("user", list(data.data.keys()), key = f"user_selector_{username}")

# with cols[1]:
#     st.radio("type", ["d", "c"], key = f"fund_type_{username}")

# with cols[2]:
#     st.selectbox("Ba", ["b1", "b2", "b3", "b4"], key = f"account_name_{username}")

# with cols[3]:
#     st.text_input("Am", f"amount_entered_{username}")

# with cols[4]:
#     st.write("Add")
#     st.button("Add", key = f"add_transaction_{username}")