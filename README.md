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

---
Made with 💚 in Hyderabad, India 