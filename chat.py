import streamlit as st
from google.genai import types

def generate_response(client, query, is_first_message=False):
    """Generate AI response to user query."""
    if 'chat_session' not in st.session_state:
        st.session_state.chat_session = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=st.session_state.system_prompt
            )
        )
        
        if is_first_message and hasattr(st.session_state, 'guide_context'):
            st.session_state.chat_session.send_message(
                f"Here is the Music Blocks documentation to reference when answering questions:\n\n{st.session_state.guide_context}\n\nPlease use this documentation to help answer user questions accurately."
            )
    
    response = st.session_state.chat_session.send_message(query)
    
    return response.text

def update_chat_history(prompt, response):
    """Update chat history with new message and response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

def generate_image_analysis(client, image, question):
    """Generate analysis of an uploaded image using the Gemini model."""
    try:
        image_system_prompt = """You are Music Blocks Assistant, an expert in music education, analyzing an image.
When analyzing music-related images:
- Identify musical notation, instruments, or Music Blocks interface elements
- Provide educational insights about what's shown in the image
- Point out any errors or issues in musical notation or instrument setups
- Suggest improvements or teaching opportunities based on what you see
- Connect observations to Music Blocks programming concepts when relevant
- Maintain a supportive, encouraging tone appropriate for music education
- If sheet music is present, analyze the notes, rhythm, and structure
- If Music Blocks code is visible, explain what the code would do

Always maintain context that you're helping teachers and students learn about music through programming with Music Blocks."""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=image_system_prompt
            ),
            contents=[
                question,
                image
            ]
        )
        return response.text
    except Exception as e:
        return f"Error analyzing image: {str(e)}"
