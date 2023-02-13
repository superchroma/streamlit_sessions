import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests
import csv
import datetime
from datetime import datetime, timedelta


# date time
today = st.date_input(f"Date: {datetime.now()}")
# 200 for a successful response or 500 for a server error.


# create title
st.title("ESSEXLab Session Tracking")



def save_data(data):
    with open("lab_study_participants.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def main():
    st.title("ESSEXLab Study")

    study_names = ['study a', 'study b', 'study c']
    selected_study = st.selectbox("Select study name:", study_names)

    study_department = ['department a', 'department b', 'department c']
    selected_department = st.selectbox("Select study department:", study_department)

    data = []
    session_date = datetime.now().strftime("%Y-%m-%d")

    for i in range(30):
        participant_name = st.text_input(f"Enter Participant Name {i+1}: ")
        sona_id = st.text_input(f"Enter SONA ID {i+1}: ")
        start_time = st.text_input(f"Enter Start Time {i+1}: ")
        end_time = st.text_input(f"Enter End Time: {i+1}")
        payment = st.text_input(f"Enter Payment: {i+1}")
        data.append([session_date, selected_department, selected_study, participant_name,
                     sona_id, start_time, end_time, payment])
        st.write('___')

    if st.button("Submit"):
        save_data(data)
        st.success("Data saved successfully!")

if __name__ == "__main__":
    main()

