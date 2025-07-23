import os
import streamlit as st
import google.generativeai as genai

# Configure API key for Gemini
genai.configure(api_key="AIzaSyD6SDscACPzOP54Vf7HEAMU1Atb7YloCfo")

# Translation function
def translate_text(text, target_language):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"translate \"{text}\" to {target_language}",
                ],
            },
        ]
    )

    response = chat_session.send_message("INSERT_INPUT_HERE")
    return response.text

# Streamlit app interface
st.title('Sharadha')

# Input field for the text to translate
text_to_translate = st.text_input("Enter the text you want to translate:")

# Language selection dropdown
languages = ["Hindi", "Spanish", "French", "German", "Italian", "Japanese"]
target_language = st.selectbox("Select the target language:", languages)

# Translate button
if st.button("Translate"):
    if text_to_translate:
        translated_text = translate_text(text_to_translate, target_language)
        st.write(f"Original Text: {text_to_translate}")
        st.write(f"Translated to {target_language}: {translated_text}")
    else:
        st.error("Please enter text to translate.")


