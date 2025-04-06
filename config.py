import streamlit as st
import os
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig

def initialize_api():
    """Initialize the Google API client."""
    if 'GOOGLE_API_KEY' not in st.secrets:
        st.warning("Please set your Google API key in Streamlit secrets.")
        api_key = st.text_input("Enter your Google API Key:", type="password")
        if api_key:
            return genai.Client(api_key=api_key)
        return None
    return genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def initialize_session_state():
    """Initialize session state variables."""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'lesson_plan' not in st.session_state:
        st.session_state.lesson_plan = ""
    if 'topic' not in st.session_state:
        st.session_state.topic = ""
    if 'is_first_message' not in st.session_state:
        st.session_state.is_first_message = True

def get_system_prompt():
    """Return the system prompt for the AI assistant."""
    return """You are Music Blocks Assistant, an expert in music education.

Your primary role is to help teachers and students work with Music Blocks, a programming environment that helps young people explore musical concepts through coding.

When responding:
- Provide clear, age-appropriate explanations about musical concepts
- Suggest engaging coding activities that connect programming with musical exploration
- Create structured lesson plans when requested, including learning objectives, materials needed, step-by-step activities, and assessment strategies
- Include examples of how to implement musical ideas 
- Be encouraging and foster a growth mindset toward both music and programming
- Reference the provided documentation to ensure accuracy in your responses
- Maintain memory of the entire conversation history, referring back to previous exchanges when relevant

Always maintain a supportive, enthusiastic tone that inspires creativity at the intersection of music and technology."""
