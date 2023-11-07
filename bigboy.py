import streamlit as st
from streamlit_extras.let_it_rain import rain
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


birthday = date(2000, 10, 7)
today = datetime.now()

age = relativedelta(today, birthday).years

if datetime.strftime(today, "%m-%d") == "11-07":
    icon = "🎂"
else:
    icon = "🤨"


st.set_page_config(page_icon=icon, page_title="Hashim", layout="centered")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if datetime.strftime(today, "%m-%d") == "11-07":

    if "button_pressed" not in st.session_state:
        st.session_state["button_pressed"] = False

    if not st.session_state["button_pressed"]:
        hashim_button = st.button("Klicka här")

        if hashim_button:
            st.session_state["button_pressed"] = True
            st.rerun()

    if st.session_state["button_pressed"]:
        st.title(f"🎉Grattis Hashim på {age} år🎉")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.image("bigboy-horse.jpeg")
        rain("🎈", animation_length="infinite")

else:
    if (today.month == 11 and today.day > 7) or today.month == 12:
        birthday_this_year = date(today.year + 1, 11, 7)
    else:
        birthday_this_year = date(today.year, 11, 7)

    delta_days = relativedelta(birthday_this_year, today)
    st.title(f"Kom tillbaka om {delta_days.months} månader "
             f"och {delta_days.days} dagar")
