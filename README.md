# Dr. Green - Plant Disease Diagnosis System 🌿

Dr. Green is an AI-powered plant pathology system that helps diagnose plant diseases using advanced Large Language Models (LLMs). The system supports multiple Indian languages and provides detailed diagnosis and treatment recommendations.

## Features 🌟

- **Multi-Language Support**: Supports English, Hindi, Bengali, Marathi, Punjabi, Tamil, and Telugu
- **Dual AI Models**: Choose between two AI pathologists (Dr. Green using Gemini and Dr. Hariyali using GPT-4)
- **Comprehensive Analysis**: Get detailed information about:
  - Disease identification
  - Severity assessment
  - Likely causes
  - Recommended treatments
  - Preventive measures
  - Additional care instructions
- **Secure Access**: Protected with access code system
- **User-Friendly Interface**: Clean, intuitive design with Streamlit

## Setup Instructions 🚀

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/dr-green.git
   cd dr-green
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## System Requirements 💻

- Python 3.8 or higher
- Internet connection for API access
- Supported operating systems: Windows, macOS, Linux

## Usage Guide 📖

1. Launch the application
2. Enter the access code
3. Select your preferred AI doctor and language
4. Upload a clear photo of the affected plant
5. Click "Diagnose & Share Action Report"
6. Review the comprehensive analysis and recommendations

## Project Structure 📁

```
dr-green/
├── app.py              # Main Streamlit application
├── config.py           # Configuration and environment setup
├── llm_utils.py        # LLM handling utilities
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (not in repo)
└── README.md          # Project documentation
```

## Contributors 👥

- Basant Singh
- Rajiv Kumar

## Guidance 🎓

- Dr. Brajendra - Principal Scientist ICAR

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- ICAR for guidance and support
- OpenAI and Google for AI APIs
- Streamlit for the wonderful framework

## Contact 📧

For any queries or support, please contact:
- Basant Singh
- Rajiv Kumar

## Deployment to Streamlit Cloud 🚀

1. **Create a Streamlit Cloud Account**
   - Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account

2. **Deploy Your App**
   - Click "New app" in your Streamlit Cloud dashboard
   - Select your GitHub repository
   - Choose the main branch
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Configure Secrets**
   - In your app's settings, go to "Secrets"
   - Add your API keys:
   ```toml
   [secrets]
   GEMINI_API_KEY = "your-gemini-api-key"
   OPENAI_API_KEY = "your-openai-api-key"
   ```

4. **Access Your App**
   - Your app will be available at `https://yourusername-dr-green.streamlit.app`
   - Share this URL with users who have the access code

## Local Development vs Cloud Deployment 🔄

- **Local Development**: Uses `.env` file for API keys
- **Cloud Deployment**: Uses Streamlit Secrets for API keys
- The app automatically detects the environment and uses the appropriate configuration

---
Made with 💚 in Hyderabad, India 