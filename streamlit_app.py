import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Bölcsesség generátor")

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

if st.button("Adj egy bölcs gondolatot"):
    with st.spinner("Gondolkodom..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": "Írj egy rövid bölcs gondolatot az életről."}
            ]
        )

        text = response.choices[0].message.content
        st.write(text)