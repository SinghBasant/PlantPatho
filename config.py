import os
import logging
from dotenv import load_dotenv

class Config:
    """Configuration management class"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize configuration by loading environment variables"""
        # Load environment variables from .env file if it exists
        load_dotenv()
        
        # Try to get API keys from Streamlit secrets first (for cloud deployment)
        try:
            import streamlit as st
            self.gemini_api_key = st.secrets.get("GEMINI_API_KEY")
            self.openai_api_key = st.secrets.get("OPENAI_API_KEY")
        except Exception as e:
            logging.warning(f"Streamlit secrets not available: {str(e)}")
            # Fall back to environment variables
            self.gemini_api_key = os.getenv("GEMINI_API_KEY")
            self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Check if API keys are configured
        self.is_gemini_configured = bool(self.gemini_api_key)
        self.is_openai_configured = bool(self.openai_api_key)

        # Log configuration status
        if not self.is_gemini_configured:
            logging.warning("Gemini API key not configured")
        if not self.is_openai_configured:
            logging.warning("OpenAI API key not configured")

    def get_gemini_api_key(self) -> str:
        if not self.is_gemini_configured:
            raise ValueError("Gemini API key not configured")
        return self.gemini_api_key

    def get_openai_api_key(self) -> str:
        if not self.is_openai_configured:
            raise ValueError("OpenAI API key not configured")
        return self.openai_api_key

    def get_api_key(self, model: str) -> str:
        """Get API key for specified model"""
        if model.lower() == 'gemini':
            return self.get_gemini_api_key()
        elif model.lower() == 'openai':
            return self.get_openai_api_key()
        raise ValueError(f"Unknown model: {model}") 