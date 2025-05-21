import streamlit as st

def apply_styling():
    """Apply custom CSS styling to the app."""
    st.markdown("""
    <style>
        body {
        }
        .stApp {
            max-width: 900px;
            margin: 0 auto;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
        }
        .st-expander {
            border: 2px solid #4caf50;
            border-radius: 10px;
            padding: 10px;
        }
        .st-expander-header {
            font-size: 18px;
            font-weight: bold;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            font-family: 'Arial', sans-serif;
        }
        .chat-message.user {
            border: 2px solid #388e3c;
        }
        .chat-message.bot {
            border: 2px solid #1565c0;
        }
        .chat-message .avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            font-weight: bold;
        }
        .chat-message .message {
            flex: 1;
            padding: 0 10px;
        }
        .stButton>button {
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #388e3c;
        }
        .stTextInput>div>div>input {
            border: 2px solid #4caf50;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .upload-container {
            display: flex;
            align-items: center;
            margin-top: 10px;
        }
        .upload-text {
            font-size: 14px;
            margin-right: 5px;
        }
        .stFileUploader > div {
            padding: 0 !important;
        }
        .upload-icon {
            font-size: 24px;
            padding: 5px 10px;
            border-radius: 5px;
            border: 1px solid #4caf50;
            cursor: pointer;
            display: inline-block;
            margin-left: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

def setup_page():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="Music Blocks Assistant",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    apply_styling()

def show_about():
    """Display the about section."""
    with st.expander("🎵 About Music Blocks Assistant", expanded=True):
        st.markdown("""
        **Music Blocks Assistant** helps you:
        
        * Learn about music concepts and programming
        * Generate detailed music lesson plans.
        * Get teaching resources and curriculum ideas
        * Analyze music-related images - just attach an image to your question!
        
        **Try these examples:**
        * "Generate a lesson plan for teaching rhythm to 4th graders"
        * "What are the best ways to introduce programming with Music Blocks?"
        * Upload an image of sheet music and ask "What's wrong with this notation?"
        """)

def display_header():
    """Display the application header."""
    st.title("🎵 Music Blocks Assistant")
    st.markdown("""
    This is a Music Blocks lesson plan creation assistant. Ask questions about music or request a lesson plan!
    """)

def display_chat_history():
    """Display chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    """Get user input from chat interface with image upload option."""
    input_container = st.container()
    
    with input_container:
        prompt = st.chat_input("Ask something about Music Blocks...")
        
        upload_container = st.container()
        with upload_container:
            st.markdown("""
            <div style="display: flex; align-items: center; width: 100%; margin-top: 5px; margin-bottom: 10px;">
                <div style="color: #4caf50; font-size: 14px; display: flex; align-items: center; width: 100%;">
                    <span style="margin-right: 5px;">📎</span> Attach an image for analysis
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_image is not None:
        st.session_state.uploaded_image = uploaded_image
        
        st.markdown("---")
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(uploaded_image, width=100)
        with cols[1]:
            st.markdown("**Image uploaded!** Ask a question about it like:")
            st.markdown("- *'What's wrong with this sheet music?'*")
            st.markdown("- *'Can you analyze this instrument setup?'*")
    
    return prompt
