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
