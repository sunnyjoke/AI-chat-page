import openai
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash

def load_configuration():
    """Load environment variables and set up API keys."""
    
    # Load environment variables from .env file
    load_dotenv()

    # Set the API key for OpenAI
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    return os.getenv("OPENAI_API_KEY")


class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'chat-users'


config = {
    'development': DevelopmentConfig
}

"""
print(generate_password_hash("write here you're password"))
"""