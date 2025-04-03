import streamlit as st
from PIL import Image
import logging
from config import Config
from llm_utils import LLMHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize configuration
config = Config()
llm_handler = LLMHandler()

# Configure page
st.set_page_config(
    page_title="Dr. Green | वनस्पति मित्र",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for green theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f7f4;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
    }
    .css-1d391kg {
        background-color: #e8f5e9;
    }
    .error-msg {
        color: #d32f2f;
        padding: 10px;
        border-radius: 5px;
        background-color: #ffebee;
        margin: 10px 0;
    }
    .success-msg {
        color: #2e7d32;
        padding: 10px;
        border-radius: 5px;
        background-color: #e8f5e9;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Access code verification
def check_access_code():
    if 'access_granted' not in st.session_state:
        st.session_state.access_granted = False

    if not st.session_state.access_granted:
        st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌿 Dr. Green👨‍⚕️वनस्पति मित्र 🌾వనస్పతి మిత్ర 🍀</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Access Verification Required</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            access_code = st.text_input("Please enter access code:", type="password")
            if st.button("Verify Access"):
                if access_code == "1947":
                    st.session_state.access_granted = True
                    st.rerun()
                else:
                    st.error("❌ Incorrect access code. Please try again. Else contact Basant/Rajiv")
        return st.session_state.access_granted
    return True

# Main app logic
if check_access_code():
    # Title and header
    st.title("👨‍⚕️Dr. Green🌿वनस्पति मित्र 🌾వనస్పతి మిత్ర 🍀")
    st.markdown("<h3 style='text-align: center; color: #2e7d32;'>Your Expert Plant Pathologist</h3>", unsafe_allow_html=True)

    # Sidebar for LLM selection
    with st.sidebar:
        st.markdown("### Choose Your Doctor")
        st.markdown("Two Pathologists at your service:")
        llm_choice = st.radio(
            label="Doctor Selection",  # Added label for accessibility
            options=["Dr. Green 👨‍⚕️", "Dr. Hariyali 👩‍⚕️"],
            index=0,
            label_visibility="collapsed"  # Hide the label but keep it accessible
        )
        
        st.markdown("### Select Response Language")
        language_choice = st.radio(
            label="Language Selection",  # Added label for accessibility
            options=["English", "Hindi", "Bengali", "Marathi", "Punjabi", "Tamil", "Telugu"],
            index=0,
            label_visibility="collapsed"  # Hide the label but keep it accessible
        )
        
        # Check if API keys are configured
        if llm_choice == "Dr. Green" and not config.is_gemini_configured:
            st.warning("⚠️ Gemini API key not found in environment variables")
        elif llm_choice == "Dr. Hariyali" and not config.is_openai_configured:
            st.warning("⚠️ OpenAI API key not found in environment variables")

    # Main content area
    st.markdown("""
        ### Welcome to Dr. Green's Pathology Lab!
        Diagnose & Treat crop problems with 3-Steps process: #1. Upload a clear photo of the affected plant #2. Click Diagnose & Share Actionable Report #3. Check the Report & Act.
    """)

    # Image upload section
    uploaded_file = st.file_uploader(
        "Step #1. Upload a photo of the affected plant",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear, well-lit photo of the plant showing the symptoms"
    )

    # Display uploaded image if available
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Plant Image", use_container_width=True)
            
            # Add analyze button
            if st.button("Step #2. Diagnose & Share Action Report", type="primary"):
                try:
                    # Check if selected model's API key is configured
                    if (llm_choice == "Dr. Green" and not config.is_gemini_configured) or \
                       (llm_choice == "Dr. Hariyali" and not config.is_openai_configured):
                        st.error("Selected model's API key is not configured. Please check your environment variables.")
                        st.stop()

                    with st.spinner("Analyzing your plant's condition..."):
                        try:
                            # Get LLM response
                            response = llm_handler.get_llm_response(
                                model_choice=llm_choice.replace(" 👨‍⚕️", "").replace(" 👩‍⚕️", ""),  # Remove emojis for model selection
                                image=image,
                                language=language_choice
                            )
                            
                            # Display response
                            if response:
                                st.markdown("### Step#3 Diagnosis Report & Action Items")
                                st.markdown(response)
                            else:
                                st.error("Unable to generate diagnosis. Please try again.")
                                
                        except Exception as e:
                            logger.error(f"Error during LLM processing: {str(e)}")
                            st.error(f"An error occurred while processing your request: {str(e)}")

                except Exception as e:
                    logger.error(f"Analysis error: {str(e)}")
                    st.error("An unexpected error occurred. Please try again later.")
                    
        except Exception as e:
            logger.error(f"Image processing error: {str(e)}")
            st.error("Error processing the uploaded image. Please try a different image.")

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center'>
            <p>🌱 Dr. Green - Crafted with 💓 Hyderabad, India By Basant Singh; Rajiv Kumar. Guided by Dr. Brajendra - Principal Scientist ICAR</p>
            <p>Your trusted Plant Pathologist. April 2025</p>
        </div>
        """, unsafe_allow_html=True) 