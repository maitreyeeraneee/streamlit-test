import streamlit as st
import requests

st.title("🔗 Blockchain Fact Generator")

openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if openai_api_key:
    if st.button("Generate a Blockchain Fact"):
        headers = {
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json"
        }

        prompt = "Give me one interesting fact about Blockchain technology."

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5,
            "max_tokens": 100
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            blockchain_fact = result['choices'][0]['message']['content']
            st.success(blockchain_fact)
        else:
            st.error("Failed to get a fact. Check your API Key.")
