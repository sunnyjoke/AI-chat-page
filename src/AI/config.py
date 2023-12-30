import openai
from dotenv import load_dotenv
import os

print("Config module executed")

def load_configuration():
    """Load environment variables and set up API keys."""
    
    # Load environment variables from .env file
    load_dotenv()

    # Set the API key for OpenAI
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    return os.getenv("OPENAI_API_KEY")

class Config:
    # General configuration variables
    SECRET_KEY = 'your_secret_key'
    # other general configurations..

class TestConfig(Config):
    TESTING = True
    # Define other configurations specific for testing
    # For example, using a different database for tests
    DATABASE_URI = 'sqlite:///:memory:'  # Example for using in-memory SQLite
    # Disable CSRF tokens for form testing (optional, but simplifies form submission testing)
    WTF_CSRF_ENABLED = False
