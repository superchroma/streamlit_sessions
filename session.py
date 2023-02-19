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

num_participants = st.number_input("Enter number of participants: ", min_value=1, max_value=35)


def save_data(data):
    with open("lab_study_participants.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def main():
    study_names = ["HUGHES_KHAN_MENGEL - MENGEL1219A"
            "MENGEL1219B"
            "Public Opinion Study (VANCOPPEN-1121)"
            "Interactions of first and second language (SOTOGARCIA-0122) pilot"
            "Buy Now, Pay Later (BROOKS-0422)"
            "Language attitudes and dialect identification in England (COLE-0422)"
            "Simple Voting - DIANAT-0222"
            "Voting Experiment (DIANAT-0222)"
            "ENGLISH MONOLINGUALS: Interactions of first and second language (SOTOGARCIA-0122)"
            "ENGLISH-SPANISH BILINGUALS: Interactions of first and second language (SOTOGARCIA-0122)"
            "SPANISH HERITAGE SPEAKERS: Interactions of first and second language (SOTOGARCIA-0122)"
            "Social processing of naturalistic social interactions - DAUGHTERS-0422"
            "ENGLISH MONOLINGUALS (2-part): Interactions of first and second language (SOTOGARCIA-0122) - Part 1"
            "ENGLISH MONOLINGUALS (2-part): Interactions of first and second language (SOTOGARCIA-0122) - Part 2"
            "SPANISH NATIVE SPEAKERS 2-part: Interactions of first and second language (SOTOGARCIA-0122) - Part 1"
            "SPANISH NATIVE SPEAKERS 2-part: Interactions of first and second language (SOTOGARCIA-0122) - Part 2"
            "Does the Beauty beat the Beast? (FULLARD-0122O)"
            "Why copy others' financial decisions? (FREER-0522)"
            "DIANAT-0522 - Conspicuous Consumption in the Lab"
            "Listening and feeling together (CHIU-0622)"
            "Decision Making Study (MENGEL-0722)"
            "BHALOTRA-0422EX - The impact of leaders on team performance"
            "Intake survey for 2-hour lab study!"
            "Invitation only: Emotional and physiological reactions to music, speech and sounds (CHIU-0622)"
            "Social Judgement (VANDOLDER-0622)"
            "Invitation only: Emotional and physiological reactions to music and sounds (CHIU-0622)"
            "Meditation and mood visualisation study: emotional andphysiological reactions to speech  (CHIU-0622)"
            "NAVYTE-1022 Affective Vicarious Touch"]
    selected_study = st.selectbox("Select study name:", study_names)

    study_department = ['department a', 'department b', 'department c']
    selected_department = st.selectbox("Select study department:", study_department)

    data = []
    session_date = datetime.now().strftime("%Y-%m-%d")

    for i in range(num_participants):
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

