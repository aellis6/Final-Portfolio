#Hire Anya Ellis

import streamlit as st

st.title("Hire Anya Ellis")
st.subheader("Summary")
st.write("Anya Ellis is a promising supply chain future executive with a background in extensive technical skills you need like SQL and Microsoft Excel.")
st.write("Anya Ellis is an IE major with a Business minor at a hiring target school..")


st.header("Onboarding Information")
st.write("Student at Target School - Ga Tech")
st.write("US Citizen")
st.write("Not a veteran")
st.write("Technical Skills: YES")
st.write("People Skills: YES")
st.write("Behavior Interview Summary: ACED")


st.write("You know I am a 5 star candidate for your internship!")
st.feedback("stars") #NEW


st.image("images/chooseme.gif", caption="Please rate me a 5 star candidate. Choose me for the intern position.", use_container_width=True)

st.write("So you've decided I'm a great fit for your company...now what?")


st.header("Test Job Offer")

st.subheader("Compensation")

st.write ("What is the compensation for the role?")

#NEW
def hr_to_sal():
    st.session_state.sal = st.session_state.hr*40*50

def sal_to_hr():
    st.session_state.hr = st.session_state.sal/(40*50)


col1, buff, col2 = st.columns([2,1,2])
with col1:
    Hourly = st.number_input("Hourly:", key = "hr",
                on_change = hr_to_sal, step=1)
with col2:
    Salary = st.number_input("Salary:", key = "sal",step=10000,
                on_change = sal_to_hr)
st.subheader("Start Date")
with st.form("job_offer_form"):
    start_date = st.date_input("Select your start date:")
    submit_button = st.form_submit_button("Submit Offer")

    if submit_button:
        st.success(f"Offer submitted! Start Date: {start_date}")