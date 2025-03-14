import streamlit as st
import pandas as pd
import json
st.title("Anya's Accolades")

#Certifications



st.header("Certifications")
st.subheader("Completed")
st.write("1. GE Supply Chain Simulation")
st.write("2. CITI Emory Research Training")
st.write("3. GADOE International Skills Diplomacy Seal")
st.subheader("In Progress")
#In progress
st.write("1. Google Data Analytics Proffessional Certificate")
if 'In Progress Certs' not in st.session_state:
    st.session_state['In Progress Certs'] = 1
st.write(f"Anya is working on {st.session_state['In Progress Certs']} certification(s)!")
button = st.button("Add Certification")
if button:
    st.session_state['In Progress Certs']+=1
dynamic_data = [x*st.session_state['In Progress Certs']  for x in range(1, 30)]

st.line_chart(dynamic_data)

st.write("---")






#Awards/Accolades
st.header("Awards and Accolades")

st.subheader("College")
st.write("March 2025- Gary S. May Leadership Shadow Certificate of Achievement")
st.write("March 2025- Most Outgoing GT Freshman Leader")
st.write("January 2025- Faculty Honors for Fall 2024")
st.write("July 2024- Campus Life Award")
st.write("July 2024- Top Student Award")


st.subheader("High School")
st.write("National African American Award")
st.write("National Merit Scholar Finalist")
st.write("AP Scholar with Distinction")
st.write("AP Scholar with Honors")
st.write("Georgia Certificate of Merit")
st.write("Georgia Tech President Stamps Semifinalist")
st.write("---")
st.subheader("Scholarships")
st.write("I am a motivated student, fully supported by part time jobs and scholarships.")
st.write(f"**I am grateful to be a recipient of these scholarships:**")
st.write("3M Society of Women Engineers Scholar")
st.write("AKA PEARL Foundation Scholar")
st.write("Zell Miller Scholar")
st.write("Montford Point Marines Scholar")
st.write("GT Challenge Scholar")
st.write("HHS PTSA Scholar")
st.write(f"**I currently work these on campus jobs:**")
st.write("Knack Peer Tutor")
st.write("iExperience Campus Ambassador")


import matplotlib.pyplot as plt

st.subheader("Past Scholarship Distributions")


with open('scholarships.json') as f:
    scholarships = json.load(f)

st.subheader("Amount From Each Scholarship")

if scholarships:
    fig, ax = plt.subplots()
    ax.pie(scholarships.values(), labels=scholarships.keys(), autopct="%1.1f%%")
    st.pyplot(fig)


#st.subheader("Submit a Scholarship Link Here!:")
st.subheader("Sponsor Me!")
st.write("How much would you like to donate to further Anya's higher education?")
amount = st.slider("USD", 5, 1000000, key = "slider") #NEWWW

st.write(f"You have elected to donate ${amount} for Anya's Education!")

st.write("What can your donation be used for?")
col1, buff, col2 = st.columns([1,0.5,3]) #NEW

option_names = ["Study Abroad", "Housing", "Food"]

next = st.button("Next option") #NEW

if next:
    if st.session_state["radio_option"] == "Study Abroad":
        st.session_state.radio_option = "Housing"
    elif st.session_state["radio_option"] == "Housing":
        st.session_state.radio_option = "Food"

option = col1.radio("Pick what the donation can be used for:", option_names, key = "radio_option")
st.session_state

if option == "Study Abroad":
    col2.write("You picked study abroad- this will allow me to further my studies of Mandarin in China!")
if option == "Housing":
    col2.write("You picked Housing- this will be used towards essentials in my apartment like toilet paper and cleaning supplies!")
if option == "Food":
    col2.write("Thank you so much! I am a broke college student and so so hungry :heart:") 

#NEW

def load_donations():
    with open('donations.json', 'r') as f:
        data = json.load(f)
    return data.get("total_donations", 0)
        

def save_donations(amount):
    data = {"total_donations": amount}
    with open('donations.json', 'w') as f:
        json.dump(data, f)

total_donations = load_donations()


if st.button("Donate"):
    total_donations += amount  
    save_donations(total_donations)  
    st.success(f"Thank you so much for donating ${amount}!")

st.write(f"Total donations so far: ${total_donations}")

donation_data = {"Total Donations": [total_donations]}
df = pd.DataFrame(donation_data)
st.bar_chart(df)  #NEW