import os
from typing import Optional
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
        # Load environment variables from .env file
        load_dotenv()
        
        # API Keys
        self.gemini_api_key: Optional[str] = os.getenv('GEMINI_API_KEY')
        self.openai_api_key: Optional[str] = os.getenv('OPENAI_API_KEY')

    @property
    def is_gemini_configured(self) -> bool:
        """Check if Gemini API is configured"""
        return bool(self.gemini_api_key)

    @property
    def is_openai_configured(self) -> bool:
        """Check if OpenAI API is configured"""
        return bool(self.openai_api_key)

    def get_api_key(self, model: str) -> Optional[str]:
        """Get API key for specified model"""
        if model.lower() == 'gemini':
            return self.gemini_api_key
        elif model.lower() == 'openai':
            return self.openai_api_key
        return None 