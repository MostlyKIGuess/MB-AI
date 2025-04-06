import streamlit as st
from PIL import Image
from config import initialize_api, initialize_session_state, get_system_prompt
from ui import setup_page, show_about, display_header, display_chat_history, get_user_input
from chat import generate_response, update_chat_history, generate_image_analysis
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
    
    uploaded_image = st.session_state.get('uploaded_image', None)
    
    if prompt:
        if uploaded_image:
            with st.spinner("Analyzing image..."):
                image = Image.open(uploaded_image)
                response = generate_image_analysis(client, image, prompt)
                st.session_state.uploaded_image = None  # clear once processed
        else:
            sentiment = detect_sentiment(prompt)
            if sentiment:
                response = get_response_for_sentiment(sentiment)
            elif is_greeting(prompt):
                response = "Hello! How can I assist you today?"
            else:
                response = generate_response(client, prompt, st.session_state.is_first_message)
                if st.session_state.is_first_message:
                    st.session_state.is_first_message = False                
                if "generate lesson plan" in prompt.lower() or "create lesson plan" in prompt.lower():
                    topic = prompt.lower().replace("generate lesson plan", "").replace("create lesson plan", "").strip()
                    file_path = save_response_to_docx(response, topic)
                    response += f"\n\nI've saved this lesson plan as a PDF. You can download it from the sidebar."
        
        update_chat_history(prompt, response)

if __name__ == "__main__":
    main()

