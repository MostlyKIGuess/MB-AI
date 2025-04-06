import streamlit as st

def apply_styling():
    """Apply custom CSS styling to the app."""
    st.markdown("""
    <style>
        body {
            background: #2b2b2b; 
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            max-width: 900px;
            margin: 0 auto;
            background-color: #2b2b2b;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
            color: #ffffff;
        }
        .st-expander {
            background-color: #3a3a3a;
            border: 2px solid #4caf50;
            border-radius: 10px;
            padding: 10px;
        }
        .st-expander-header {
            font-size: 18px;
            font-weight: bold;
            color: #4caf50;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .chat-message.user {
            background-color: #4caf50;
            color: #ffffff;
            border: 2px solid #388e3c;
        }
        .chat-message.bot {
            background-color: #1e88e5;
            color: #ffffff;
            border: 2px solid #1565c0;
        }
        .chat-message .avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
            background-color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            font-weight: bold;
            color: #000000;
        }
        .chat-message .message {
            flex: 1;
            padding: 0 10px;
        }
        .stButton>button {
            background-color: #4caf50;
            color: white;
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
            background-color: #3a3a3a;
            color: #ffffff;
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
        
        * Learn about music concepts
        * Generate music lesson plans
        * Explore musical topics
        
        Try asking for a lesson plan or any questions about music!
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
    """Get user input from chat interface."""
    return st.chat_input("Ask something about Music Blocks...")
