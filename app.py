import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚"
)

st.title("📚 Smart Study Planner")

name = st.text_input(
    "Enter Your Name"
)

subjects = st.text_input(
    "Enter Subjects (comma separated)"
)

hours = st.slider(
    "Study Hours Per Day",
    1,
    12,
    4
)

exam = st.date_input(
    "Select Exam Date"
)

priority = st.selectbox(
    "Priority",
    [
        "High",
        "Medium",
        "Low"
    ]
)

if st.button(
    "Generate Plan"
):

    subject_list = subjects.split(",")

    st.subheader(
        "Your Study Plan"
    )

    for sub in subject_list:

        st.write(
            f"Study {sub.strip()} → {round(hours/len(subject_list),1)} hrs"
        )

    if priority == "High":

        st.success(
            "Daily Revision Recommended"
        )

    elif priority == "Medium":

        st.info(
            "Maintain Consistency"
        )

    else:

        st.warning(
            "Increase Study Time"
        )
