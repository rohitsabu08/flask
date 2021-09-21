# Importing the required package
from flask import Flask, render_template, request
import streamlit as st

def praxis():
        st.title("Learning Streamlit")
        name = st.text_input("Student_name","Type Here")
        roll_no = st.text_input("Roll_no","Type Here")
        result = ""
        if st.button("Print_result"):
            st.success(f"The student name is {name} with roll no {roll_no}")

if __name__=="__main__":
    praxis()