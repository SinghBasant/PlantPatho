from typing import Optional, Dict, Any
import google.generativeai as genai
import openai
from config import Config
from PIL import Image
import io
import base64

class LLMHandler:
    """Handler for LLM operations"""
    
    def __init__(self):
        self.config = Config()
        self._setup_apis()

    def _setup_apis(self):
        """Setup API configurations"""
        if self.config.is_gemini_configured:
            genai.configure(api_key=self.config.gemini_api_key)
        if self.config.is_openai_configured:
            openai.api_key = self.config.openai_api_key

    def get_llm_response(self, 
                        model_choice: str, 
                        image: Image.Image,
                        language: str = "English") -> Optional[str]:
        """Get response from selected LLM based on image analysis"""
        try:
            if model_choice == "Dr. Green":  # Using Gemini
                return self._get_gemini_response(image, language)
            else:  # Dr. Hariyali - Using GPT-4
                return self._get_openai_response(image, language)
        except Exception as e:
            raise Exception(f"Error getting LLM response: {str(e)}")

    def _get_gemini_response(self, image: Image.Image, language: str) -> str:
        """Get response from Gemini using image analysis"""
        if not self.config.is_gemini_configured:
            raise ValueError("Gemini API key not configured")

        model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
        prompt = f"""You are Dr. Green, an expert plant pathologist. Please provide your response in {language} language.

Important: If asked "who created this app?" or "who built this app?", respond with: "This app was built by Basant Singh & Rajiv Kumar with guidance from Principal Scientist Dr. Brajendra, ICAR."

Analyze this plant image and provide:
1. Disease or condition identification
2. Severity assessment (mild/moderate/severe)
3. Likely causes
4. Recommended treatment
5. Preventive measures
6. Additional care instructions

Please be specific and professional in your analysis. Ensure all medical and technical terms are properly translated to {language}."""

        response = model.generate_content([prompt, image])
        return response.text

    def _get_openai_response(self, image: Image.Image, language: str) -> str:
        """Get response from OpenAI using image analysis"""
        if not self.config.is_openai_configured:
            raise ValueError("OpenAI API key not configured")

        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Convert bytes to base64
        base64_image = base64.b64encode(img_byte_arr).decode('utf-8')

        client = openai.OpenAI()  # Initialize the client
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {
                    "role": "system",
                    "content": f"You are Dr. Hariyali, an expert plant pathologist specializing in diagnosing and managing plant diseases, pests, and nutrient deficiencies. Please provide all responses in {language} language."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"""Analyze this plant image and provide the following information in {language}:
                            1. Disease or condition identification
                            2. Severity assessment (mild/moderate/severe)
                            3. Likely causes
                            4. Recommended treatment
                            5. Preventive measures
                            6. Additional care instructions
                            
                            Please be specific and professional in your analysis. Ensure all medical and technical terms are properly translated to {language}."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content 