import streamlit as st

from config import initialize_api, initialize_session_state, get_system_prompt
from ui import setup_page, show_about, display_header, display_chat_history, get_user_input
from chat import generate_response, update_chat_history
from sentiment import detect_sentiment, is_greeting, get_response_for_sentiment
from file_handler import ensure_directories, load_guide_context, save_response_to_docx

def main():
    setup_page()
    ensure_directories()
    
    initialize_session_state()
    
    if 'system_prompt' not in st.session_state:
        st.session_state.system_prompt = get_system_prompt()    
    if 'guide_context' not in st.session_state:
        st.session_state.guide_context = load_guide_context()
    
    client = initialize_api()
    if not client:
        st.error("API client couldn't be initialized. please give davlid api key")
        return
    
    show_about()
    display_header()
    display_chat_history()    
    prompt = get_user_input()
    
    if prompt:
        sentiment = detect_sentiment(prompt)
        if sentiment:
            response = get_response_for_sentiment(sentiment)
        elif is_greeting(prompt):
            response = "Hello! How can I assist you today?"
        else:
            response = generate_response(client, prompt, st.session_state.is_first_message)
            if st.session_state.is_first_message:
                st.session_state.is_first_message = False        
        update_chat_history(prompt, response)

if __name__ == "__main__":
    main()

