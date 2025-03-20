import streamlit as st
from chatbot.bot import ChatBot
import base64

# Function to load and encode images
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Load and encode images
city_image = load_image("city.png")
background_image = load_image("background.avif")
map_image = load_image("map2.png")

# Initialize the chatbot
chatbot = ChatBot()

# Streamlit app
st.markdown(
    f"""
    <style>
    .banner {{
        background-image: url('data:image/png;base64,{city_image}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 150px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2em;
        font-weight: bold;
    }}
    .stApp {{
        background-image: url('data:image/avif;base64,{background_image}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Banner
st.markdown('<div class="banner">Homee by Star Homes</div>', unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Initialize session state for viewing properties
if 'view_properties' not in st.session_state:
    st.session_state.view_properties = False

def show_welcome_page():
    st.write("Welcome to Homee by Star Homes. Let's help you make your right move.")
    if st.button("Let's Go!"):
        st.session_state.page = 'chatbot'

def show_chatbot_page():
    st.write("Welcome to the House Finder Homee!")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Initialize session state for user input key
    if 'user_input_key' not in st.session_state:
        st.session_state.user_input_key = 0

    # Add initial message if chat history is empty
    if not st.session_state.chat_history:
        st.session_state.chat_history.append({"sender": "HOMEE", "message": "Hi, welcome to STAR Homes. How can we help you today? I can answer queries such as 'show me properties in east London to rent' or provide tips for renting in London."})

    # Create a placeholder for the chat history
    chat_placeholder = st.empty()

    # Display chat history
    with chat_placeholder.container():
        for chat in st.session_state.chat_history:
            if chat['sender'] == "You":
                st.markdown(f"<div style='background-color: #e6f7ff; padding: 10px; border-radius: 5px; margin-bottom: 5px;'>{chat['sender']}: {chat['message']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-bottom: 5px;'>{chat['sender']}: {chat['message']}</div>", unsafe_allow_html=True)

    # User input
    user_message = st.text_input("You:", key=f"user_input_{st.session_state.user_input_key}")

    if st.button("Send"):
        if user_message.strip():
            # Display user message
            st.session_state.chat_history.append({"sender": "You", "message": user_message})

            # Process user input and get bot response
            full_conversation = "\n".join([f"{chat['sender']}: {chat['message']}" for chat in st.session_state.chat_history])
            bot_response = chatbot.process_input(full_conversation)
            st.session_state.chat_history.append({"sender": "", "message": bot_response})

            # Check if the bot response contains "couple of options" or "here are some options"
            if "couple of options" in bot_response.lower() or "Here are a few properties" in bot_response.lower() or "here are some options" in bot_response.lower():
                st.session_state.view_properties = True

            # Clear the input box by re-rendering it with a different key
            st.session_state.user_input_key += 1
            st.rerun()

    # Display the "View properties" button if the bot response contains "couple of options" or "here are some options"
    if st.session_state.view_properties:
        if st.button("View properties"):
            st.image("map2.png", caption="Map of Properties")
            st.session_state.view_properties = False

# Navigation
if st.session_state.page == 'welcome':
    show_welcome_page()
elif st.session_state.page == 'chatbot':
    show_chatbot_page()
