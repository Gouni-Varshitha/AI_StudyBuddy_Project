import streamlit as st

# Import the functions and dataset from your existing file
from study_buddy import study_topics, get_response

# Streamlit app design
st.title("AI-Based Study Buddy")
st.write("Ask a study-related question, and I'll help you understand the topic!")

# Input from the user
user_input = st.text_input("Enter your study question:")

# Get response and display it
if user_input:
    response = get_response(user_input)
    st.subheader("Response:")
    st.write(response)