from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")