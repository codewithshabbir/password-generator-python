import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")
st.title('🔐 Advanced Password Generator')
st.write('Generate a secure password with custom options!')

def passwordGenerator(length, useUpperCase, useLowerCase, useDigits, useSpecialCharacters):
    characters = ""

    if useUpperCase:
        characters += string.ascii_uppercase

    if useLowerCase:
        characters += string.ascii_lowercase

    if useDigits:
        characters += string.digits
    
    if useSpecialCharacters:
        characters += string.punctuation

    if not characters:
        return "Please Select at least one Option!"

    return ''.join(random.choice(characters) for _ in range(length))


length = st.slider("🔐 Password Length", min_value=6, max_value=32, value=12)
useUpperCase = st.checkbox("🔠 Uppercase Letters (A-Z)", value=True)
useLowerCase = st.checkbox("🔡 Lowercase Letters (a-z)", value=True)
useDigit = st.checkbox("🔢 Numbers (0-9)", value=False)
useSpecialCharacters = st.checkbox("💢 Special Characters (@, #, !, etc.)", value=False)
visibility = st.radio("🔍 Show Password As:", ["Plain Text", "Hidden"])

if st.button("🔑 Generate Password"):
    password = passwordGenerator(length, useUpperCase, useLowerCase, useDigit, useSpecialCharacters)

    if password != "Please Select at least one Option!":
        st.success("✅ Password Generated Successfully!")
        if visibility == "Plain Text":
            st.text_input("Generated Password:", value=password, key="password")
        else:
            st.text_input("Generated Password:", value=password, key="password", type="password")

        st.write("📋 Copy Password into Clipboard:")
        st.code(password, language="plaintext")
    else:
        st.error("⚠️ Please select at least one character type!")


st.divider()

st.write("Made with ❤️ by [Muhammad Shabbir](https://codewithshabbir.vercel.app/)")